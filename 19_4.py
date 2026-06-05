# 로또 번호 뽑기
import random

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
    Bun = int(input("로또 번호 몇 번 출력할까요? : "))
    for i in range (Bun):
        print(ran_num())
if __name__ == "__main__":
    main()