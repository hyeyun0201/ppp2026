#구구단 문제
import random
import PySimpleGUI as sg

problems = []
score =0
num = 0
for i in range(3):
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    problems.append((a,b))   # 문제 저장
    print(f"{i+1}번 : {a}*{b} =")

layout = [
    [sg.Text("1번정답"), sg.Input(key='-A1-')],
    [sg.Text("2번정답"), sg.Input(key='-A2-')],
    [sg.Text("3번정답"), sg.Input(key='-A3-')],
    [sg.Button('채점'), sg.Button('Exit')]
]

window = sg.Window('구구단 퀴즈', layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break

    if event == '채점':
        score = 0

        if int(values['-A1-']) == problems[0][0]*problems[0][1]:
            score += 100

        if int(values['-A2-']) == problems[1][0]*problems[1][1]:
            score += 100

        if int(values['-A3-']) == problems[2][0]*problems[2][1]:
            score += 100

        sg.popup(f"점수는 {score}점입니다.")

window.close()
def main():
    pass
if __name__ == "__main__":
    main()



