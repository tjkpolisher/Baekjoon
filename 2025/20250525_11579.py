# 11579: 초차원전쟁 이나
# 출처: 2015 인하대학교 프로그래밍 경시대회 E번
# 알고리즘 분류: 수학/사칙연산/선형대수학

# 1. 테스트 케이스의 수 T 입력
# 2. 차원의 수를 나타내는 양의 정수 n 입력 (1 ≤ n ≤ 500)
# 3. n개의 줄에 걸쳐 여신들의 단위 이동 입력
# [보충설명] i번째 줄에는 i번 단위 이동을 나타내는 n개의 정수 x_ij 입력
# [보충설명] 1 ≤ i ≤ n, 1 ≤ j ≤ n, -1,000 ≤ x_ij ≤ 1,000
# 4. 특정 위치의 좌표를 나타내는 n개의 정수 y_i 입력 (1 ≤ i ≤ n, -5×10^8 ≤ y_i ≤ 5×10^8)
# 5. 목표 좌표 coords 벡터를 앞에서부터 처리하면서 u_r = coords[r] - sum(u_i * moves[i][r]) 계산
# 6. ans에 u_r을 더하기
# 7-1. u_r이 음수이거나 ans가 2*10^9을 넘으면 0 출력 후 다음 루프로 진행
# 7-2. 모든 차원 처리 후 문제가 없으면 1과 ans를 한 줄에 출력

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    moves = [list(map(int, input().split())) for _ in range(n)]
    coords = list(map(int, input().split()))

    ans = 0
    ok = True

    for r in range(n):
        c = coords[r]
        if c < 0:
            print(0)
            ok = False
            break

        u_r = c
        ans += u_r
        if ans > 2 * 10 ** 9:
            print(0)
            ok = False
            break

        for j in range(r, n):
            coords[j] -= u_r * moves[r][j]

    if ok:
        print(1, ans)
