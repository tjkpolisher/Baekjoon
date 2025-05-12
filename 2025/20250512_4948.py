# 4948: 베르트랑 공준
# 특이사항: 다국어(영어)(한국어 번역)
# 출처: ICPC 2011 Japan Domestic Contest A번
# 알고리즘 분류: 수학/정수론/소수 판정/에라토스테네스의 체

# 1. 에라토스테네스의 체를 이용해 246912까지의 소수를 구함
# 2. 각 인덱스까지의 소수의 개수를 저장
# 3. 한 줄에 정수 입력
# 3-1. 0이 입력되면 프로그램 종료
# 4. 인덱스 2n의 수에서 인덱스 n의 수를 빼서 출력

import sys
input = sys.stdin.readline

MAX_N = 123456
MAX_LIMIT = 2 * MAX_N

is_prime = [True] * (MAX_LIMIT + 1)
is_prime[0] = False
is_prime[1] = False
for i in range(2, int(MAX_LIMIT ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i ** 2, MAX_LIMIT + 1, i):
            is_prime[j] = False

prime_count = [0] * (MAX_LIMIT + 1)
cnt = 0
for i in range(MAX_LIMIT + 1):
    if is_prime[i]:
        cnt += 1
    prime_count[i] = cnt

while True:
    n = int(input())
    if n == 0:
        break
    print(prime_count[2 * n] - prime_count[n])
