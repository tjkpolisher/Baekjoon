# 9753: 짝 곱
# 특이사항: 다국어(영어)(한국어 번역)
# 출처: Thailand Central Group-B Programming Contest 2013 A번
# 알고리즘 분류: 수학/정수론/소수 판정/에라토스테네스의 체

# 1. 테스트 케이스의 개수 T 입력 (1 ≤ T ≤ 20)
# 2. 10만까지의 자연수 중 소수를 담은 리스트 생성
# 3. 서로 다른 두 소수의 곱을 구하고 정렬
# 4. T개의 줄에 걸쳐 정수 K 입력 (1 ≤ K ≤ 100,000)
# 5. 이진 탐색을 통해 K와 가장 가까운 소수의 곱을 탐색
# 6. 탐색한 소수의 곱 값을 출력

import sys
import bisect
input = sys.stdin.readline

MAX = 100_000 * 2
is_prime = [True] * (MAX + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(MAX ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, MAX + 1, i):
            is_prime[j] = False
primes = [i for i, v in enumerate(is_prime) if v]

products = set()
for i in range(len(primes)):
    for j in range(i + 1, len(primes)):
        prod = primes[i] * primes[j]
        if prod > 200_000:
            break
        products.add(prod)
products = sorted(products)

T = int(input())
for _ in range(T):
    K = int(input())
    idx = bisect.bisect_left(products, K)
    print(products[idx])
