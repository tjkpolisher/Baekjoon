import sys
# 27160: 할리갈리
## 1. 카드 개수 N 입력
## 2. 과일 종류별 카드 숫자 합산을 담을 딕셔너리 생성
## 3. 카드 N개에 있는 숫자를 딕셔너리 값에 추가
## 4. 정확히 5가 있는 경우 "YES", 그 외에는 "NO" 출력

input = sys.stdin.readline

N = int(input())
table = {"STRAWBERRY":0, "BANANA":0,
         "LIME":0, "PLUM":0}
for _ in range(N):
    S, X = input().split()
    X = int(X)
    table[S] += X
values = table.values()
if 5 in values:
    print("YES")
else:
    print("NO")