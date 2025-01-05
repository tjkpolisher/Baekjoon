# 6588: 골드바흐의 추측
# 특이사항: 다국어(영어)(한국어 번역)
# 출처: University of Ulm Local Contest 1998 G번
# 알고리즘 분류: 수학/정수론/소수 판정/에라토스테네스의 체

# 1. 시작하기 전 100만 이하의 홀수인 소수를 집합에 저장
# 2. 테스트 케이스마다 짝수인 정수 n 입력 (6 ≤ n ≤ 1000000)
# 2-1. 입력의 마지막 줄에는 0이 하나 주어짐
# 3. 소수 집합 중 2개를 고르는 투 포인터 순회
# 4. 각 조합들을 순회하면서 그 합이 n이 되는지 확인
# 4-1. n이 나올 경우 n = a + b 형식으로 정답 출력
# 4-2. 조합이 나올 수 없는 경우 "Goldbach's conjecture is wrong." 출력

import sys
input = sys.stdin.readline

prime = [True] * 1000001
for i in range(2, int(1000001 ** 0.5) + 1):
    if prime[i]:
        for j in range(i * 2, 1000001, i):
            prime[j] = False

while True:
    n = int(input())
    if not n:
        break
    for i in range(3, n - 2, 2):
        if prime[i] and prime[n - i]:
            print(f"{n} = {i} + {n - i}")
            break
    else:
        print("Goldbach's conjecture is wrong.")
