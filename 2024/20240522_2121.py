# 2121: 넷이 놀기
# 알고리즘 분류: 자료 구조/기하학/이분 탐색/해시를 사용한 집합과 맵

# 1. 점의 개수 N 입력 (5 ≤ N ≤ 500,000)
# 2. 직사각형의 가로 길이 A, B 입력 (1 ≤ A, B ≤ 1,000)
# 3. N줄에 걸쳐 점들의 좌표 입력 (-1,000,000,000 이상 1,000,000,000 이하)
# 4. 점들의 좌표를 순회하면서 직사각형을 구성할 수 있는 조합을 찾으면 개수에 1을 더함
# 5. 개수 출력

import sys
input = sys.stdin.readline

N = int(input())
A, B = map(int, input().split())
dots = set()
for _ in range(N):
    dots.add(tuple(map(int, input().split())))

cnt = 0
for dot in dots:
    key1 = (dot[0] + A, dot[1]) in dots
    key2 = (dot[0], dot[1] + B) in dots
    key3 = (dot[0] + A, dot[1] + B) in dots
    if key1 and key2 and key3:
        cnt += 1

print(cnt)
