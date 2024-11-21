# 32372: 마법의 나침반
# 출처: 인천대학교 INU 코드페스티벌 2024 D번
# 알고리즘 분류: 구현

# 1. 지도의 한 변의 크기 N, 나침반 사용 기록의 개수 M 입력 (2 ≤ N ≤ 10, 1 ≤ M ≤ N^2)
# 2. N × N 크기의 지도의 각 좌표를 담은 집합 생성
# 3. M개의 줄에 걸쳐 i번째 나침반을 사용한 좌표 X_i, Y_i, 보물의 방향 K_i 입력
# [보충설명] 1 ≤ X_i,Y_i ≤ N, 1 ≤ K_i ≤ 8, 세 변수는 모두 정수로 주어짐
# 4. 나침반 방향을 바탕으로, 보물이 없는 좌표를 집합에서 삭제
# 5. 길이가 1이 되거나 모든 나침반 사용 기록을 조회했을 경우, 집합에 남은 원소를 한 줄에 출력

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
coordinates = set()
for i in range(1, N + 1):  # x좌표
    for j in range(1, N + 1):  # y좌표
        coordinates.add((i, j))

for _ in range(M):
    X, Y, K = map(int, input().split())
    if len(coordinates) == 1:
        continue

    if K == 1:
        # 방향 1: x좌표가 작고, y좌표가 같은 곳
        coordinates = {(x, y) for (x, y) in coordinates if x < X and y == Y}
    elif K == 2:
        # 방향 2: x좌표가 작고, y좌표가 큰 곳
        coordinates = {(x, y) for (x, y) in coordinates if x < X and y > Y}
    elif K == 3:
        # 방향 3: x좌표가 같고, y좌표가 큰 곳
        coordinates = {(x, y) for (x, y) in coordinates if x == X and y > Y}
    elif K == 4:
        # 방향 4: x좌표가 크고, y좌표가 큰 곳
        coordinates = {(x, y) for (x, y) in coordinates if x > X and y > Y}
    elif K == 5:
        # 방향 5: x좌표가 크고, y좌표가 같은 곳
        coordinates = {(x, y) for (x, y) in coordinates if x > X and y == Y}
    elif K == 6:
        # 방향 6: x좌표가 크고, y좌표가 작은 곳
        coordinates = {(x, y) for (x, y) in coordinates if x > X and y < Y}
    elif K == 7:
        # 방향 7: x좌표가 같고, y좌표가 작은 곳
        coordinates = {(x, y) for (x, y) in coordinates if x == X and y < Y}
    elif K == 8:
        # 방향 8: x좌표가 작고, y좌표가 작은 곳
        coordinates = {(x, y) for (x, y) in coordinates if x < X and y < Y}

x, y = list(coordinates)[0]
print(x, y)
