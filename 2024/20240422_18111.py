# 18111: 마인크래프트
# 알고리즘 분류: 구현/브루트포스 알고리즘

# 1. 세로 N, 가로 M, 초기 블록 개수 B 입력 (1 ≤ M, N ≤ 500, 0 ≤ B ≤ 6.4 × 10^7)
# 2. N개의 줄에 걸쳐 각각 M개의 정수로 땅의 높이 입력
# 3. 가장 위에 있는 블록을 제거해 인벤토리에 넣기(2초 소모)
# 4. 인벤토리에서 블록을 꺼내 현재 높이가 가장 낮은 위치에 놓기(1초 소모)
# 5. 최소 시간과 땅의 높이 출력(답이 여러 개라면 땅의 높이가 가장 높은 것 출력)

import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
heights = []
for _ in range(N):
    h = list(map(int, input().split()))
    heights.append(h)

ans = int(1e9)
ground_level = 0

for i in range(257):
    used_block = 0  # 블럭 회수 분
    taken_block = 0  # 블럭 사용 분
    for x in range(N):
        for y in range(M):
            if heights[x][y] > i:
                used_block += heights[x][y] - i
            else:
                taken_block += i - heights[x][y]

    if used_block + B >= taken_block:
        if (used_block * 2) + taken_block <= ans:
            ans = (used_block * 2) + taken_block
            ground_level = i

print(ans, ground_level)
