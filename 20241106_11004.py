# 11004: K번째 수
# 알고리즘 분류: 정렬

# 1. N, K 입력 (1 ≤ N ≤ 5,000,000, 1 ≤ K ≤ N)
# 2. A_1, A_2, ..., A_N 입력 (-10^9 ≤ Ai ≤ 10^9)
# 3. A의 리스트를 오름차순으로 정렬
# 4. K번째 수(인덱스 상으로는 K-1번) 출력

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A_list = sorted(list(map(int, input().split())))
print(A_list[K - 1])
