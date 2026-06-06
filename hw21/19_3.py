#행맨게임i
import random
import PySimpleGUI as sg

def Hangman():
    trial = 7
    list_h = ["apple", "red", "blue", "elephant"]
    answer = random.choice(list_h)
    result = []
    for i in answer: #글자수만큼 언더바 출력
        result.append("_")
    layout = [
        [sg.Text(" ".join(result), key="-Word-")],
        [sg.Text(f"주어진기회 :{trial}", key="-Trial-")],
        [sg.Input(key="-INPUT-", size=8)],
        [sg.Button("확인"), sg.Button("종료")]
    ]
    window = sg.Window("행맨 게임", layout)
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == "종료":
            break
        a = values["-INPUT-"]
        for i in range(len(answer)):
            if answer[i] == a:
                result[i] = a
        window["-Word-"].update(" ".join(result)) #맞춘단어 화면에 출력
        window["-Trial-"].update(f"주어진기회 : {trial}") # 남은 기회 출력
        window["-INPUT-"].update("") # 입력창 비우기
        if "_"not in result:
            print("정답입니다!")
            trial -= 1
            break
        else:
            trial -= 1
        if trial ==0:
            print("게임오버")
            break

def main():
    Hangman()


if __name__ == "__main__":
    main()
