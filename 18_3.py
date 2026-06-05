import random

def chosung():
    result = ""
    quiz = ["대한민국", "넷플릭스", "바나나", "파인애플"]
    cs = ["ㄱ", "ㄲ", "ㄴ", "ㄷ", "ㄸ", "ㄹ", "ㅁ", "ㅂ", "ㅃ", "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅉ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"]
    munjae = random.choice(quiz)
    for r in munjae:
        index = (ord(r) - 44032) // 588 # 44032(가, 유니코드 시작값), 588(초성 하나 당 포함된 글자 수 21*28)
        result += cs[index]
    return result, munjae

def main():
    print("초성퀴즈게임입니다")
    result, answer = chosung()#초성과 정답을 각각 저장하게됨
    print(result)
    while True:
        a = input("정답:")
        if a ==answer:
            print("정답입니다.")
            break
        else:
            print("틀렸습니다.")


if __name__ == "__main__":
    main()