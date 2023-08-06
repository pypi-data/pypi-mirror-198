from ..model import ChatBotModel


class ChatBot(ChatBotModel):
    """ChatBot对象提供用于与接口交互的各种方法"""

    def __init__(
        self,
        cookieFile: str="",
        cookies = None,
    ):
        """创建ChatBot对象"""
        pass

    def list_history(self):
        """列出历史记录列表"""
        pass

    def check_history(self, sessionId):
        """获取指定历史记录的内容"""
        pass
