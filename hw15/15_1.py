import requests
import os

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
    url = f"https://api.taegon.kr/stations/146/?sy=2023&ey=2023&format=csv"
    weather_filename = "weather_2023.csv"
    if not os.path.exists(weather_filename):#파일이 없으면
        resp = requests.get(url)
        with open(weather_filename, "w", encoding="utf-8") as fout:
            fout.write(resp.text)

    tavgs = read_tavg(weather_filename)
    rainfalls = read_rainfall(weather_filename)
    with open("result.txt","w", encoding="utf-8") as fout:
        fout.write(f"연 평균 기온은 {sum(tavgs) / len(tavgs)}도\n5mm 이상 강우일수는 {count_rainy(rainfalls)}일\n총 강우량은 {sum(rainfalls)}입니다. ")

if __name__ == "__main__":
    main()
