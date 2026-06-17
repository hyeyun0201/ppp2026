import os
os.environ["DISPLAY"] = ":0" #GUI 프로그램이 실행될 때 어느 화면에 창을 띄울지 알려줌 ->라즈베리파이 디스플레이
import RPi.GPIO as gpio
import time
import tkinter as tk
import adafruit_dht
import board
import csv
import matplotlib.pyplot as plt


def main():
    gpio.setmode(gpio.BCM)
    trig = 13 
    echo = 19  
    gpio.setup(trig, gpio.OUT)
    gpio.setup(echo, gpio.IN)
    window = tk.Tk()
    window.title("strawberry smartfarm")
    window.geometry("800x480")
    label = tk.Label(window,text="",font=("Arial",15),justify="left")
    label.place(x=20, y=20)


    dht = adafruit_dht.DHT11(board.D21)
    csv_file = open("/home/hyeyun0201/Desktop/ppp_final/strawberry_data.csv","a",newline="")

    writer = csv.writer(csv_file)
    writer.writerow(["time","temperature","humidity"])

    temp = []
    humi = []

    # 서보 모터
    servo_pin = 18 #핀번호
    gpio.setup(servo_pin,gpio.OUT)
    pwm = gpio.PWM(servo_pin,50)
    pwm.start(0)

    pwm.ChangeDutyCycle(7.5)
    time.sleep(1)
    motor_status = "OFF"

    for i in range(30):
        gpio.output(trig, True)
        time.sleep(0.00001)
        gpio.output(trig, False)

        while gpio.input(echo) == 0:
            pulse_start = time.time()

        while gpio.input(echo) == 1:
            pulse_end = time.time()

        distance = round((pulse_end -pulse_start) *17000, 2) #거리계산방법

        if distance > 8:
            water_status = "LOW"
        else:
            water_status = "NORMAL"

        #온습도 센서
        try:
            temperature = dht.temperature
            humidity = dht.humidity
        except RuntimeError:
            print("DHT11 error")
            continue

        temp.append(temperature)
        humi.append(humidity)

        avg_temp = sum(temp) /len(temp)
        avg_humi = sum(humi) /len(humi)



        # 환경조건 체크
        if 18 <= avg_temp <= 25 and 60 <= avg_humi <= 70:
            environment ="GOOD"
        else:
            environment ="CHECK"

        # 서보모터 조건
        if humidity >= 70:
            pwm.ChangeDutyCycle(12.5)
            motor_status ="ON"
        else:
            pwm.ChangeDutyCycle(7.5)
            motor_status = "OFF"


        label.config(

text=f"""
< Strawberry Smart Farm>
---------------------------
Measurement : {i+1}/30

Current temperature : {temperature}℃
Current humidity : {humidity}%

Average temperature : {avg_temp:.1f}℃
Water status : {water_status}
Average humidity : {avg_humi:.1f}%

Appropriate temperature : 18 ~ 25℃
Appropriate humidity : 60 ~ 70%

Status : {environment}
---------------------------
"""
        )
        window.update()

        #csv파일 저장
        now = time.strftime("%H:%M:%S")
        writer.writerow([now,temperature,humidity])
        csv_file.flush()
        time.sleep(2)

    pwm.stop()
    gpio.cleanup()
    csv_file.close()
    window.destroy()

    # 온습도 그래프 그리기
    plt.figure(figsize=(8,4))
    plt.plot(temp,label="temperature")
    plt.plot(humi,label="humidity")
    plt.title("Strawberry Smart Farm Environment")
    plt.xlabel("measurement")
    plt.ylabel("value")
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == "__main__":
    main()