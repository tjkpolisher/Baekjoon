# 1697: 숨바꼭질
# 출처: USA Computing Olympiad (USACO) US Open 2007 Silver 2번
# 알고리즘 분류: 그래프 이론/그래프 탐색/너비 우선 탐색

# 1. 수빈이의 위치 N과 동생이 있는 위치 K 입력 (N, K는 모두 정수, 0 ≤ N, K ≤ 100,000)
# 2. 0부터 100,000까지의 수를 저장한 노드로 구성된 그래프 구성
# 2-1. N, K의 범위를 만족해야 함.
# 2-2. 위치가 X일 때 X - 1, X + 1, 2 * X로 이동 가능.
# 3. N을 큐에 삽입한 후, BFS를 실행해 K까지 가장 빠르게 도달하는 경우의 수 탐색
# 4. 해당 경우의 수가 만들어내는 가장 빠른 시간을 출력

from collections import deque
import sys
input = sys.stdin.readline


def bfs(start, end, visited):
    q = deque()
    q.append(start)
    while q:
        v = q.popleft()
        if v == end:
            return visited[end]

        for i in (v + 1, v - 1, v * 2):
            if 0 <= i <= 100000 and not visited[i]:
                visited[i] = visited[v] + 1
                q.append(i)


N, K = map(int, input().split())
visited = [0] * 100001

print(bfs(N, K, visited))
