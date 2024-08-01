# 12034: 김인천씨의 식료품가게 (Large)
# 특이사항: 다국어(영어)(한국어 번역)
# 출처: Google Code Jam to I/O for Women 2016 A2번
# 알고리즘 분류: 구현/그리디 알고리즘

# 1. 테스트 케이스 T 입력 (1 ≤ T ≤ 100)
# 2. 테스트 케이스 첫 줄에 상품 수 N 입력 (1 ≤ N ≤ 100)
# 3. 테스트 케이스 둘째 줄에 2*N개의 정수가 오름차순으로 P_i 입력 (1 ≤ Pi ≤ 10^9)
# [보충설명] 원래의 가격은 4의 배수로 주어짐.
# 4. 남은 가격을 저장하는 리스트를 복사
# 5. 리스트를 순회하면서 할인 가격을 남은 가격 리스트에서 탐색
# 6. 해당 할인 가격을 찾으면 할인 가격 리스트에 추가하고, 남은 가격 리스트에서 정상 가격과 할인 가격 제거
# 7. 할인 가격 리스트 오름차순으로 정렬
# 8. 주어진 양식에 따라 할인 가격 리스트 출력

from collections import deque

T = int(input())
for i in range(1, T + 1):
    N = int(input())
    prices = deque(map(int, input().split()))

    remaining_prices = prices.copy()  # 처리된 가격을 관리할 리스트
    discounted_prices = []

    for price in prices:
        if price % 4 == 0:
            discounted_price = price * 3 // 4
            if discounted_price in remaining_prices:
                discounted_prices.append(discounted_price)
                remaining_prices.remove(discounted_price)
                remaining_prices.remove(price)

    discounted_prices.sort()

    print(f"Case #{i}: ", end='')
    print(*discounted_prices)
