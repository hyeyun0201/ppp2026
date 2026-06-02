import os
import requests
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
    filename = "weather_jeonju_1980_2024.csv"
    download_weather(filename,146,1980,2024)
    df_jj = pd.read_csv(filename, skipinitialspace=True)
    filename_sw = "weather_suwon_1980-2024.csv"
    download_weather(filename_sw, 119, 1980, 2024)
    df_sw = pd.read_csv(filename_sw, skipinitialspace=True)
    print(f"전주시 2012년 강수량은 {(df_jj[df_jj["year"]==2012]["rainfall"].sum())}입니다")
    print(f"전주시 2024년 최고기온은 {(df_jj[df_jj["year"] == 2024]["tavg"].max())}입니다.")
    df_jj["tdiff"] = df_jj["tmax"] - df_jj["tmin"]
    print(f"전주시 2020년 최고 일교차는 {(df_jj[df_jj["year"] == 2020]["tdiff"].max())}입니다.")
    prec_jj = df_jj[df_jj["year"] == 2019]["rainfall"].sum()
    prec_sw = df_sw[df_sw["year"] == 2019]["rainfall"].sum()
    print(f"수원시와 전주시의 2019년 총강수량 차이는 {(abs(prec_jj - prec_sw))}입니다.")



if __name__ == "__main__":
    main()