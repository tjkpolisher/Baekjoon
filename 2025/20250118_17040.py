# 17040: The Great Revegatation (Bronze)
# 특이사항: 다국어(영어)
# 출처: USACo 2019 February Contest Bronze 2번
# 알고리즘 분류: 그래프 이론/그리디 알고리즘

# 1. 목초지의 수 N, 데리고 온 소의 마릿수 M 입력 (2 ≤ N ≤ 100, 1 ≤ M ≤ 150)
# 2. M개의 줄에 걸쳐 1에서 N 사이의 있는 두 정수를 입력 (i번째 소가 가장 선호하는 두 개의 목초지의 번호)
# 3. 입력받은 정수들을 바탕으로 그래프의 연결 정보를 저장
# 4. 인접한 목초지에서 사용된 풀 번호 확인 (사용되는 풀은 1, 2, 3, 4번의 총 네 가지)
# 5. 1번부터 4번 풀 중 사용되지 않은 풀 선택
# 6. 선택된 풀을 결과 리스트에 저장
# 7. 결과 리스트의 1번 인덱스부터 마지막 인덱스까지 join하여 출력

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
connections = [tuple(map(int, input().split())) for _ in range(M)]
graph = [[] for _ in range(N + 1)]
for a, b in connections:
    graph[a].append(b)
    graph[b].append(a)

result = [0] * (N + 1)
for pasture in range(1, N + 1):
    visited = {result[neighbor] for neighbor in graph[pasture]}

    for grass in range(1, 5):
        if grass not in visited:
            result[pasture] = grass
            break

print(''.join(map(str, result[1:])))
