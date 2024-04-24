# 11047: 동전 0
# 알고리즘 분류: 그리디 알고리즘

# 1. 동전의 종류 N, 목표 가치의 합 K 입력 (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)
# 2. N개의 줄에 걸쳐 동전의 가치를 오름차순으로 입력 (1 ≤ A_i ≤ 1,000,000, A_1 = 1, i ≥ 2인 경우에 A_i는 A_{i-1}의 배수)
# 3. 단, A_i가 K를 초과하면 리스트에 추가하지 않음
# 4. 가장 큰 원소부터 리스트에서 pop하여 K와 나눗셈 연산 진행
# 5. 몫을 답에 더하고, 나머지는 K의 새로운 값으로서 갱신
# 6. K의 값이 0에 도달하면 종료 후 개수 출력

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
values = []
for _ in range(N):
    A_i = int(input())
    if A_i <= K:
        values.append(A_i)

ans = 0
while K:
    p = values.pop()
    v1, v2 = divmod(K, p)
    ans += v1
    K = v2  # 남은 가치 갱신

print(ans)
