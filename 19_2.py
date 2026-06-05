#구구단 문제
import random
def gugudan():
    a = random.randint(2,9)
    b = random.randint(2,9)
    result = input(f"{a}*{b}=?")
    return int(result) == a*b


def main():
    score =0
    num = 0
    print("5개의 구구단 문제를 내겠습니다.(각100점)")
    for i in range(5):
        if gugudan():
            score += 100
            num += 1
    print(f"{num}개 맞았고, 총 점수는 {score}입니다.")
if __name__ == "__main__":
    main()