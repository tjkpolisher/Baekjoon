# 23968: 알고리즘 수업 - 버블 정렬 1
# 알고리즘 분류: 구현/정렬/시뮬레이션

# 1. 배열 A의 크기 N, 교환 횟수 K 입력 (5 ≤ N ≤ 10,000, 1 ≤ K ≤ N^2)
# 2. 배열 A의 원소 N개 입력 (1 ≤ A_i ≤ 10^9)
# 3. 버블 정렬을 오름차순으로 정렬하는 과정을 K회 반복
# 4. K번째에 교환되는 두 수를 작은 수부터 한 줄에 출력
# 4-1. 단, 총 교환 횟수가 K보다 작으면 -1 출력

N, K = map(int, input().split())
A = list(map(int, input().split()))

if N ** 2 < K:
    print(-1)
    exit()


def bubble_sort(arr, k):
    cnt = 0
    for i in range(N, 0, -1):
        for j in range(0, i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                cnt += 1
            if cnt == k:
                return f'{arr[j]} {arr[j + 1]}'
    return -1


print(bubble_sort(A, K))
