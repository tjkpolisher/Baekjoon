# 12000: Circular Barn (Bronze)
# 특이사항: 다국어(영어)
# 출처: USACO February 2016 Contest Bronze 2번
# 알고리즘 분류: 구현/브루트포스 알고리즘

# 1. 헛간 안의 방의 개수 n 입력 (3 ≤ n ≤ 1000)
# 2. n개의 줄에 걸쳐 각 방의 소의 마릿수 r_1, r_2, ..., r_n 입력 (1 ≤ r_i ≤ 100)
# 3. 입력받은 소의 마릿수를 리스트에 저장
# 4. 0번부터 n-1까지의 인덱스에 대하여 다음 계산
# 4-1. i번 방에서 시작해 시계 방향으로 돌면서 각 방의 소가 이동하는 거리 계산
# 4-2. 각 방의 연산이 끝나면 이전 값과 비교해 작은 값으로 갱신
# 5. 최소 거리 출력

import sys
input = sys.stdin.readline

n = int(input())
cows = [int(input()) for _ in range(n)]
ans = 10 ** 9

for i in range(n):
    dist = 0
    for j in range(n):
        idx = (i + j) % n
        dist += cows[idx] * j
    ans = min(ans, dist)

print(ans)
