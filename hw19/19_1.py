#카운트다운
import time
def main():
    a = int(input("몇 초 카운트를 할까요"))
    for i in range(a, 0, -1):
        print(i, end="\n")
        time.sleep(1) #1초 멈췄다가 실행
if __name__ == "__main__":
    main()
