# 16928: 뱀과 사다리 게임
# 알고리즘 분류: 그래프 이론/그래프 탐색/너비 우선 탐색

# 1. 게임판에 있는 사다리의 수 N (1 ≤ N ≤ 15), 뱀의 수 M (1 ≤ M ≤ 15) 입력
# 1-1. 그래프 생성
# 2. N개의 줄에 걸쳐 사다리의 정보를 의미하는 x, y 입력 (x < y)
# 2-1. 입력받은 x, y를 바탕으로 그래프에 해당 정보 추가
# 3. 다음 M개의 줄에 걸쳐 뱀의 정보를 의미하는 u, v 입력 (u > v)
# 3-1. 입력받은 u, v를 바탕으로 그래프에 해당 정보 추가
# [보충설명] 1번 칸과 100번 칸은 뱀과 사다리의 시작 또는 끝이 아님. 모든 칸은 최대 하나의 사다리 또는 뱀을 가지면 동시에 두 가지를 가질 수 없음.
# 4. 1번 칸부터 BFS를 실행하여 최소 이동 횟수를 기록
# 5. 최소 이동 횟수 출력

from collections import deque

N, M = map(int, input().split())
graph = [i for i in range(101)]

# 사다리의 정보를 그래프에 추가
for _ in range(N):
    x, y = map(int, input().split())
    graph[x] = y
# 뱀의 정보를 그래프에 추가
for _ in range(M):
    u, v = map(int, input().split())
    graph[u] = v


def bfs(start):
    q = deque()
    q.append(start)
    dist = [-1] * 101
    dist[1] = 0

    while q:
        v = q.popleft()
        if v == 100:
            return dist[100]
        for dice in range(1, 7):
            next_v = v + dice
            if next_v > 100:
                continue  # 결과가 100을 넘으면 다음 위치로 스킵

            final_v = graph[next_v]
            if dist[final_v] == -1:
                dist[final_v] = dist[v] + 1
                q.append(final_v)
    return -1  # 100번 칸에 도달할 수 없으면 -1을 리턴


print(bfs(1))
