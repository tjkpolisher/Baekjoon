# 1920: 수 찾기
# 알고리즘 분류: 자료 구조/정렬/이분 탐색

# 1. 자연수 N 입력 (1 ≤ N ≤ 100,000)
# 2. 수열 A를 이루는 N개의 정수 입력
# 3. 정수 M 입력 (1 ≤ M ≤ 100,000)
# 4. M개의 정수 입력(이 수들이 A 안에 존재하는지 알아내야 함)

import sys
input = sys.stdin.readline

N = int(input().rstrip())
A = list(map(int, input().rstrip().split()))
A.sort()
M = int(input().rstrip())
Ms = list(map(int, input().rstrip().split()))


def binary_search(start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if A[mid] == target:
            return 1
        elif A[mid] >= target:
            end = mid - 1
        else:
            start = mid + 1
    return 0


for i in range(M):
    target = Ms[i]
    print(binary_search(0, N - 1, target))
