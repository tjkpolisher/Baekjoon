# 1331: 나이트 투어
# 알고리즘 분류: 구현/시뮬레이션

# 1. 36개의 줄에 걸쳐 나이트가 방문한 순서대로 체스판에 존재하는 칸을 입력
# [보충설명] 체스판의 크기는 6x6, 한 칸은 A~F까지의 알파벳과 1~6까지의 숫자를 하나씩 조합해서 표기.
# 2. 나이트가 움직일 수 있는 경우의 수 맞게 x, y 방향의 인덱스를 제어
# 3-1. 처음 입력받은 경우, 해당 칸의 x, y 좌표를 초기값으로 설정
# 3-2. 이후에 입력받은 경우 나이트가 움직일 수 있는 8가지 경우의 수에 따라 움직일 수 있는 경로인지 판단.
# 3-2-1. 이동할 수 없는 경로일 경우 Invalid를 출력하고 종료.
# 3-2-2. 이동할 수 있는 경로일 경우 현재까지 방문한 좌표에 있는지 체크
# 4. 방문 여부를 저장하는 2중 리스트에 False가 있는 경우 Invalid를 출력
# 5. 위 사항을 모두 준수했을 경우 Valid 출력

visited = [[False] * 6 for _ in range(6)]  # 좌표 방문 여부 체크
dx = [1, 1, 2, 2, -1, -1, -2, -2]
dy = [2, -2, 1, -1, 2, -2, 1, -1]
alphabets = ['A', 'B', 'C', 'D', 'E', 'F']

for i in range(36):
    coord = input()
    x = alphabets.index(coord[0])
    y = int(coord[1]) - 1

    if i == 0:
        orig_x = alphabets.index(coord[0])
        orig_y = int(coord[1]) - 1
        ox = orig_x
        oy = orig_y
        visited[y][x] = True
        continue

    for j in range(8):
        nx = ox + dx[j]
        ny = oy + dy[j]
        if 0 <= nx < 6 and 0 <= ny < 6 and nx == x and ny == y:
            visited[ny][nx] = True
            ox = nx
            oy = ny
            break


def is_valid():
    for i in range(6):
        for j in range(6):
            if not visited[j][i]:
                return "Invalid"
    return "Valid"


# 마지막 체크
for i in range(8):
    nx = ox + dx[i]
    ny = oy + dy[i]
    if 0 <= nx < 6 and 0 <= ny < 6 and nx == orig_x and ny == orig_y:
        print(is_valid())
        break
else:
    print("Invalid")
