# 3190: 뱀
# 특이사항: 다국어(영어)(한국어 번역)
# 출처: Croatian Highschool Competitions in Informatics 2005 Juniors 2번
# 알고리즘 분류: 구현/자료 구조/시뮬레이션/덱/큐

# 1. 보드의 크기 N 입력 (2 ≤ N ≤ 100)
# 2. 사과의 개수 K 입력 (0 ≤ K ≤ 100)
# 3. N x N 보드를 표현하는 2차원 리스트의 모든 원소를 0으로 초기화
# 4. K개의 줄에 걸쳐 사과의 위치(행, 열)를 입력받아 보드에 1로 표시
# 5. 뱀의 방향 변환 횟수 L 입력 (1 ≤ L ≤ 100)
# 6. L개의 줄에 걸쳐 뱀의 방향 변환 정보 X와 C 입력 (X는 10,000 이하의 양의 정수)
# [보충설명] 게임 시작 후 X초 뒤에 왼쪽(C가 'L') 또는 오른쪽(C가 'D')으로 90도 회전
# 7. 보드 맨 위 맨 좌측, 즉 1행 1열(인덱스: [0][0])을 뱀을 뜻하는 -1로 변환
# [보충설명] 1행 1열에는 사과가 존재하지 않음. 초기 방향은 오른쪽.
# 8. 문제의 규칙에 따라 시뮬레이션 진행
# 9. 게임이 끝나는 시간 출력

N = int(input())
K = int(input())
board = [[0] * N for _ in range(N)]  # 게임이 진행되는 보드
for _ in range(K):
    r, c = map(int, input().split())
    board[r - 1][c - 1] = 1

L = int(input())
snake_movements = []
for _ in range(L):
    X, C = input().split()
    X = int(X)
    snake_movements.append((X, C))


def turn(direction, C):
    if C == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction


cnt = 0  # 게임 진행 시간
x, y = 0, 0   # 뱀의 첫 위치

# 방향 정보: 초기조건은 오른쪽을 보고 있음(리스트 상에는 시계 방향으로 돌아가며 배치)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

board[x][y] = -1
direction = 0  # 초기 방향
idx = 0  # 다음에 회전할 정보
snake_current = [(x, y)]

while True:
    nx = x + dx[direction]
    ny = y + dy[direction]

    if 0 <= nx < N and 0 <= ny < N and board[nx][ny] != -1:
        # 사과가 없을 경우 - 이동 후, 꼬리 제거
        if board[nx][ny] == 0:
            board[nx][ny] = -1
            snake_current.append((nx, ny))
            tx, ty = snake_current.pop(0)
            board[tx][ty] = 0
        # 사과가 있을 경우 - 이동 후 꼬리 그대로 두기
        if board[nx][ny] == 1:
            board[nx][ny] = -1
            snake_current.append((nx, ny))
    # 벽이나 뱀의 몸통과 부딪힐 경우
    else:
        cnt += 1
        break

    x, y = nx, ny  # 위치 갱신
    cnt += 1
    # 회전할 시간이 되면 회전
    if idx < L and cnt == snake_movements[idx][0]:
        direction = turn(direction, snake_movements[idx][1])
        idx += 1

print(cnt)
