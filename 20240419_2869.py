# 2869: 달팽이는 올라가고 싶다
# 특이사항: 다국어(영어)(한국어 번역)
# 알고리즘 분류: 수학

# 1. A, B, V 입력 (1 ≤ B < A ≤ V ≤ 1,000,000,000)
# 2. V // (A - B) = n으로 계산
# 3-1. 만약 A * n + B * (n - 1)이 V보다 크면 그대로 출력
# 3-2. 작을 경우에는 A * (n + 1) + B * n 출력

import sys
input = sys.stdin.readline

A, B, V = map(int, input().split())
n, rem = divmod((V - B), (A - B))
if rem == 0:
    print(n)
else:
    print(n + 1)
