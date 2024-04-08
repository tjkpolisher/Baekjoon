# 1446: 지름길
# 알고리즘 분류: 다이나믹 프로그래밍/그래프 이론/데이크스트라/최단 경로

# 1. 지름길의 개수 N, 고속도로 길이 D 입력
# 2. N개의 줄에 걸쳐 시작 위치, 도착 위치, 지름길 길이 입력
# 3. 시작 위치도, 도착 위치도 지정되지 않았던 모든 나머지 수를 개별적인 노드로 가정
# 4. 개별적인 노드들의 거리를 1이라고 가정하여 그래프에 입력
# 5. 다익스트라 알고리즘 적용
# 6. 최단 거리 리스트의 D번째 원소 출력

import heapq
import sys
input = sys.stdin.readline
INF = 10 ** 9

N, D = map(int, input().split())
graph = [[] for _ in range(D + 1)]

# 지름길 정보 입력
for _ in range(N):
    a, b, c = map(int, input().split())
    if b > D:  # 역주행이 불가능하므로 도착점이 D보다 크면 제외
        continue
    graph[a].append((b, c))  # 모든 지름길은 일방통행이므로 단방향 간선

# 거리를 무한대로 초기화
distance = [INF] * (D + 1)
# 지름길이 없는 노드들은 전부 거리 1로 초기화
for i in range(D):
    graph[i].append((i + 1, 1))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0  # 시작점 거리를 0으로 초기화
    while q:
        d, now = heapq.heappop(q)
        if distance[now] < d:
            continue
        for i in graph[now]:
            d_temp = d + i[1]
            if d_temp < distance[i[0]]:
                distance[i[0]] = d_temp
                heapq.heappush(q, (d_temp, i[0]))


# 시작점 거리가 0이므로 0에서 출발하는 걸로 설정
dijkstra(0)
print(distance[D])
