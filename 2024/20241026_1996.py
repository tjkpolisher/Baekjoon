# 1996: 지뢰 찾기
# 알고리즘 분류: 구현

# 1. 맵의 크기 N 입력 (1 ≤ N ≤ 1,000)
# 2. N개의 줄에 걸쳐 map의 정보 입력 ('.'은 지뢰가 없음을, 숫자는 그 칸의 지뢰의 개수를 의미)
# 2-1. 정보 입력 시 숫자가 적힌 칸을 '*'로 입력해 별도의 정답 리스트에 저장
# 3. 맵 리스트의 N * N개의 원소들을 순회
# 3-1. 2-1에서 정답 리스트에 '*'로 표시해둔 칸에서는 continue
# 3-2. 해당 칸 주위 8개의 칸을 탐색하면서 지뢰의 개수 집계
# 3-3. 지뢰의 개수를 정답 리스트에 저장하되, 10개 이상인 경우 'M'으로 저장
# 4. 정답 리스트를 주어진 형식에 맞게 출력

import sys
input = sys.stdin.readline

N = int(input())
mine_map = []
ans = [[0] * N for _ in range(N)]
for i in range(N):
    row = input().rstrip()
    for j in range(N):
        if row[j] != '.':
            ans[i][j] = '*'
    mine_map.append(list(row))

# 탐색할 8개의 방향 지정(좌상, 상, 우상, 좌, 우, 좌하, 하, 우하)
dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [1, 1, 1, 0, 0, -1, -1, -1]
for i in range(N):
    for j in range(N):
        if ans[i][j] == '*':
            continue
        cnt = 0  # 지뢰의 개수
        for k in range(8):
            nx = i + dx[k]
            ny = j + dy[k]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if mine_map[nx][ny] != '.':
                cnt += int(mine_map[nx][ny])
            if cnt >= 10:
                ans[i][j] = 'M'
                break
        else:
            ans[i][j] = str(cnt)

# 출력
for i in range(N):
    print(''.join(ans[i]))
