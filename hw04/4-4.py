import math
R = float(input("반지름을 입력하시오 : "))
C = 2 * math.pi * R
P = math.pi * R**2
print(f"원의 둘레는 {C:.1f}, 원의 면적은 {P:.2f}이다.")
