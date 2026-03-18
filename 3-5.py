x1 = int(input("x1의 거리를 입력하시오 :"))
y1 = int(input("y1의 거리를 입력하시오 :"))
x2 = int(input("x2의 거리를 입력하시오 :"))
y2 = int(input("y2의 거리를 입력하시오 :"))
Result = ((x2-x1)**2+(y2-y1)**2)**0.5
print("두 지점의 거리는 {}입니다.".format(Result))