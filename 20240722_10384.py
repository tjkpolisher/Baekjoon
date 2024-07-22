# 10384: 팬그램
# 특이사항: 다국어(영어)(한국어 번역)
# 출처: 2014 ICPC East Central North America Regional Contest PB번
# 알고리즘 분류: 구현/문자열

# 1. 테스트 케이스의 개수 n 입력
# 2. 테스트 케이스의 문장 입력
# 3. 팬그림/더블 팬그램/트리플 팬그램을 나타내는 불리언 변수 초기화(기본값: False)
# 4. 문장의 문자를 순회하면서 알파벳인지 판단
# 4-1. 알파벳이 아니면 그대로 패스
# 4-2. 알파벳일 경우 소문자로 변환한 뒤, 알파벳과 그 개수를 저장하는 딕셔너리에 카운터 1을 더함
# 5. 순회가 끝난 후 각 알파벳의 개수의 최소값에 따라 불리언 변수를 True로 변환
# 6. 불리언 변수의 값에 따라 정답 문자열 출력

import sys
input = sys.stdin.readline

n = int(input())
for i in range(1, n + 1):
    test_sentence = input().rstrip()

    is_pangram = False
    is_double = False
    is_triple = False

    test_sentence = test_sentence.lower()
    alphabets = list("abcdefghijklmnopqrstuvwxyz")
    alphabet_counter = {alphabets[i]: 0 for i in range(26)}

    for c in test_sentence:
        if c in alphabets:
            alphabet_counter[c] += 1

    counters = list(alphabet_counter.values())
    minimum_counter = min(counters)
    if minimum_counter == 3:
        is_triple = True
    elif minimum_counter == 2:
        is_double = True
    elif minimum_counter == 1:
        is_pangram = True

    if is_triple:
        print(f"Case {i}: Triple pangram!!!")
    elif is_double:
        print(f"Case {i}: Double pangram!!")
    elif is_pangram:
        print(f"Case {i}: Pangram!")
    else:
        print(f"Case {i}: Not a pangram")
