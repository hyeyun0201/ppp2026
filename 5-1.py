C =input("화씨->섭씨 변환 시 '화씨', 섭씨->화씨 변환 시 '섭씨', 피트->cm 변환 시 '피트', cm->피트 변환 시 'cm'이라고 정확하게 입력하시오. :")
if C == "화씨":
    Num = float(input("화씨를 입력하시오."))
    Result = (Num -32) * 5/9
    print(f"{Num}℉는 섭씨{Result:.1f}입니다.")
elif C == "섭씨":
    Num = float(input("섭씨를 입력하시오."))
    Result = (Num * 9/5) + 32
    print(f"{Num}℃는 화씨{Result:.1f}℉입니다.")
elif C == "피트":
    Num = float(input("피트를 입력하시오."))
    Result = Num * 30.48
    print(f"{Num}ft는 {Result:.1f}㎝입니다.")
elif C == "cm":
    Num = float(input("cm를 입력하시오."))
    Result = Num / 30.48
    print(f"{Num}㎝는 {Result:.1f}ft입니다.")
else:
    print("프로그램을 다시 실행시켜 정확하게 다시 입력해주세요")
