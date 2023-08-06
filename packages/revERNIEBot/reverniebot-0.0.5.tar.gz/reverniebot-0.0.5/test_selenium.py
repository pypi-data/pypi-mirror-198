from revERNIEBot import selenium

bot = selenium.ChatBot(
    cookieFile="cookies.json",
    browsermobProxyPath="/workspaces/revERNIEBot/res/browsermob-proxy-2.1.4/bin/browsermob-proxy",
    chromeDriverPath="res/chromedriver",
)

print(bot.ask("早上好！"))

bot.quit()

