#행맨게임i
import random

def Hangman():
    trial = 7
    result = []
    list_h = ["apple", "red", "blue", "elephant"]
    answer = random.choice(list_h)
    for i in answer: #글자수만큼 언더바 출력
        result.append("_")
    while True:
        print(" ".join(result),f"(trial={trial})")
        a = input("답을 입력하세요(한 개씩) :")
        for i in range(len(answer)):
            if answer[i] == a:
                result[i] = a
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
