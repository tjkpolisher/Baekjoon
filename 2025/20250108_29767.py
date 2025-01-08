# 29767: 점수를 최대로
# 출처: 단대소프트고 2023 알고리즘 대회 B번
# 알고리즘 분류: 그리디 알고리즘/정렬/누적 합

# 1. 교실의 개수 N, 학생의 수 K 입력 (1 ≤ K ≤ N ≤300,000)
# 2. N개의 교실에 대한 고정 점수 A_1, A_2, ..., A_N 입력 (-10^8 ≤ A_i ≤ 10^8)
# 3. dp 테이블 생성
# 4. dp[i] = dp[i - 1] + classrooms[i]를 계산
# 5. dp 테이블을 내림차순으로 정렬
# 6. dp 테이블의 K - 1번째 인덱스까지의 합을 출력

N, K = map(int, input().split())
classrooms = list(map(int, input().split()))

dp = [0] * N
dp[0] = classrooms[0]
for i in range(1, N):
    dp[i] = dp[i - 1] + classrooms[i]

dp.sort(reverse=True)
print(sum(dp[:K]))
