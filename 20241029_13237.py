# 13237: Binary tree
# 특이사항: 다국어(영어)
# 출처: 2016 All-Ireland Programming Olympiad (AIPO) Preliminary Round 4번
# 알고리즘 분류: 그래프 이론/그래프 탐색/트리/깊이 우선 탐색

# 1. 노드의 개수 n 입력 (1 ≤ n ≤ 20)
# 2. n개의 줄에 걸쳐 각 노드의 부모 노드를 의미하는 정수 입력 (루트 노드는 -1로 인식됨)
# [보충설명] 1번 노드가 항상 루트 노드가 되지는 않음!
# 3. n개의 노드를 순회하면서 -1이면 0을, 나머지는 노드 리스트의 값에 1을 더한 값을 저장
# 4. 저장된 높이 리스트의 높이를 하나씩 출력

n = int(input())
nodes = []
for _ in range(n):
    nodes.append(int(input()))

height = [0] * n

for i in range(n):
    # 루트 노드의 높이는 0
    if nodes[i] == -1:
        continue
    height[i] = height[nodes[i] - 1] + 1

for h in height:
    print(h)
