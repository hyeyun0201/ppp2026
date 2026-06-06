# 로또 번호 뽑기
import random
import time
import tkinter as tk
from tkinter import simpledialog
chang = tk.Tk()
chang.withdraw()

def gui_input(text):
    return simpledialog.askstring(title="Test", prompt=text)

def ran_num():
    lotto = []
    while len(lotto) < 6:
        result = random.randint(1, 45)
        for k in range(len(lotto)):
            if lotto[k] == result:
                break
        else:
            lotto.append(result)


    return lotto

def main():
    Bun = int(gui_input("로또 번호 몇번 출력할까요"))
    for i in range (Bun):
        print(ran_num())
if __name__ == "__main__":
    main()