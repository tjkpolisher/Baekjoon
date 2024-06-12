# 10815: 숫자 카드
# 알고리즘 분류: 자료구조/정렬/이분 탐색/해시를 사용한 집합과 맵

## 1. 상근이가 가진 숫자 카드 개수 N 입력
## 2. 숫자 카드에 적혀 있는 정수 N개를 큐에 입력(중복은 없음)
## 3. 카드 중에서 찾고자 하는 정수의 개수 M 입력
## 4. 정수 M개를 딕셔너리의 키로 입력(각 키의 값은 0으로 초기화)
## 5. [반복문]
## 5-1. 숫자 카드를 큐 순서대로 뽑으면서 키로 선택
## 5-2-1. 키가 있을 경우 해당 키의 값을 1로 변경
## 5-2-2. 없을 경우 pass
## 6. 값 출력

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
cards = deque(map(int, input().split()))
M = int(input())
integers = {m: 0 for m in map(int, input().split())}

while cards:
    card = cards.popleft()
    if card in integers:
        integers[card] = 1

values = integers.values()
for v in values:
    print(v, end=' ')
