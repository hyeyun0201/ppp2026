def caesar_encode(text: str, shift: int = 3): #문자->아스키코드
    result = ""
    for i in text:
        if 'a'<=i<='z':
            result += (chr((ord(i) + shift - 97) %26+97))
        else:
            result += (chr((ord(i) + shift -65) %26+65))
    return result

def str_caesar_decode(text: str, shift: int = 3): #DEF->ABC
    result = ""
    for i in text:
        if 'a'<=i<='z':
            result += (chr((ord(i) - shift - 97) %26+97))
        else:
            result += (chr((ord(i) - shift -65) %26+65))
    return result


def main():
    text = input("알파벳 3개를 입력하시오(ABC->DEF):")
    text_2 = input("알파벳 3개를 입력하시오(DEF->ABC):")
    print(caesar_encode(text, 3))
    print(str_caesar_decode(text_2,3))
if __name__ == "__main__":
    main()
