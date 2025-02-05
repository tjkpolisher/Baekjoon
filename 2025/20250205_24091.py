# 24091: 알고리즘 수업 - 퀵 정렬 2
# 알고리즘 분류: 구현/정렬

# 1. 배열 A의 크기 N, 교환 횟수 K 입력 (5 ≤ N ≤ 10,000, 1 ≤ K ≤ 10^8)
# 2. 서로 다른 배열 A의 원소 N개를 한 줄에 입력 (1 ≤ A_i ≤ 10^9)
# 3. 주어진 의사코드를 참고해 quicksort와 partition 함수 정의
# 4. K회까지 quicksort 함수를 이용한 배열의 원소 교환 진행
# 5. K회까지 교환이 진행되었으면 교환이 진행된 배열을 한 줄에 출력
# 5-1. 단, 정렬 후 교환 횟수가 K보다 작으면 -1을 출력

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0  # 교환 횟수


def partition(arr, p, r):
    global cnt
    x = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            cnt += 1
            if cnt == K:
                print(*arr)
                exit()

    if i + 1 != r:
        arr[i + 1], arr[r] = arr[r], arr[i + 1]
        cnt += 1
        if cnt == K:
            print(*arr)
            exit()

    return i + 1


def quicksort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quicksort(arr, p, q - 1)
        quicksort(arr, q + 1, r)


quicksort(A, 0, N - 1)
print(-1)
