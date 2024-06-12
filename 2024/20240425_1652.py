# 1652: 누울 자리를 찾아라
# 알고리즘 분류: 구현/문자열 (놀랍게도 그래프 아님)

# 1. 방의 크기 N 입력 (1 ≤ N ≤ 100)
# 2. N줄에 걸쳐 N개의 문자로 방의 배치 입력
# [보충설명] '.'은 아무 것도 없는 곳, 'X'는 짐이 있는 곳
# 3. 가로 방향부터 계산해 2개 이상 '.'이 이어지면 가로 방향 답에 1을 더함
# 4. 같은 방식으로 세로 방향에 대한 답을 구함
# 5. 가로 방향 답과 세로 방향 답을 출력

import sys
input = sys.stdin.readline

N = int(input())
room = []
for _ in range(N):
    room.append(list(input().rstrip()))

ans = [0, 0]  # 가로일 때의 답, 세로일 때의 답
for i in range(N):
    r, c = 0, 0
    for j in range(N):
        if room[i][j] == '.':
            r += 1
        else:
            r = 0
        if r == 2:
            ans[0] += 1

        if room[j][i] == '.':
            c += 1
        else:
            c = 0
        if c == 2:
            ans[1] += 1

print(ans[0], ans[1])
