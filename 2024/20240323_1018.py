# 1018: 체스판 다시 칠하기
# 알고리즘 분류: 브루트포스 알고리즘

# 1. 행의 개수 N, 열의 개수 M 입력
# 2. N줄에 걸쳐 보드의 각 행의 상태를 입력(B는 검은색, W는 흰색)
# 3. [반복문]맨 왼쪽 위부터 시작해 8*8 크기의 체스판 영역 선택
# 3-1. 선택된 영역에 대해 맨 왼쪽이 W인 경우와 B인 경우의 패턴마다 비교
# 3-2. 해당하는 경우의 패턴과 비교하면서 순회
# 3-3. 패턴의 무늬에 맞지 않는 색이 나오면 카운터에 1 더하기
# 3-4. 모두 탐색이 끝난 후 해당 개수가 지금까지의 개수 중 가장 작으면 최소값 갱신
# 4. 최소값 출력

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(input().strip())

minimum = 8 ** 2  # 칠해야 할 칸의 최소값(초기값은 8*8 영역을 다 칠하는 경우로 설정)

patterns = ['WBWBWBWB', 'BWBWBWBW'] * 4, ['BWBWBWBW', 'WBWBWBWB'] * 4

for i in range(N - 7):
    for j in range(M - 7):
        for pattern in patterns:
            cnt = 0
            for a in range(8):
                for b in range(8):
                    if board[i + a][j + b] != pattern[a][b]:
                        cnt += 1
            minimum = min(minimum, cnt)

print(minimum)
