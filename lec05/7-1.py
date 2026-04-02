cal_dict = {"한라봉": 50, "딸기": 34, "바나나": 77}
eat_dict = {"한라봉": 100, "딸기": 200, "바나나": 500 }
total_cal = 0
for fruit, cal in eat_dict.items():
    if fruit in cal_dict:
        total_cal += cal * cal_dict[fruit]
print(total_cal)
