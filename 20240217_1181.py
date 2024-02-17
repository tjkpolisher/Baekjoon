# 1181: 단어 정렬
# 알고리즘 분류: 문자열/정렬

## 1. 단어의 개수 N 입력
## 2. [반복문]
## 2-1. 단어 입력
## 2-2. 단어의 길이에 해당하는 배열이 없으면 새로 생성 후 add, 있으면 그냥 add
## 3. 각 리스트를 사전 순으로 정렬
## 4. 길이가 짧은 리스트부터 단어 출력

N = int(input())
length_word = {}

for _ in range(N):
    word = input()
    if len(word) not in length_word:
        length_word[len(word)] = {word}
    else:
        length_word[len(word)].add(word)

for k in sorted(length_word.keys()):
    words = list(length_word[k])
    words.sort()
    for w in words:
        print(w, end='\n')
