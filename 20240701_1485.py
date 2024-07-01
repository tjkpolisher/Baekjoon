# 1485: 정사각형
# 알고리즘 분류: 정렬/기하학

# 1. 테스트 케이스의 개수 T 입력
# 2. 네 줄에 걸쳐 점의 좌표(x, y)를 한 줄에 하나씩 입력
# [보충설명] 점의 좌표는 -100,000 이상 100,000 이하의 정수, 같은 점이 두 번 이상 주어지지 않음
# 3. 네 개의 점의 좌표를 리스트에 저장한 뒤, x좌표를 기준으로 오름차순, 같은 좌표이면 y좌표를 기준으로 오름차순으로 정렬
# (편의상 이렇게 정렬된 점의 순서대로 1, 2, 3, 4번 점이라고 칭함)
# 3-1. 3번과 4번의 위치를 바꿔 1번부터 시계 방향으로 1,2,3,4번 점으로 정렬되게끔 순서 변경
# 4-1. 네 점의 길이가 모두 같은지 체크 후 아니면 0 출력 후 종료
# 4-2. 두 대각선의 길이가 서로 같은지 체크 후 아니면 0 출력, 같으면 1 출력

T = int(input())


def length(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


for _ in range(T):
    coords = []
    for i in range(4):
        x, y = map(int, input().split())
        coords.append((x, y))
    coords.sort(key=lambda x: (x[0], x[1]))
    coords[2], coords[3] = coords[3], coords[2]

    # 대각선 길이 체크
    diag1 = length(coords[0], coords[2])
    diag2 = length(coords[1], coords[3])
    if diag1 != diag2:
        print(0)
        continue

    # 변 길이 체크
    lengths = set()
    for i in range(4):
        if i == 3:
            lengths.add(length(coords[3], coords[0]))
        else:
            lengths.add(length(coords[i], coords[i + 1]))
    if len(lengths) > 1:
        print(0)
    else:
        print(1)
