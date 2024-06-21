# 30802: 웰컴 키트
# 특이사항: 다국어(영어)(한국어 번역)
# 출처: solved.ac Grand Arena #3 Division 2 A번
# 알고리즘 분류: 수학/구현/사칙연산

# 1. 참가자의 수 N 입력 (1 ≤ N ≤ 10^9)
# 2. 티셔츠 사이즈별 신청자의 수 S, M, L, XL, XXL, XXXL 입력
# [보충설명] 0 ≤ S, M, L, XL, XXL, XXXL ≤ N, S + M + L + XL + XXL + XXXL = N
# 3. 티셔츠와 펜의 묶음 수를 의미하는 정수 T와 P 입력 (2 ≤ T, P ≤ 10^9)
# 4. 펜 묶음의 개수 = N // P, 한 자루씩 주문할 양 = N % P
# 5. S부터 XXXL까지 순서대로 N을 해당 수로 나눈 값을 계산
# 6. 최대값일 경우 갱신
# 7. 티셔츠 묶음의 개수 최대값과 펜 묶음, 펜 한 자루 주문 개수 출력

N = int(input())
sizes = list(map(int, input().split()))
T, P = map(int, input().split())

n_t = 0
for size in sizes:
    t1, t2 = divmod(size, T)
    if t2:
        t1 += 1
    n_t += t1
p1, p2 = divmod(N, P)

print(n_t)
print(p1, p2)
