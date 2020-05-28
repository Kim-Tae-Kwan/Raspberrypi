#라즈베리파이 Tkinter GUI Programming 학습.
from tkinter import *

root =Tk()

root.title("Callback and Evet Test") # 제목
root.geometry("640x400+20+20") # 틀 크기
def callback():
    exit(1)
    #print("button clicked")

Button(root, text="Quit",width=10,command=callback).pack(padx=10,pady=10) # 버튼 생성

root.mainloop()