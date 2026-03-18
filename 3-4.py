import math
R = float(input("반지름을 입력하시오 : "))
C = round(2 * math.pi * R, 1)
P = round(math.pi * R**2,2)
print(f"원의 둘레는 {C}, 원의 면적은 {P}이다.")
