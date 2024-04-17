# 11050: 이항 계수 1
# 알고리즘 분류: 수학/구현/조합론

# 1. N, K 입력 (1 ≤ N ≤ 10, 0 ≤ K ≤ N)
# 2. N!/K!(N-K)! 계산 후 출력

from math import factorial
N, K = map(int, input().split())
print(int(factorial(N) / (factorial(K) * factorial(N - K))))
