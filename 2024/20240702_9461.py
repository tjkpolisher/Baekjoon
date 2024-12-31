# 9461: 파도반 수열
# 특이사항: 다국어(영어)(한국어 번역)
# 출처: ICPC Asia Reginal - Daejeon 2013 G번
# 알고리즘 분류: 수학/다이나믹 프로그래밍

# 1. 테스트 케이스의 개수 T 입력
# 2. 테스트 케이스마다 N 입력 (1 ≤ N ≤ 100)
# 3. 각 인덱스 별 리스트를 생성하고 [1, 1, 1, 2, 2]를 우선 생성
# 4. i번째 변 길이 + (i + 4)번째 변의 길이를 리스트 맨 끝에 append
# 5. 리스트의 맨 마지막 원소 출력

T = int(input())
for _ in range(T):
    N = int(input())
    dp = [1, 1, 1, 2, 2]
    if N > 5:
        for i in range(5, N):
            dp.append(dp[i - 5] + dp[i - 1])
    print(dp[N - 1])
