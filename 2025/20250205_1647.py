# 1647: 도시 분할 계획
# 알고리즘 분류: 그래프 이론/최소 스패닝 트리

# 1. 집의 개수 N, 길의 개수 M 입력 (2 ≤ N ≤ 100,000, 1 ≤ M ≤ 1,000,000)
# 2. M줄에 걸쳐 출발점 A, 도착점 B, 그 길의 유지비 C 입력
# [보충설명] 길은 어느 방향으로든 다닐 수 있으므로 방향성이 없음
# 3. 입력받은 간선 정보를 유지비에 대해 오름차순으로 정렬
# 4. 주어진 그래프에서 2개의 최소 신장 트리를 만들도록 크루스칼 알고리즘 실행
# 5. 최종 비용에서 최대 간선 비용을 뺀 값을 출력

import sys
input = sys.stdin.readline

N, M = map(int, input().split())


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


edges = []
result = 0

parent = [0] * (N + 1)
for i in range(1, N + 1):
    parent[i] = i

for _ in range(M):
    A, B, C = map(int, input().split())
    edges.append((C, A, B))

edges.sort()
maximum_cost = 0

for edge in edges:
    C, A, B = edge
    if find_parent(parent, A) != find_parent(parent, B):
        union_parent(parent, A, B)
        result += C
        maximum_cost = C

print(result - maximum_cost)
