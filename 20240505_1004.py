# 1004: 어린 왕자
# 알고리즘 분류: 수학/기하학

# 1. 테스트 케이스의 개수 T 입력
# 2. 테스트 케이스의 첫째 줄에 출발점과 도착점의 x, y 좌표 입력
# 3. 행성계의 개수 n 입력 (1 ≤ n ≤ 50)
# 4. 세 번째 줄 부터 n개의 줄에 걸쳐 행성계의 중점과 반지름 입력 후 딕셔너리에 저장
# [보충설명] -1000 ≤ x1, y1, x2, y2, cx, cy ≤ 1000, 1 ≤ r ≤ 1000
# 5. 최소 행성계 진입/이탈 횟수 출력

import sys
input = sys.stdin.readline


def is_in_the_system(x, y, cx, cy, r):
    d = ((x - cx) ** 2 + (y - cy) ** 2) ** 0.5
    return d < r


T = int(input())
for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())  # 출발점, 도착점 좌표
    n = int(input())  # 행성계의 개수
    cnt = 0
    for i in range(n):
        cx, cy, r = map(int, input().split())  # 각 행성계의 중점과 반지름
        start = is_in_the_system(x1, y1, cx, cy, r)
        end = is_in_the_system(x2, y2, cx, cy, r)
        if (start and not end) or (not start and end):
            cnt += 1
    print(cnt)
