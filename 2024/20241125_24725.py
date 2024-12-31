# 24725: 엠비티아이
# 특이사항: 다국어(영어)
# 출처: 2022 연세대학교 신학기맞이 프로그래밍 경진대회 C번
# 알고리즘 분류: 구현/문자열/브루트포스 알고리즘

# 1. 행의 개수와 열의 개수를 뜻하는 두 정수 N, M 입력 (1 ≤ N, M ≤ 200)
# 2. N개의 줄에 걸쳐 M개의 알파벳 대문자로 구성된 문자열 입력
# 3. 4개의 문자로 구성된 문자열을 추출(가로, 세로, 대각선)
# 4. 추출된 문자열 또는 문자열을 뒤집은 문자열이 16개의 MBTI 조합에 포함되어 있을 경우 카운터에 1을 더함
# 5. 카운터 출력

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(input().rstrip())

# 16개의 MBTI 조합
mbti = {'ENFP', 'ENFJ', 'ENTP', 'ENTJ',
        'ESFP', 'ESFJ', 'ESTP', 'ESTJ',
        'INFP', 'INFJ', 'INTP', 'INTJ',
        'ISFP', 'ISFJ', 'ISTP', 'ISTJ'}

cnt = 0
for i in range(N):
    for j in range(M):
        # 가로
        if j + 3 < M:
            string = board[i][j:j + 4]
            if string in mbti or string[::-1] in mbti:
                cnt += 1
        # 세로
        if i + 3 < N:
            string = board[i][j] + board[i + 1][j] + board[i + 2][j] + board[i + 3][j]
            if string in mbti or string[::-1] in mbti:
                cnt += 1
        # 대각선
        if i + 3 < N and j + 3 < M:
            string = board[i][j] + board[i + 1][j + 1] + board[i + 2][j + 2] + board[i + 3][j + 3]
            if string in mbti or string[::-1] in mbti:
                cnt += 1
        if i + 3 < N and j - 3 >= 0:
            string = board[i][j] + board[i + 1][j - 1] + board[i + 2][j - 2] + board[i + 3][j - 3]
            if string in mbti or string[::-1] in mbti:
                cnt += 1
print(cnt)
