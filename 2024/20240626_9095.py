# 9095: 1, 2, 3 더하기
# 출처: ICPC Regional Asia Pacific Korea Taejon 2001 PC번
# 알고리즘 분류: 다이나믹 프로그래밍

# 1. 테스트 케이스의 개수 T 입력
# 2. 테스트 케이스 n을 입력 (n은 11보다 작은 양수)
# 3. n을 1, 2, 3의 합으로 나타내는 방법을 찾고 개수를 출력

T = int(input())
for _ in range(T):
    n = int(input())
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        if i - 1 >= 0:
            dp[i] += dp[i - 1]
        if i - 2 >= 0:
            dp[i] += dp[i - 2]
        if i - 3 >= 0:
            dp[i] += dp[i - 3]
    print(dp[n])
