# 1316: 그룹 단어 체커
# 알고리즘 분류: 구현/문자열

## 1. 단어의 개수 N 입력, 카운터의 개수도 N개로 초기화
## 2. [반복문]
## 2-1. 단어 입력
## 2-2. 문자마다 순회하며 문자를 set에 입력. 해당 문자가 그룹 외의 다른 곳에서 나타날 경우 카운터에서 1을 뺌
## 2-3. 그렇지 않고 모두 순회했을 경우, 그룹 문자이므로 pass
## 3. 그룹 단어의 개수 출력

N = int(input())
cnt = N

for _ in range(N):
    word = input()
    unique = set()
    for i, c in enumerate(word):
        if i == 0:
            unique.add(c)
        elif c != word[i-1] and c not in unique:
            unique.add(c)
        elif c != word[i-1] and c in unique:
            cnt -= 1
            break

print(cnt)
