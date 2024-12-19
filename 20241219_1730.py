# 1730: 판화
# 특이사항: 다국어(영어)(한국어 번역)
# 출처: 2007 Croatian Highschool Competitions in Informatics Regional Competition - Juniors 2번
# 알고리즘 분류: 구현/시뮬레이션

# 1. 목판의 크기 N 입력 (2 ≤ N ≤ 10)
# 2. 로봇팔의 움직임을 입력받아 리스트로 변환 (움직임은 최대 250개)
# 3. N행 N열을 뜻하는 2차원 리스트를 생성
# 4. 0행 0열을 시작으로 로봇팔 리스트를 순회하면서 움직임을 기로
# 4-1. 수직으로만 지났을 경우 '|'로 변경
# 4-2. 수평으로만 지났을 경우 '-'로 변경
# 4-3. '|' 또는 '-'로 지난 상태에서 다른 방향으로의 움직임이 있으면 '+'로 변경
# 5. 해당 칸의 원소를 움직임에 맞게 변경한 후, 새 방향으로 진행
# 6. 모든 움직임이 끝난 후 목판의 상태를 출력

N = int(input())
moves = list(input())

board = [['.'] * N for _ in range(N)]
dx = [-1, 1, 0, 0]  # U, D, L, R 순서
dy = [0, 0, -1, 1]
x, y = 0, 0  # 초기 위치


def carve(x, y, move):
    if board[x][y] == '.':
        if move in ('L', 'R'):
            board[x][y] = '-'
        if move in ('U', 'D'):
            board[x][y] = '|'
    if board[x][y] == '|':
        if move in ('L', 'R'):
            board[x][y] = '+'
    if board[x][y] == '-':
        if move in ('U', 'D'):
            board[x][y] = '+'


for move in moves:
    if move == 'U':
        nx = x + dx[0]
        ny = y + dy[0]
    if move == 'D':
        nx = x + dx[1]
        ny = y + dy[1]
    if move == 'L':
        nx = x + dx[2]
        ny = y + dy[2]
    if move == 'R':
        nx = x + dx[3]
        ny = y + dy[3]

    # 목판 바깥으로 나가는 명령일 경우 무시하고 다음 명령 진행
    if nx < 0 or nx >= N or ny < 0 or ny >= N:
        continue
    carve(x, y, move)
    carve(nx, ny, move)
    x, y = nx, ny

for row in board:
    print(''.join(row))
