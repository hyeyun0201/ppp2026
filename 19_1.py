#카운트다운
import time
import tkinter as tk
from tkinter import simpledialog
chang = tk.Tk()
chang.withdraw()

def gui_input(text):
    return simpledialog.askstring(title="Test", prompt=text)


def main():
    a = int(gui_input("몇 초 카운트를 할까요"))
    for i in range(a, 0, -1):
        print(i, end="\n")
        time.sleep(1) #1초 멈췄다가 실행
if __name__ == "__main__":
    main()









