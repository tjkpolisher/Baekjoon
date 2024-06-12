# 10816: 숫자 카드 2
# 알고리즘 분류: 자료 구조/정렬/이분 탐색/해시를 사용한 집합과 맵

# 1. 숫자 카드의 개수 N(1 ≤ N ≤ 500,000) 입력
# 2. 숫자 카드에 적혀 있는 정수 입력
# 3. M 입력
# 4. 개수를 찾고자 하는 M개의 정수 입력

from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
Ms = list(map(int, input().split()))

cards.sort()
for m in Ms:
    start = bisect_left(cards, m)
    end = bisect_right(cards, m)
    print(end - start, end=' ')
