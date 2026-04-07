def cal(cal_dict,eat_dict):
    total_cal = 0
    for key, val in eat_dict.items():
        if key in cal_dict:
            total_cal += val * cal_dict[key]
    return total_cal
def main():
    cal_dict = {"한라봉": 50, "딸기": 34, "바나나": 77}
    eat_dict = {"한라봉": 100, "딸기": 200, "바나나": 500}
    result = cal(cal_dict,eat_dict)
    print(f"총 칼로리는{result}입니다.")
if __name__ == "__main__":
    main()









