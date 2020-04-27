import os
import tkinter


while True :
    a=input("请输入要关闭的端口号:")
    b = os.popen(f"netstat -ano | findstr {a}").read()
    print(b)
    c=input("请输入你要关闭的pid:")
    d=os.popen(f"taskkill -F /pid {c}").read()
    print(d)
    os.system("cls")
