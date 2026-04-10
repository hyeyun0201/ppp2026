def average(nums):
    result = sum(nums)/len(nums)
    return result
def main():
    nums = str(input("리스트를 작성하시오(큰따옴표 붙여서):"))
    N = nums.split()
    numbers = []
    for x in N:
        numbers.append(int(x))
    print(average(numbers))
if __name__ == "__main__":
    main()