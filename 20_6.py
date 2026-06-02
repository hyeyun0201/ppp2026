import matplotlib.pyplot as plt
import requests
import os
import pandas as pd

def download_weather(weather_filename,stid, sy, ey):
    url = f"https://api.taegon.kr/stations/{stid}/?sy={sy}&ey={ey}&format=csv"
    if not os.path.exists(weather_filename):
        resp = requests.get(url)
        with open(weather_filename, "w", encoding="utf-8") as fout:
            fout.write(resp.text)

def main():
    year = []
    rain = []
    filename = "weather_jeonju_1980_2024.csv"
    download_weather(filename, 146, 1980, 2024)
    df_jj = pd.read_csv(filename, skipinitialspace=True)

    fig, ax = plt.subplots(figsize=(15, 6))
    for y in range(1980, 2025) :
        year.append(y)
        rain.append(df_jj[df_jj["year"] ==y]["rainfall"].sum())
    ax.bar(year, rain, color="r")
    ax.set_ylabel("연간강수량(mm)")
    fig.savefig("bar_year_rain.png")


if __name__ == "__main__":
    main()
