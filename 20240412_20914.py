# 20914: QWERTY 자판
# 특이사항: 다국어(영어)(한국어 번역)
# 알고리즘 분류: 구현/그래프 이론/시뮬레이션

# 1. 키보드 상의 자판들을 인접 리스트 형태의 그래프로 표현
# 2. 테스트 케이스의 수 T 입력
# 3. [반복문]
# 3-1. 영문 대문자로만 구성된 문자열 s 입력
# 3-2. s를 구성하는 각 문자에 대해 BFS를 실시해 다음 문자열까지 가는 경로 탐색
# 3-3. 입력할 때 기본 1초 더해주고, 탐색 깊이에 따라 2초를 더해 줌.
# 3-4. 마지막 글자까지 탐색 후 총 소모된 시간 출력

from collections import deque
keyboards = [
    ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
    ['Z', 'X', 'C', 'V', 'B', 'N', 'M']
]
table = dict()
for i, c in enumerate(keyboards):
    for j, ch in enumerate(c):
        table[ch] = (i, j)

T = int(input())

dx = [0, 0, 1, -1, 1, -1]
dy = [1, -1, 0, 0, -1, 1]


def bfs(start, end):
    visited = [[False for _ in range(len(keyboards[0]))] for _ in range(3)]
    visited[1][-1] = True
    visited[2][-1] = True
    visited[2][-2] = True
    visited[2][-3] = True
    cur_y, cur_x = table[start][0], table[start][1]

    q = deque()
    q.append([cur_y, cur_x, 0])
    while q:
        cur_y, cur_x, t = q.popleft()
        visited[cur_y][cur_x] = True
        if cur_y == table[end][0] and cur_x == table[end][1]:
            return t * 2
        for i in range(6):
            next_x, next_y = cur_x + dx[i], cur_y + dy[i]
            if 0 <= next_x < 10 and 0 <= next_y < 3 and not visited[next_y][next_x]:
                q.append([next_y, next_x, t + 1])


for _ in range(T):
    s = input()
    second = 1  # 첫 번째 키를 입력하고 시작
    for i in range(1, len(s)):
        second += bfs(s[i - 1], s[i])
        second += 1
    print(second)
