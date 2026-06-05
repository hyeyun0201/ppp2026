def toggle_ch(alphabet):
    if ord(alphabet) >= 65 and ord(alphabet) <= 90: #대문자
        return chr(ord(alphabet) + 32)
    elif ord(alphabet) >= 97 and ord(alphabet) <= 122: #소문자
        return chr(ord(alphabet) - 32)
    return alphabet

def toggle_text(text):
    result = ""
    for c in text:
        result += toggle_ch(c) #텍스트를 넣으면 뒤에 누적으로 붙여짐
    return result


def main():
    ment = input("대소문자 변환 :")
    print(toggle_text(f"{ment}"))
if __name__ == "__main__":
    main()