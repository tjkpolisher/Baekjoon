# 12869: 뮤탈리스크
# 알고리즘 분류: 다이나믹 프로그래밍/그래프 이론/그래프 탐색/너비 우선 탐색

# 1. SCV의 수 N 입력 (1 ≤ N ≤ 3)
# 2. 각 SCV의 체력을 뜻하는 N개의 정수 입력 (체력은 60 이하의 자연수)
# 2-1. 체력을 리스트에 저장하고, 원소가 3개가 되도록 나머지 원소를 0으로 채우기
# 3. 1에서 60까지의 체력을 지났는지에 여부를 3차원 리스트에 저장
# 4. 뮤탈리스트가 가할 수 있는 데미지 순서의 경우의 수를 순열로 만들기
# 5. 큐에 체력 리스트와 0을 넣고 BFS 시작
# 5-1. [종료 조건] 모든 SCV의 체력이 0이 되면 현재까지의 공격 횟수를 출력 후 종료
# 5-2. 데미지 순열을 하나씩 선택하면서 체력을 변경
# 5-3. 이때 방문하지 않은 방문 리스트에는 방문 체크 후 새 체력 리스트를 큐에 저장

from collections import deque
from itertools import permutations

N = int(input())
hp = list(map(int, input().split()))

hp = hp + [0] * (3 - N)
visited = [[[0 for i in range(61)] for j in range(61)] for k in range(61)]
perms = list(permutations([9, 3, 1], 3))

q = deque([[hp, 0]])
while q:
    hp, cnt = q.popleft()
    if hp == [0, 0, 0]:
        print(cnt)
        break
    for p in perms:
        new_hp = [max(hp[i] - p[i], 0) for i in range(3)]
        if not visited[new_hp[0]][new_hp[1]][new_hp[2]]:
            visited[new_hp[0]][new_hp[1]][new_hp[2]] = 1
            q.append([new_hp, cnt + 1])
