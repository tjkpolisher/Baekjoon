# 24174: 알고리즘 수업 - 힙 정렬 2
# 알고리즘 분류: 구현/정렬

# 1. 배열 A의 크기 N(5 ≤ N ≤ 500,000), 교환 횟수 K(1 ≤ K ≤ 10^8) 입력
# 2. 서로 다른 배열 A의 원소 N개를 한 줄에 입력 (1 ≤ A_i ≤ 10^9)
# 3. 배열 A의 맨 앞쪽에 0을 추가
# 4. 교환 카운터와 K번째 교환을 찾았는지 플래그 변수 선언
# 5. 교환이 일어날 때마다 카운터를 증가시키고 K번째 교환인지 확인
# 5-1. K번째 교환일 경우 배열을 출력하고 플래그를 True로 변환
# 6. K번째 교환 직후의 배열을 공백으로 구분해 출력
# 6-1. 단, 총 교환 횟수가 K보다 작으면 -1을 출력

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

A = [0] + arr

cnt = 0
found = False


def heapify(A, k, n):
    global cnt, K, found

    left = 2 * k
    right = 2 * k + 1

    if right <= n:
        if A[left] < A[right]:
            smaller = left
        else:
            smaller = right
    elif left <= n:
        smaller = left
    else:
        return

    if A[smaller] < A[k]:
        A[smaller], A[k] = A[k], A[smaller]
        cnt += 1
        if cnt == K:
            print(*A[1:])
            found = True
            return

        heapify(A, smaller, n)


def build_min_heap(A, n):
    for i in range(n // 2, 0, -1):
        if found:
            return
        heapify(A, i, n)


def heap_sort(A, n):
    global cnt, found

    build_min_heap(A, n)

    for i in range(n, 1, -1):
        if found:
            return

        A[1], A[i] = A[i], A[1]
        cnt += 1

        if cnt == K:
            print(*A[1:])
            found = True
            return

        heapify(A, 1, i - 1)


heap_sort(A, N)
if not found:
    print(-1)
