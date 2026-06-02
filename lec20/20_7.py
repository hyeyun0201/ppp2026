import matplotlib.pyplot as plt
import requests
import os
import pandas as pd
import koreanize_matplotlib

def read_weather(filename):
    dataset = []
    with open(filename, encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(float(tokens[9]))
    return dataset

def download_weather(weather_filename,stid, sy, ey):
    url = f"https://api.taegon.kr/stations/{stid}/?sy={sy}&ey={ey}&format=csv"
    if not os.path.exists(weather_filename):
        resp = requests.get(url)
        with open(weather_filename, "w", encoding="utf-8") as fout:
            fout.write(resp.text)

def main():
    tavg = []
    year = []
    filename = "weather_jeonju_1980_2024.csv"
    download_weather(filename, 146, 1980, 2024)
    df_jj = pd.read_csv(filename, skipinitialspace=True)
    for y in range(1980, 2025) :
        year.append(y)
        tavg.append(df_jj[(df_jj["year"] == y) & (df_jj["month"] ==2) &(df_jj["day"] == 1)]["tavg"].mean())
    for i in range(len(year)):
        if year[i] == 2006:
            birth_temp = tavg[i]
    rank = 1
    for temp in sorted(tavg, reverse=True): #reverse=True는 인터넷 검색을 통해 학습하고 사용했습니다.
        if temp == birth_temp:
            break
        rank += 1

    print(f"2006년은 {rank}번째로 온도가 높다")

    max_temp = max(tavg)
    for i in range(len(tavg)): #가장 높았던 해
        if tavg[i] == max_temp:
            print(f"가장 온도가 높았던 해는 {year[i]}년입니다.")

    min_temp = min(tavg)
    for i in range(len(tavg)): #가장 낮았던 해
        if tavg[i] == min_temp:
            print(f"가장 온도가 낮았던 해는 {year[i]}년입니다.")

    plt.plot(year, tavg, color="b", label="Jeonju")
    plt.ylabel("평균기온(℃)")
    plt.legend()
    plt.savefig("line_birth_tavg.png")


if __name__ == "__main__":
    main()
