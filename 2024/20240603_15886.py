# 15886: 내 선물을 받아줘 2
# 출처: 선린인터넷고등학교 제2회 천하제일 코딩대회 예선 B번
# 알고리즘 분류: 그래프 이론/문자열

# 1. 골목길의 길이 N 입력 (2 ≤ N ≤ 1,000)
# 2. 길이 N짜리 구사과가 있는 곳의 지도 입력
# 3. 'EW'가 나오는 곳을 그래프의 사이클이 나오는 곳으로 판정하여 카운터에 1을 더함
# 4. 사이클의 개수를 출력(사이클에 진입하기만 하면, 사이클 상에 있는 노드를 한 번씩은 방문하기 때문)

import sys
input = sys.stdin.readline

N = int(input())
raw_map = input().rstrip()

n_cycle = 0
for i in range(N - 1):
    if raw_map[i] == 'E' and raw_map[i + 1] == 'W':
        n_cycle += 1
if n_cycle == 0:
    n_cycle = N
print(n_cycle)
