# 6064: 카잉 달력
# 특이사항: 다국어(영어)(한국어 번역)
# 출처: ICPC Korea Daejeon Nationalwide Internet Competition 2013 B번
# 알고리즘 분류: 수학/브루트포스 알고리즘/정수론/중국인의 나머지 정리

# 1. 테스트 데이터의 개수 T 입력
# 2. 네 개의 정수 M, N, x, y 입력 (1 ≤ M, N ≤ 40,000, 1 ≤ x ≤ M, 1 ≤ y ≤ N)
# [보충설명] <M:N>은 카잉 달력의 마지막 해를 나타냄.
# 3. M과 N의 최대공약수와 최소공배수(마지막 해)를 구함.
# 4. 정답을 x로 초기화시킨 후 M씩 증가시키면서 y로 나타낼 수 있을 때까지 반복
# 5-1. 결과값이 n으로 나뉘어지지 않거나 마지막 해를 초과하면 -1을 출력
# 5-2. 그렇지 않으면 계산한 정답 출력

from math import gcd, lcm

T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    GCD = gcd(M, N)
    LCM = lcm(M, N)
    ans = x
    while ans <= LCM:
        if (ans - 1) % N + 1 == y:
            break
        ans += M
    if ans > LCM:
        print(-1)
    else:
        print(ans)
