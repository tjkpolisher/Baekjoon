# 1927: 최소 힙
# 특이사항: 시간 제한 1초 (추가 시간 없음)
# 알고리즘 분류: 자료 구조/우선순위 큐

# 1. 연산의 개수 N 입력 (1 ≤ N ≤ 100,000)
# 2. N개의 줄에 걸쳐 연산에 대한 정보를 나타내는 정수 x 입력 (0 ≤ x < 2^31)
# 3. 입력이 종료될 때까지 아래의 연산 수행
# 3-1. 만약 x가 자연수라면 배열에 x라는 값을 추가하는 연산 수행.
# 3-2. x가 0이라면 배열에서 가장 작은 값을 출력하고 그 값을 배열에서 제거.
# 3-3. 단, 배열이 비어 있는데 가장 작은 값을 출력하라고 한 경우에는 0을 출력.

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
            print(heappop(heap))
    else:
        heappush(heap, x)
