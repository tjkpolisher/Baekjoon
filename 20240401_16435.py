# 16435: 스네이크버드
# 알고리즘 분류: 그리디 알고리즘/정렬

# 1. 과일의 개수 N, 스네이크버드의 초기 길이 L 입력
# 2. 과일의 높이 h를 나타내는 N개의 정수 입력
# 3. 과일 높이 리스트를 오름차순으로 정렬
# 4. 현재 자신의 길이 이하라면 리스트에서 맨 앞 숫자를 빼고 길이에 1을 더함
# 5. 과일 높이가 스네이크버드의 몸길이보다 클 경우 종료 및 길이 출력

from collections import deque

N, L = map(int, input().split())
heights = list(map(int, input().split()))
heights.sort()
heights = deque(heights)
for _ in range(N):
    p = heights.popleft()
    if p > L:
        break
    L += 1
print(L)
