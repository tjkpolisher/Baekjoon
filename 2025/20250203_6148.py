# 6148: Bookshelf 2
# 특이사항: 다국어(영어)
# 출처: USACO December 2007 Contest Bronze 2번
# 알고리즘 분류: 그래프 이론/브루트포스 알고리즘/그래프 탐색/깊이 우선 탐색/백트래킹

# 1. 소의 마리 수 N, 찬장의 높이 B 입력 (1 ≤ N ≤ 20, 1 ≤ B ≤ S, S는 모든 소의 키의 합)
# 2. N개의 줄에 걸쳐 소의 키 H_i 입력(1 ≤ H_i ≤ 1,000,000)
# 2-1. 입력받은 키를 리스트에 저장
# 2-2. 동시에, 키의 합을 저장하는 변수에 키를 더함
# 3. 백트래킹을 이용해 정답과 sum - B를 구하는 정답 계산
# 4. 정답 출력

import sys
input = sys.stdin.readline

N, B = map(int, input().split())
heights = []
sum_height = 0
for _ in range(N):
    height = int(input())
    heights.append(height)
    sum_height += height


def backtracking(start, total):
    if total >= B:
        global ans
        ans = min(ans, total - B)
        return
    for i in range(start, N):
        backtracking(i + 1, total + heights[i])


ans = 10 ** 9
backtracking(0, 0)

print(ans)
