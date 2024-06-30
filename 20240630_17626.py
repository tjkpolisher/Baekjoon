# 17626: Four Squares
# 특이사항: 다국어(영어)(한국어 번역)
# 출처: ICPC Seoul Nationalwide Internet Competition 2019 H번
# 알고리즘 분류: 다이나믹 프로그래밍/브루트포스 알고리즘

# 1. n 입력 (1 ≤ n ≤ 50,000) 후 n까지의 제곱수의 개수를 저장할 dp 리스트 생성(dp[1] = 1로 변경)
# 2. 1부터 시작해 숫자 j의 제곱수를 연산
# 3. 제곱수가 n보다 작은 자연수 i보다 커지면, 분기 실행
# 3-1. 아직 i에 값이 할당되지 않았다면 dp[i - j * j] + 1을 할당
# 3-2. i에 값이 이미 할당되었다면 min(dp[i], dp[i - j * j] + 1)을 할당
# 4. dp[n] 출력

import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n + 1)
dp[1] = 1
for i in range(2, n + 1):
    j = 1
    while j * j <= i:
        if dp[i]:
            dp[i] = min(dp[i], dp[i - j * j] + 1)
        else:
            dp[i] = dp[i - j * j] + 1
        j += 1
print(dp[-1])
