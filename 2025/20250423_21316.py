# 21316: 스피카
# 출처: 인하대학교 2021 IGRUS Newbie Programming Contest E번
# 알고리즘 분류: 그래프 이론/애드 혹

# 1. 12개의 줄에 걸쳐 서로 다른 두 개의 정수 x, y 입력
# [보충설명] x, y는 x와 y를 잇는 선분을 의미.
# 2. 입력받은 두 정수를 2차원 리스트에 양방향 그래프로 구성
# 3. 그래프를 순회하면서 다음 조건을 만족하는 번호를 탐색
# 3-1. 해당 별과 연결된 별의 개수가 3개
# 3-2. 연결된 별은 각각 연결된 변의 수가 1개/3개/2개여야 함.(순서 무관)
# 4. 조건을 만족하는 별의 번호를 출력

import sys
input = sys.stdin.readline

graph = [[] for _ in range(13)]
for _ in range(12):
    x, y = map(int, input().split())
    # 양방향 그래프로 구성
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, 13):
    if len(graph[i]) != 3:
        continue
    adjacent_line = set(range(1, 4))
    for j in graph[i]:
        if len(graph[j]) not in adjacent_line:
            break
        else:
            adjacent_line.remove(len(graph[j]))
    if not adjacent_line:
        print(i)
        exit()
