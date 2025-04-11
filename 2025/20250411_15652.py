# 15652: N과 M (4)
# 알고리즘 분류: 백트래킹

# 1. 두 자연수 N과 M 입력 (1 ≤ M ≤ N ≤ 8)
# 2. 정답 리스트에 1부터 시작해 하나씩 수를 추가하며 재귀적으로 함수 호출
# 2-1. 새로 추가하는 수는 이전 수보다 크거나 같아야 함.
# 2-2. 정답 리스트의 길이가 M이 되면 리스트를 한 줄에 하나씩 출력

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N, M = map(int, input().split())


def sequence(n, s):
    if len(s) == M:
        print(*s)
        return
    for num in range(n, N + 1):
        sequence(num, s + [num])


ans = []
for i in range(1, N + 1):
    sequence(i, [i])
