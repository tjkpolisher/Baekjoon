# 18405: 경쟁적 전염
# 알고리즘 분류: 구현/그래프 이론/그래프 탐색/너비 우선 탐색

# 1. 시험관의 크기 N, 바이러스의 종류 K 입력 (1 ≤ N ≤ 200, 1 ≤ K ≤ 1,000)
# 2. N개의 줄에 걸쳐 시험관의 바이러스 번호 입력
# [보충설명] 각 행은 N개의 원소로 구성, 바이러스가 존재하지 않는 경우는 0이 주어짐. 바이러스의 번호는 K 이하의 자연수.
# 3. S, X, Y 입력 (0 ≤ S ≤ 10,000, 1 ≤ X, Y ≤ N)
# [보충설명] S초가 지난 후 좌표 X,Y에 존재하는 바이러스의 종류를 출력하는 것이 목적
# 4. BFS를 실행하여 n초 후까지의 바이러스 증식 상황을 계산
# [보충설명] 매 초마다 번호가 낮은 종류의 바이러스부터 먼저 증식. 특정 칸에 바이러스가 이미 존재하면, 그곳에는 다른 바이러스가 들어갈 수 없음.
# 4-0. 현재 시각이 S와 같으면 BFS 종료
# 4-1. 상하좌우 네 방향에 대하여 해당 칸에 바이러스가 없으면 현재 바이러스 번호로 해당 칸을 변경
# 4-2. 현재 시각에서의 모든 큐의 원소에 대하여 연산을 실행한 후에 시간을 1초 증가
# 5. S초가 지나거나 큐가 비면 BFS 종료 후 [X-1][Y-1] 인덱스의 원소 출력

from collections import deque

N, K = map(int, input().split())
cylinder = []
virus_location = []
for i in range(N):
    row = list(map(int, input().split()))
    for j, v in enumerate(row):
        if v:
            virus_location.append((v, i, j))
    cylinder.append(row)

virus_location.sort()  # 바이러스 번호의 오름차순으로 정렬

S, X, Y = map(int, input().split())
# 인덱싱 효율을 위해 X, Y에서 1씩 빼기
X -= 1
Y -= 1


def bfs(arr, S):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    sec = 0
    q = deque(arr)
    while q:
        if sec == S:
            break
        for _ in range(len(q)):
            v, x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue
                if cylinder[nx][ny] == 0:
                    cylinder[nx][ny] = v
                    q.append((v, nx, ny))
        sec += 1


bfs(virus_location, S)
print(cylinder[X][Y])
