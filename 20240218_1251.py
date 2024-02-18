# 1251: 단어 나누기
# 알고리즘 분류: 구현/문자열/브루트포스 알고리즘/정렬

## 1. 단어 입력
## 2. 단어의 길이 계산
## 3. [반복문]
## 3-1. 단어를 3등분해서(길이 1 이상) 나올 수 있는 조합 찾기
## 3-2. 쪼개진 각 부분을 뒤집어서 새 단어 조합 후 리스트에 추가
## 4. 리스트 정렬
## 5. 리스트 맨 앞의 단어 출력

word = input()
length = len(word)
flipped = []

for i in range(1, length - 1):
    for j in range(1, length - i):
        p1 = word[:i]
        p2 = word[i:i + j]
        p3 = word[i + j:]
        flipped.append(p1[::-1] + p2[::-1] + p3[::-1])

flipped.sort()
print(flipped[0])
