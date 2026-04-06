import math
weight = int(input("몸무게를 입력하시오 : "))
#height = float(input("키를 입력하시오(m로) :"))
height = int(input("키를 입력하시오(cm) :"))
height /= 100
BMI= weight/math.pow(height,2)
if BMI >= 35:
    print("3단계 비만입니다.")
elif BMI >= 30 and BMI <34.9:
    print("2단계 비만입니다.")
elif BMI >= 25 and BMI < 29.9:
    print("1단계 비만입니다.")
else:
    print("비만 전단계 입니다.")
#math사용하는 조건이 있어서 **2가 아닌 math.pow를 찾아서 작성했습니다!
