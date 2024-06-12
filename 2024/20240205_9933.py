# 9933: 민균이의 비밀번호
# 특이사항: 다국어(영어)(한국어 번역), 답이 유일한 경우만 입력으로 주어짐

## 1. 단어의 개수 N 입력
## 2. [반복문]
## 2-1. 단어 입력
## 2-2. 입력한 단어를 리스트에 저장
## 3. 모든 단어를 변환 후 동일한 set가 존재할 경우 해당 단어가 정답
## 4. 해당 단어의 길이 및 가운데 글자 출력

N = int(input())
words = []

for _ in range(N):
    word = input()
    words.append(word)

for word in words:
    if word[::-1] in words:
        print(len(word), word[len(word) // 2])
        break
    elif word[::-1] == word:
        print(len(word), word[len(word) // 2])
        break