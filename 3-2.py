x = int(input("x좌표를 입력하시오 :"))
y = int(input("y좌표를 입력하시오 :"))
if x>0 and y >0:
    print(f"입력한 좌표는({x},{y})는 제 1사분면 입니다.")
elif x < 0 and y > 0:
    print(f"입력한 좌표는({x},{y})는 제 2사분면 입니다.")
elif x < 0 and y < 0:
    print(f"입력한 좌표는({x},{y})는 제 3사분면 입니다.")
else:
    print(f"입력한 좌표는({x},{y})는 제 4사분면 입니다.")

