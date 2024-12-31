# 15686: 치킨 배달
# 출처: 삼성전자 SW 역량테스트
# 알고리즘 분류: 구현/시뮬레이션/백트래킹

# 1. 도시의 크기 N과 수익이 최대인 치킨집의 개수 M 입력 (2 ≤ N ≤ 50, 1 ≤ M ≤ 13)
# 2. N개의 줄에 걸쳐 도시의 정보 입력
# 2-1. 입력받는 동시에 집과 치킨집의 좌표 정보를 별도의 리스트에 입력
# [보충설명] 도시 정보에서 0은 빈 칸, 1은 집, 2는 치킨집. 집의 개수는 1 이상 2N 이하.
# [보충설명] 치킨집의 개수는 M 이상 13 이하.
# 3. 최대 13개 중 M개를 선택하는 조합에 따라 거리 계산.
# 4. 치킨 거리의 최소값 출력

import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
city = []  # 도시 정보를 저장할 2차원 리스트
houses = []  # 집의 좌표를 저장할 리스트
chickens = []  # 치킨집의 좌표를 저장할 리스트
for i in range(N):
    row = list(map(int, input().split()))
    for j, building in enumerate(row):
        if building == 1:  # 집
            houses.append([i, j])
        elif building == 2:  # 치킨집
            chickens.append([i, j])
    city.append(row)

candidates = list(combinations(chickens, M))


def get_sum(candidate):
    result = 0
    for hx, hy in houses:
        temp = float('inf')
        for cx, cy in candidate:
            temp = min(temp, abs(cx - hx) + abs(cy - hy))
        result += temp
    return result


result = float('inf')
for candidate in candidates:
    result = min(result, get_sum(candidate))

print(result)
