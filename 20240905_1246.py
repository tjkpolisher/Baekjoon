# 1246: 온라인 판매
# 특이사항: 다국어(영어)(한국어 번역)
# 출처: USA Computing Olympiad November 2008 Contest Bronze 3번
# 알고리즘 분류: 그리디 알고리즘/정렬

# 1. 달걀의 개수 N, 잠재 고객의 수 M 입력 (1 ≤ N ≤ 1,000, 1 ≤ M ≤ 1,000)
# 2. M개의 줄에 걸쳐 i번째 고객이 각자 달걀 하나를 구매할 수 있는 가격 상한 P_i 입력 (1 ≤ P_i ≤ 1,000,000)
# 3. 가격을 저장한 리스트를 내림차순으로 정렬
# 4. 가장 높은 가격 * 그 가격의 순서(몇 번째인지)를 수익으로 정하고 인덱스를 바꿔가며 비교
# 5. 더 이상 분배를 할 수 없는 가격을 A로 할당하고, 현재 분배된 가격과 달걀의 개수로 수익 계산
# 5-1. 단, 반복문 상에서 인덱스 + 1이 달걀의 개수 N을 초과했을 경우 반복문 종료
# 6. 책정한 가격 A와 이 가격으로 올릴 수 있는 수익 출력

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
prices = []
for _ in range(M):
    prices.append(int(input()))

prices.sort(reverse=True)
revenue = 0
for i in range(M):
    tmp_price = prices[i]
    if i + 1 <= N:
        tmp_revenue = tmp_price * (i + 1)
        if tmp_revenue > revenue:
            revenue = tmp_revenue
            A = tmp_price
    else:
        break
print(A, revenue)
