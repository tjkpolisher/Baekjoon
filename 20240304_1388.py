# 1388: 바닥 장식
# 알고리즘 분류: 구현/그래프 이론/그래프 탐색/깊이 우선 탐색

# 1. 방 바닥의 세로, 가로 크기 N, M 입력
# 2. N개의 줄에 M개의 바닥 장식 문자열 입력
# 3. [반복문] DFS

N, M = map(int, input().split())
floor = []

for _ in range(N):
    floor.append(list(input()))


def dfs(graph, x, y):
    if graph[x][y] == '-':
        graph[x][y] = 0
        for _y in [1, -1]:
            Y = y + _y
            if (Y > 0 and Y < M) and graph[x][Y] == '-':
                dfs(graph, x, Y)
    elif graph[x][y] == '|':
        graph[x][y] = 0
        for _x in [1, -1]:
            X = x + _x
            if (X > 0 and X < N) and graph[X][y] == '|':
                dfs(graph, X, y)


ans = 0
for i in range(N):
    for j in range(M):
        if floor[i][j] == '-' or floor[i][j] == '|':
            dfs(floor, i, j)
            ans += 1

print(ans)
