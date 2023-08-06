import logging

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from browsermobproxy import Server, Client

import time
import json

class ChatBot:
    """ChatBot对象提供用于与接口交互的各种方法"""

    server: Server = None
    """browsermobproxy.Server对象"""

    driver: webdriver.Chrome = None
    """selenium.webdriver.Chrome对象"""

    proxy: Client = None
    """browsermobproxy.Client对象"""

    already_quit = False

    def __init__(
        self,
        cookieFile: str="",
        cookies: list = None,
        browsermobProxyPath: str="",
        chromeDriverPath: str="",
        headless: bool=True,
    ):
        """创建ChatBot对象"""
        if self.already_quit:
            raise Exception("此对象已销毁")

        if cookieFile == "" and cookies == None:
            raise ValueError("cookieFile和cookies不能同时为空")
        
        if cookieFile != "":
            with open(cookieFile, "r") as f:
                cookies = json.load(f)

        self.__login__(cookies, browsermobProxyPath, chromeDriverPath, headless)

    def __login__(self, cookies, browsermobProxyPath, chromeDriverPath, headless):
        """登录"""

        # 启动browsermobproxy
        self.server = Server(path=browsermobProxyPath)
        self.server.start()
        self.proxy = self.server.create_proxy()

        # 启动Chrome
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument('--headless')
        options.add_argument('--incognito')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
        options.add_argument('window-size=1920x1080')
        options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
        options.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
        options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片,提升速度
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument('log-level=3')
        options.add_argument("--proxy-server={0}".format(self.proxy.proxy))

        if chromeDriverPath != "":
            self.driver = webdriver.Chrome(
                executable_path=chromeDriverPath,
                options=options
            )
        else:
            self.driver = webdriver.Chrome(
                options=options
            )


        # 添加cookies
        self.driver.delete_all_cookies()
        self.driver.get("https://yiyan.baidu.com")
        for cookie in cookies:
            cookie['sameSite'] = 'None'
            self.driver.add_cookie(cookie)

        self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
            Object.defineProperty(navigator, 'webdriver', {
            get: () => false
            })
        """
        })
        # 进入主页
        self.driver.get("https://yiyan.baidu.com")
    
    def quit(self):
        """退出"""
        if not self.already_quit:
            if self.driver != None:
                self.driver.quit()
            if self.server != None:
                self.server.stop()
            self.already_quit = True

    def __del__(self):
        quit()

    def __new_session__(self):
        """创建新的会话"""
        # 点击class为MO979HM2的元素
        WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(By.CLASS_NAME, "MO979HM2")).click()
        
    
    def reset_session(self):
        """重置当前会话"""
        self.__new_session__()

    def ask(self, text: str, timeout: int=60, wait_output: bool=False):
        """向机器人发送消息"""
        self.proxy.new_har("yiyan", {"captureHeaders": False, "captureContent": True})
        # 输入消息
        input_area = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(By.CLASS_NAME, 'wBs12eIN'))

        for word in text:
            time.sleep(0.1)
            input_area.send_keys(word)

        time.sleep(0.8)

        enter_button = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(By.CSS_SELECTOR, "#root > div > div.N_eugr4S > div > div.qyxOCbmP > div.xgTDL7D_ > div.oeNDrlEA > div.bUwIGATa > div:nth-child(3) > span.pa6BxUpp > svg > g > g:nth-child(1)"))
        # 等待enter_button的opacity属性大于0.9
        WebDriverWait(self.driver, timeout=timeout).until(lambda d: float(enter_button.value_of_css_property("opacity")) > 0.9)
        enter_button.click()

        reply = [
            {
                "text": ""
            }
        ]
        # 轮询回复
        count = 0
        while True:
            time.sleep(1)
            enties = self.proxy.har['log']['entries']

            done = False
            reply[0]['text'] = ""

            for enty in enties:
                if 'url' in enty['request'] and (enty['request']['url'] == "https://yiyan.baidu.com/eb/chat/new" or enty['request']['url'] == "https://yiyan.baidu.com/eb/chat/query"):
                    
                    if enty['request']['url'] == "https://yiyan.baidu.com/eb/chat/new":
                        if "text" in enty['response']['content']:
                            resp_text = enty['response']['content']['text']
                            resp_json = json.loads(resp_text)

                            if resp_json['data']['botChat']['message'][0]['content'] != "正在生成中...":
                                reply[0]['text'] += resp_json['data']['botChat']['message'][0]['content']
                                done = True
                                break
                    elif enty['request']['url'] == "https://yiyan.baidu.com/eb/chat/query":
                        if "text" in enty['response']['content']:
                            resp_text = enty['response']['content']['text']
                            resp_json = json.loads(resp_text)

                            reply[0]['text'] += resp_json['data']['text']
                            if resp_json['data']['is_end'] == 1 or resp_json['data']['is_end'] == "1":
                                done = True
                                break
            if done:
                break

            count += 1
            if count > timeout:
                break
        
        if wait_output:
            # 等待网页上输出完
            WebDriverWait(self.driver, timeout=timeout).until(lambda d: float(enter_button.value_of_css_property("opacity")) > 0.9)

        return reply
                    