# 1986: 체스
# 특이사항: 다국어(영어)(한국어 번역)
# 출처: ICPC 2005 East Central Regional Contest D번
# 알고리즘 분류: 구현

# 1. 체스 판의 크기 n, m 입력 (1 ≤ n, m ≤ 1000)
# 2. 퀸의 개수와 그 개수만큼의 퀸의 위치 입력
# 3. 나이트의 개수와 그 개수만큼의 나이트의 위치 입력
# 4. 폰의 개수와 그 개수만큼의 폰의 위치 입력
# [보충설명] 나이트, 퀸, 폰의 개수는 각각 100 이하의 음이 아닌 정수
# 5. 각각의 퀸, 나이트가 현재 움직일 수 있는 칸을 측정해 정답에서 1씩 빼기
# [보충설명] 폰은 장애물의 역할만을 수행하므로 폰이 있는 칸은 먼저 처리
# 6. 남은 칸(즉, 안전한 칸)의 개수 출력

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
n_queen, *queens = map(int, input().split())
n_knight, *knights = map(int, input().split())
n_pawn, *pawns = map(int, input().split())

# 현재 이동 가능한 칸의 수
cnt = n * m - n_queen - n_knight - n_pawn

# 체스판 초기화
board = [[0 for _ in range(m)] for _ in range(n)]
# 폰, 퀸, 나이트가 있는 칸은 별도로 장애물 표시
for i in range(n_pawn):
    x, y = pawns[2 * i] - 1, pawns[2 * i + 1] - 1
    board[x][y] = "P"
for i in range(n_queen):
    x, y = queens[2 * i] - 1, queens[2 * i + 1] - 1
    board[x][y] = "Q"
for i in range(n_knight):
    x, y = knights[2 * i] - 1, knights[2 * i + 1] - 1
    board[x][y] = "K"

# 퀸이 이동 가능한 칸
q_xd = [0, -1, -1, -1, 0, 1, 1, 1]
q_yd = [-1, -1, 0, 1, 1, 1, 0, -1]
for i in range(n_queen):
    x, y = queens[2 * i] - 1, queens[2 * i + 1] - 1
    for j in range(8):
        nx, ny = x + q_xd[j], y + q_yd[j]
        while 0 <= nx < n and 0 <= ny < m and board[nx][ny] in (0, 1):
            if board[nx][ny] == 0:
                board[nx][ny] = 1
                cnt -= 1
            nx += q_xd[j]
            ny += q_yd[j]

# 나이트가 이동 가능한 칸
k_xd = [-1, -2, -2, -1, 1, 2, 2, 1]
k_yd = [-2, -1, 1, 2, 2, 1, -1, -2]
for i in range(n_knight):
    x, y = knights[2 * i] - 1, knights[2 * i + 1] - 1
    for j in range(8):
        nx, ny = x + k_xd[j], y + k_yd[j]
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] in (0, 1):
            if board[nx][ny] == 0:
                board[nx][ny] = 1
                cnt -= 1

print(cnt)
