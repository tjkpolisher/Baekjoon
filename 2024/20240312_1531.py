# 1531: 투명
# 알고리즘 분류: 구현/시뮬레이션

# 1. 종이의 개수 N, 그림이 안 보이는 종이의 개수 M 입력
# 2. [반복문] N개의 줄에 걸쳐 종이의 좌표 입력
# 3. 입력받은 좌표들 중 원본 모자이크 그림의 좌표에 해당하는 부분에 1을 더함
# 4. 모든 종이의 좌표를 입력받은 후, 모자이크 그림의 각 좌표에서 M보다 큰 수가 있는 곳을 count해서 출력

N, M = map(int, input().split())
picture = [[0] * 100 for _ in range(100)]

for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(y1 - 1, y2):
        for i in range(x1 - 1, x2):
            picture[j][i] += 1

ans = 0
for i in range(100):
    for j in range(100):
        if picture[j][i] > M:
            ans += 1

print(ans)
