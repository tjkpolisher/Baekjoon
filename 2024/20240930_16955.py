# 16955: 오목, 이길 수 있을까?
# 알고리즘 분류: 구현/브루트포스 알고리즘

# 1. 10개 줄에 걸쳐 바둑판의 상태 입력
# [보충설명] '.'는 빈 칸, 'x'는 구사과의 돌, 'o'는 큐브러버의 돌
# 2. 0행 0열 인덱스부터 시작해 x의 위치를 탐색
# 3. 우측, 상측, 우하대각선, 우상대각선 벡터 정의
# 4. 모든 칸을 순회하면서 빈 칸일 경우 'X'로 바꿔가면서 이길 수 있는지 확인
# 4-1. 'X'에 해당하는 칸에서 네 방향 모두에 대해 검사
# 4-2. 이전 셀이 'X'인지부터 확인 후, 카운터 개수 집계
# 4-3. 5개 이상이 발견되면 True를 반환하고, 그렇지 않고 반복문이 종료되면 False 반환
# 5-1. 칸을 순회하는 중 True가 반환되면 1을 출력
# 5-2. 그렇지 않고 반복문이 종료되면 0을 출력

board = []
for _ in range(10):
    board.append(list(input()))

# 방향 벡터 정의 (우, 하, 우하대각선, 우상대각선)
directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]


def check_win(board):
    for i in range(10):
        for j in range(10):
            if board[i][j] == 'X':
                # 네 가지 방향에 대해 확인
                for dx, dy in directions:
                    cnt = 1
                    x, y = i, j
                    # 이전 위치가 보드 범위를 벗어나지 않고, 'X'라면 continue
                    prev_x, prev_y = x - dx, y - dy
                    if 0 <= prev_x < 10 and 0 <= prev_y < 10 and board[prev_x][prev_y] == 'X':
                        continue
                    x += dx
                    y += dy
                    while 0 <= x < 10 and 0 <= y < 10 and board[x][y] == 'X':
                        cnt += 1
                        x += dx
                        y += dy
                    if cnt >= 5:
                        return True
    return False


for i in range(10):
    for j in range(10):
        if board[i][j] == '.':
            board[i][j] = 'X'
            if check_win(board):
                print(1)
                exit()
            board[i][j] = '.'

print(0)
