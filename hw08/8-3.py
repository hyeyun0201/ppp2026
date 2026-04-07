def c2f(temp_c):
    result = temp_c*1.8+32
    return result
def main():
    A = float(input("섭씨를 입력하시오 :"))
    C = c2f(A)
    print(f"{C}℉입니다.")
if __name__ =="__main__":
    main()
