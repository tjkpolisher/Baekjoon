# 11279: 최대 힙
# 알고리즘 분류: 자료 구조/우선순위 큐

# 1. 연산의 개수 N 입력 (1 ≤ N ≤ 100,000)
# 2. N개의 줄에 걸쳐 자연수 x 입력
# 2-1. x가 자연수일 경우 튜플 (-x, x)를 배열에 추가 (자연수는 2^31보다 작은 값)
# 2-2. x가 0일 경우 배열에서 가장 높은 값을 1번 인덱스 원소를 출력하고 그 값을 배열에서 제거
# 2-3. 단, 힙이 비어있는 경우에는 0을 출력

import sys
from heapq import heappop, heappush

input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    x = int(input())
    if x == 0:
        if not heap:
            print(0)
        else:
            popped = heappop(heap)
            print(popped[1])
    else:
        heappush(heap, (-x, x))
