H = int(input("한라봉 몇 g 섭취하셨나요?"))
S = int(input("딸기 몇 g 섭취하셨나요?"))
B= int(input("바나나 몇 g 섭취하셨나요?"))
Result = (H/100)*50 + (H/100)*34 +(H/100)*77
print("총 {} 칼로리 섭취하셨습니다.".format(Result))