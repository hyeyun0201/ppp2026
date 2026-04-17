import statistics

def text2list(text):
    num_list = []
    for num_text in text.split():
        num_list.append(int(num_text))
    return num_list
def list_len(nums):
    return len(nums)
def list_avg(nums):
    return sum(nums)/list_len(nums)
def list_max(nums):
    return max(nums)
def list_min(nums):
    return min(nums)
def list_mid(nums):
    return statistics.median(nums)
def main():
     nums = text2list(input("리스트를 입력하시면 개수, 평균, 최댓값, 최솟값, 중앙값을 출력하겠습니다."))
     print(list_len(nums), list_avg(nums), list_max(nums), list_min(nums), list_mid(nums))
if __name__ == "__main__":
    main()
