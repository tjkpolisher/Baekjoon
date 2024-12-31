# 11286: 절댓값 힙
# 알고리즘 분류: 자료 구조/우선순위 큐

# 1. 연산의 개수 N 입력 (1 ≤ N ≤ 100,000)
# 2. N개의 줄에 걸쳐 연산에 대한 정보를 나타내는 정수 x 입력
# [보충설명] -2^31 ≤ x ≤ 2^31
# 2-1. x가 0이 아니면 배열에 x라는 값을 추가
# 2-2. x가 0이라면 배열에서 절대값이 가장 작은 값을 출력하고 그 값을 배열에서 제거
# 2-3. 배열이 비어있는데 0을 입력받았다면 0을 출력

from heapq import heappop, heappush
import sys
input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
    integer = int(input())
    if not integer:
        if not heap:
            print(0)
        else:
            p = heappop(heap)
            print(p[1])
    else:
        heappush(heap, (abs(integer), integer))
