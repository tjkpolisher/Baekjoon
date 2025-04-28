# 14550: 마리오 파티
# 출처: The 2016 Beninese Collegiate Programming Contest H번
# 특이사항: 다국어(영어)(한국어 번역)
# 알고리즘 분류: 다이나믹 프로그래밍

# 1. 테스트 케이스마다 N, S, T 입력(마지막 줄은 0 입력)
# [보충설명] 2 ≤ N ≤ 200, 2 ≤ S ≤ 10, N + 1 ≤ ST, T ≤ N + 1
# 2. 여러 개의 줄에 걸쳐 각 칸에 도착할 때 얻거나 잃는 코인의 수 N개 입력(절대값 10,000 이하)
# 3. 2차원 dp 테이블 생성(행: 이동 횟수, 열: 해당 위치, 값: 최대 수익)
# 4. 2차원 dp 테이블의 1행을 1에서 S까지의 값으로 채우고 시작(나머지 값들은 그대로 False로 유지)
# 5. 2행부터 (T - 1)행까지 다음의 과정 실행
# 5-1. 임시값의 초기값을 적당히 작은 값인 -10^9으로 설정(단, 1열인 경우 0으로 초기화)
# 5-2. 주사위 값을 1에서 S까지 바꾸면서 그 값이 0 이상 N 미만일 경우 다음 실행
# 5-2-1. 이전 행의 (j - k)열이 False일 경우 continue
# 5-2-2. 그렇지 않으면 이전 행의 (j - k)열과 임시값 중 더 큰 값으로 갱신
# 5-3. dp 테이블의 i행 j열을 임시값 + coin_diff[j]로 채우기
# 6. dp 테이블의 끝에서 두 번째 행의 최대값 출력

import sys
input = sys.stdin.readline

while True:
    test_case = input().rstrip()
    if test_case == '0':
        break

    N, S, T = test_case.split()  # 출발점과 별 사이의 칸수, 주사위의 눈 범위, 최대 턴
    N, S, T = int(N), int(S), int(T)
    board = []
    while len(board) < N:
        board.extend(map(int, input().split()))

    dp = [[False] * N for _ in range(T)]
    for i in range(S):
        dp[0][i] = board[i]

    for i in range(1, T - 1):
        for j in range(N):
            tmp = -(10 ** 10)
            if j == 0:
                tmp = 0
            for k in range(1, S + 1):
                if 0 <= j - k < N:
                    if not dp[i - 1][j - k]:
                        continue
                    tmp = max(tmp, dp[i - 1][j - k])

            dp[i][j] = tmp + board[j]

    ans = -10 ** 10
    for i in range(1, S + 1):
        ans = max(ans, dp[-2][-i])
    print(ans)
