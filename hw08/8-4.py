def sum_n(n):
    result = 0
    for i in range(1, n+1):
        result += i
    return result
def main():
    n = int(input("1부터 n의 합을 구하겠습니다. n의 값을 입력하시오:"))
    print(sum_n(n))
if __name__ == "__main__":
    main()
