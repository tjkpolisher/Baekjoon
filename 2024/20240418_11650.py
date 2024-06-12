# 11650: 좌표 정렬하기
# 알고리즘 분류: 정렬

# 1. 점의 개수 N 입력 (1 ≤ N ≤ 100,000)
# 2. N개의 줄에 걸쳐 i번째 점의 위치 x_i와 y_i 입력
# 3. 입력받은 2차원 리스트를 x좌표 오름차순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 후 출력

import sys
input = sys.stdin.readline

N = int(input())
coordinates = []
for _ in range(N):
    coordinates.append(list(map(int, input().split())))

coordinates.sort(key=lambda x: (x[0], x[1]))
for i in range(N):
    print(coordinates[i][0], coordinates[i][1])
