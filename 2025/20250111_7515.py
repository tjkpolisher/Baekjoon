# 7515: Prehistoric Operating System
# 특이사항: 다국어(영어)
# 출처: TUD Contest 2008 (Single) 5번
# 알고리즘 분류: 다이나믹 프로그래밍

# 1. 시나리오의 개수 입력
# 2. 각 시나리오마다 운영체제의 개수 n 입력 (1 ≤ n ≤ 40)
# 3. 입력된 n에 대하여 피보나치 수열을 계산
# 4. 수열의 n항을 표시 형식에 맞게 출력

import sys
input = sys.stdin.readline


def calculate(n):
    if n == 1:
        return 2
    elif n == 2:
        return 3
    dp = [0] * (n + 1)
    dp[1], dp[2] = 2, 3
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


T = int(input())
for i in range(T):
    n = int(input())

    print(f"Scenario {i + 1}:\n{calculate(n)}")
    if i != T - 1:
        print()
