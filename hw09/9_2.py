def get_range_list(n):
    result = []
    for i in range(1,n+1):
        result.append(i)
    return result
def main():
    n = int(input("1-n리스트를 만들어드리겠습니다. n의 값을 입력하세요:"))
    numbers = get_range_list(n)
    # numbers = []
    print(numbers)
if __name__ == "__main__":
    main()

