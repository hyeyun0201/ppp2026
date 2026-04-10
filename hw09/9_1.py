def average(nums):
    result = sum(nums)/len(nums)
    return result
def main():
    nums = [1,2,3,4,5,6,7,8,9,10]
    print(f"평균 = {average(nums)}")
if __name__ == "__main__":
    main()
