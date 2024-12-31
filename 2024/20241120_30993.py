# 30993: 자동차 주차
# 출처: BOJ 2023 제2회 미적확통컵 PA번
# 알고리즘 분류: 수학/조합론

# 1. 양의 정수 형태로 주차장 칸 수 N, 빨간색 자동차 수 A, 초록색 자동차 수 B, 파란색 자동차 수 C 입력
# [보충설명] A + B + C = N ≤ 15
# 2. N! / (A! * B! * C!) 출력

from math import factorial
N, A, B, C = map(int, input().split())
print(factorial(N) // (factorial(A) * factorial(B) * factorial(C)))
