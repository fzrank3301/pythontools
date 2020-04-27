import requests, time
from bs4 import BeautifulSoup
from urllib.parse import urlencode
import json
import win32con
import win32gui
import pyperclip
import time
import os
# 用于获得文字
class nmslba:

    def __init__(self,url,count):
        self.count = count
        self.url=url
        self.it =[]


    def nmslPachong(self):
        for i in range(self.count):
            html = requests.get(self.url).content
            soup = BeautifulSoup(html, "html.parser")
            text = soup.find("div", class_="layui-col-xs12 layui-col-sm12 layui-col-md12").text
            self.it.append(text.replace("\r","").replace("\n","").replace(" ",""))
        print(self.it)
        return self.it



#复制粘贴
class QQ:
    def __init__(self,name,nmsllist):
        self.d = ''
        self.to_who=name
        self.string=nmsllist


    def findWindows(self):
       # 循环获得每一项
        for i in self.string:
            time.sleep(2)  #休眠两秒
            pyperclip.copy(i)  #复制i中的内容
            ##根据to_who锁定窗口
            qqwindow = win32gui.FindWindow(None, self.to_who)
            ##粘贴文字到输入框
            win32gui.SendMessage(qqwindow, 258, 22, 2080193)
            win32gui.SendMessage(qqwindow, 770, 0, 0)
            ##发送消息
            win32gui.SendMessage(qqwindow,win32con.WM_KEYDOWN,win32con.VK_RETURN,0)
            win32gui.SendMessage(qqwindow,win32con.WM_KEYUP,win32con.VK_RETURN,0)




if __name__ == '__main__':
    choice = int(input("请问你是想嘴臭还是嘴甜\n1.嘴臭\n2.嘴甜"))
    if (choice == 1):
        url = "https://nmsl8.club/nmsl"
    elif (choice == 2):
        url = "https://nmsl8.club/love"
    else:
        print("你可真是把爷给逗笑了，nmsl，再瞎几把输爷这就去把你你妈骨灰给羊了")
        quit()
    name = input("请输入你要发的人的名字")
    count = int(input("你要发多少次？"))
    nmslit = nmslba(url,count).nmslPachong()
    if nmslit:
        QQ(name,nmslit).findWindows()