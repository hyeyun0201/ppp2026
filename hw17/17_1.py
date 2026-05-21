def str2int(text:str):
    try:
        return int(text)
    except ValueError:
        return None

def main():
    values = []
    while True:
        a = input("x ->")
        a_value = str2int(a)
        if a_value == -1:
            break
        if a_value is not None:
            if a_value > 0  and type(a_value) == int:
                values.append(a_value)
    print(f"입력된 값은 {values}입니다. 총{len(values)}개의 자연수가 입력되었고, 평균은{sum(values)/len(values)}입니다.")

if __name__ == "__main__":
    main()
