def read_weather(filename):
    dataset = []
    with open(filename, encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(float(tokens[9]))
    return dataset

def sumifs(rainfalls, months, selected_month=[6,7,8]): # 6,7,8 적으면 메인에서 따로 작성할 필요가 없다
    total_value = 0
    for i in range(len(rainfalls)):
        r = rainfalls[i]
        m = months[i]
        if m in selected_month: #[6,7,8]
            total_value += r
    return total_value

def read_weather_col_int(weather_filename, col_idx=9, conv_fn=float): #값을 안주면 9, float을 준다.
    dataset = []
    with open(weather_filename, encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(conv_fn(tokens[col_idx])) # 정수로 바꿀지 실수로 바꿀지 정함
    return dataset

def main():
    weather_filename = "weather(146)_2001-2022.csv"
    rainfall = read_weather_col_int(weather_filename)
    years = read_weather_col_int(weather_filename, 0, int)
    months = read_weather_col_int(weather_filename, 1)
    summer_rainfall = sumifs(rainfall, months, [6, 7, 8])
    print(f"여름철 강수량(6,7,8월)은 {summer_rainfall:.1f}mm입니다.")
    for y in range(2021, 2023):
        rainfall_y = sumifs(rainfall, years, [y])
        print(f"{y}년 강수량은 {rainfall_y:.1f}mm입니다.")

if __name__ == "__main__":
    main()
