# 11651: 좌표 정렬하기 2
# 알고리즘 분류: 정렬

# 1. 점의 개수 N 입력 (1 ≤ N ≤ 100,000)
# 2. N개의 줄에 걸쳐 i번 점의 위치 x_i, y_i 입력 (-100,000 ≤ x_i, y_i ≤ 100,000)
# 3. y좌표에 대해 오름차순으로, y좌표가 같으면 x좌표 오름차순으로 정렬
# 4. 정렬된 순서대로 출력

import sys
input = sys.stdin.readline

N = int(input())
coordinates = []
for _ in range(N):
    x_i, y_i = map(int, input().split())
    coordinates.append((x_i, y_i))

coordinates.sort(key=lambda x: (x[1], x[0]))
for i in range(N):
    print(coordinates[i][0], coordinates[i][1])
