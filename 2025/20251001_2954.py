# 2954: 창영이의 일기장
# 특이사항: 다국어(영어)(한국어 번역)
# 출처: COCI 2008/2009 Contest #3 2번
# 알고리즘 분류

# 1. 알파벳 소문자와 공백으로 이루어진 문장 입력(길이는 최대 100)
# 2-1. a, e, i, o, u 중 하나가 포착됐는지 확인
# 2-2. 포착되지 않았다면 그대로 정답 리스트에 append 후 인덱스를 1 증가시킴
# 2-3. 포착되었다면 인덱스를 3 증가시킴
# 3. 정답 리스트를 join하여 출력

sentence = input()
answer = []
vowels = {'a', 'e', 'i', 'o', 'u'}
i = 0
while i < len(sentence):
    answer.append(sentence[i])
    if sentence[i] in vowels:
        i += 3
    else:
        i += 1

print(''.join(answer))
