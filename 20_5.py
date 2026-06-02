import matplotlib.pyplot as plt
import numpy as np
import koreanize_matplotlib
import requests
import os
import pandas as pd

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
    if not os.path.exists(weather_filename):#파일이 없으면
        resp = requests.get(url)
        with open(weather_filename, "w", encoding="utf-8") as fout:
            fout.write(resp.text)

def main():
    year =[]
    t_jj =[]
    t_sw =[]
    filename = "weather_jeonju_1980_2024.csv"
    download_weather(filename, 146, 1980, 2024)
    df_jj = pd.read_csv(filename, skipinitialspace=True)
    filename_sw = "weather_suwon_1980-2024.csv"
    download_weather(filename_sw, 119, 1980, 2024)
    df_sw = pd.read_csv(filename_sw, skipinitialspace=True)

    for y in range(1980, 2025) :
        year.append(y)
        t_jj.append(df_jj[df_jj["year"] ==y]["tavg"].mean()) #.mean()은 인터넷으로 찾아본 후 사용했습니다.
        t_sw.append(df_sw[df_sw["year"] == y]["tavg"].mean())
    plt.plot(year,t_jj, color="r", label="Jeonju")
    plt.plot(year,t_sw, color="b", label="Suwon")
    plt.ylabel("평균기온(℃)")
    plt.legend()
    plt.savefig("line_tavg_jj_sw_.png")


if __name__ == "__main__":
    main()
