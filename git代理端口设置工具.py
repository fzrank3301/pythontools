import os
import tkinter


while True:
    a = input("请输入要代理的端口号:")
    os.popen(f"git config --global http.proxy http://127.0.0.1:{a}")
    os.popen(f"git config --global https.proxy https://127.0.0.1:{a}")
    # os.popen(f"git config --global http.proxy 'socks5://127.0.0.1:{a}'")
    # os.popen(f"git config --global https.proxy 'socks5://127.0.0.1:{a}'")
    input("设置完成，是否查看")
    b = os.popen("git config --global --get http.proxy").read()
    print(b)
    c = os.popen("git config --global --get https.proxy").read()
    print(c)
    input("按任意键退出")
    os.system("cls")
    