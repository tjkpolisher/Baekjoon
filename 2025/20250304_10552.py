# 10552: DOM
# 특이사항: 다국어(영어)
# 출처: COCI 2014/2015 Contest #3 2번
# 알고리즘 분류: 그래프 이론/그래프 탐색/너비 우선 탐색/깊이 우선 탐색

# 1. 세 정수 N, M, P 입력 (1 ≤ N,M ≤ 10^5, 1 ≤ P ≤ M)
# 2. N개의 줄에 걸쳐 a_i, b_i 입력 (1 ≤ a_i, b_i ≤ M, a_i ≠ b_i)
# 3. 입력받은 정보를 바탕으로 단방향 간선 그래프 구성
# 3-1. 단, 이미 해당 채널의 노드로 가는 간선이 있으면 continue
# 4. DFS 실행
# 4-1. 노드에서 나가는 간선이 없으면 0 리턴
# 4-2. 이미 방문한 노드라면 사이클이 감지된 것이므로 -1 리턴
# 4-3. 사이클을 이루지 않으면 결과에 1을 더해서 리턴
# 4-4. 사이클을 이룬다면 그대로 리턴
# 5. 정답 출력

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N, M, P = map(int, input().split())  # 사람의 수, 채널의 수, 시작 채널 번호
graph = [-1] * M

for _ in range(N):
    a, b = map(int, input().split())
    a -= 1
    b -= 1

    if ~graph[b]:
        continue
    graph[b] = a

visited = [False] * M


def dfs(n):
    visited[n] = True

    if not ~graph[n]:
        return 0

    if visited[graph[n]]:
        return -1

    result = dfs(graph[n])
    if ~result:
        return result + 1
    return result


ans = dfs(P - 1)
print(ans)
