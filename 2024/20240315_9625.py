# 9625: BABBA
# 특이사항: 다국어(영어)(한국어 번역)
# 알고리즘 분류: 다이나믹 프로그래밍

# 1. K 입력 (1 ≤ K ≤ 45)
# 2. a, b = b, a + b라는 점화식을 사용해 반복문 처리
# 3. A와 B의 개수 출력

K = int(input())
a, b = 0, 1
for _ in range(1, K):
    a, b = b, a + b

print(a, b)
