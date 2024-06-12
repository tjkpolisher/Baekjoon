# 1817: 짐 챙기는 숌
# 알고리즘 분류: 구현/그리디 알고리즘

# 1. 책의 개수 N, 박스에 넣을 수 있는 최대 무게 M 입력
# 2. N이 0보다 클 경우 둘째 줄에 N권의 책의 무게 입력 후 스택으로 취급
# 3. 맨 위 원소부터 뽑으면서 박스에 넣되, M을 초과하는 순간 박스 개수에 1을 더하기
# 4. 박스의 개수 출력

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
if N == 0:
    print(0)
else:
    books = list(map(int, input().split()))
    boxes = 1
    net_weight = 0
    for _ in range(N):
        weight = books.pop()
        if net_weight + weight > M:
            boxes += 1
            net_weight = weight
        else:
            net_weight += weight

    print(boxes)
