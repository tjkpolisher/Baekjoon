# 19947: 투자의 귀재 배주형
# 출처: 인하대학교 2020 IGRUS Newbie Programming Contest D번
# 알고리즘 분류: 다이나믹 프로그래밍/브루트포스 알고리즘

# 1. 초기 비용 H, 투자 기간 Y 입력 (10,000 ≤ H ≤ 100,000, 0 ≤ Y ≤ 10)
# 2. 최대 수익을 전역 변수로 설정
# 3. 재귀 함수를 통해 최대 수익 계산
# 3-1. 1년 투자는 5%, 3년 투자는 20%, 5년 투자는 35% 이율.
# 3-2. 투자 방식은 매녈 바꿀 수 있지만, 기한을 다 채운 시점에만 이율이 반영되고 그 사이에는 돈이 늘어나지 않음
# 4. 최대 수익 출력

import sys
from math import trunc
sys.setrecursionlimit(10**6)

H, Y = map(int, sys.stdin.readline().split())
max_profit = 0


def profit(h, y):
    global max_profit
    if y == 0:  # 종료 조건
        max_profit = max(max_profit, h)
        return max_profit
    if y >= 5:
        profit(trunc(h * 1.35), y - 5)
    if y >= 3:
        profit(trunc(h * 1.2), y - 3)
    if y >= 1:
        profit(trunc(h * 1.05), y - 1)

    return max_profit


max_profit = profit(H, Y)
print(max_profit)
