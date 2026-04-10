def is_leap_year(y):
    if y%4==0:
        if y%100==0:
            print("False")
        else:
            print("True")
def main():
    y = int(input("연도를 입력하시면 윤년인지 알려드립니다:"))
    is_leap_year(y)
if __name__ == "__main__":
    main()
