def read_rainfall(weather_filename):
    dataset1 = []
    with open(weather_filename, encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            dataset1.append(float(tokens[9]))
    return dataset1

def read_tavg(weather_filename):
    dataset2 = []
    with open(weather_filename, encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            dataset2.append(float(tokens[4]))
    return dataset2

def count_rainy(rainfalls):
    count = 0
    for i in rainfalls:
        if i>= 5:
            count+=1
    return count

def main():
    weather_filename = "weather(146)_2022-2022.csv"
    tavgs = read_tavg(weather_filename)
    print(f"연 평균 온도는 {sum(tavgs)/len(tavgs)}입니다.")
    rainfalls = read_rainfall(weather_filename)
    print(f"총 강수량은 {sum(rainfalls)}입니다.")
    print(f"5mm이상 강우일수는 {count_rainy(rainfalls)}입니다.")

if __name__ == "__main__":
    main()