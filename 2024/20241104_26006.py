# 26006: K-Queen
# 출처: 2022 홍익대학교 HI-ARC 프로그래밍 경진대회 C번
# 알고리즘 분류: 구현/많은 조건 분기

# 1. 체스판의 크기 N, 흑색 퀸의 수 K 입력(3 ≤ N ≤ 10^9, 1 ≤ ㅏ)
# 2. 백색 킹의 위치 R, C 입력(1 ≤ R, C ≤ N, R행 C열에 백색 킹이 위치함)
# 3. K개의 줄에 걸쳐 흑색 퀸의 위치 R_i, C_i 입력(1 ≤ R_i, C_i ≤ N)
# [보충설명] 위치는 중복해서 주어지지 않음. 백색 킹과 8방향으로 인접한 칸에는 흑색 퀸이 놓여있지 않음.
# 4. 흑색 퀸의 위치와 백색 킹의 위치로부터 체크, 체크메이트, 스테일메이트를 판단하는 과정
# 4-1. 흑색 퀸의 위치로부터 같은 행, 열, 대각선에 위치하면 체크로 표시
# 4-2. 모든 흑색 퀸에 대하여 4-1을 반복
# 4-3. 백색 킹의 위치와 주변 위치로부터 체크, 체크메이트, 스테일메이트 판단
# 4-3-1. 백색 킹의 위치가 1이 아니고, 주변 여덟 방향 중 0이 한 곳이라도 있으면 체크
# 4-3-2. 백색 킹의 위치가 1이고, 주변 여덟 방향이 모두 1일 경우 체크메이트
# 4-3-3. 백색 킹의 위치가 0이 아니고, 주변 여덟 방향이 모두 1일 경우 스테일메이트
# 4-3-4. 셋 중 어느 것에도 해당하지 않으면 NONE
# 5. 결과 출력

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
R, C = map(int, input().split())
R -= 1
C -= 1

queens = []  # 흑색 퀸의 위치를 저장할 리스트
for _ in range(K):
    R_i, C_i = map(int, input().split())
    R_i -= 1
    C_i -= 1
    queens.append([R_i, C_i])

dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [1, 1, 1, 0, 0, -1, -1, -1]


def is_attacked_by_queen(R, C):
    for qr, qc in queens:
        # 같은 행
        if qr == R:
            return True
        # 같은 열
        if qc == C:
            return True
        # 같은 대각선상
        if abs(qr - R) == abs(qc - C):
            return True
    return False


is_check = is_attacked_by_queen(R, C)

is_escapable = False
for i in range(8):
    nx = R + dx[i]
    ny = C + dy[i]
    if 0 <= nx < N and 0 <= ny < N:
        if not is_attacked_by_queen(nx, ny):
            is_escapable = True
            break

# 최종 상태 판단
if is_check and not is_escapable:
    print("CHECKMATE")
elif is_check and is_escapable:
    print("CHECK")
elif not is_check and not is_escapable:
    print("STALEMATE")
else:
    print("NONE")
