# 2798: 블랙잭
# 특이사항: 다국어(영어)(한국어 번역)
# 알고리즘 분류: 브루트포스 알고리즘

# 1. 카드의 개수 N, 딜러가 외칠 숫자 M 입력
# 2. 카드에 쓰여 있는 N개의 수 입력
# 3. 카드의 수 오름차순으로 정렬
# 4. 맨 앞 카드의 수부터 차례대로 더하면서 M에 최대한 가까운 3장의 합 구하기
# 4-1. 단, 합이 M보다 커질 경우 pass
# 5. 가장 가까운 카드 3장의 합 출력

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cards = list(map(int, input().split()))
cards.sort()
result = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            tmp = cards[i] + cards[j] + cards[k]
            if tmp > M:
                pass
            else:
                result = max(result, tmp)

print(result)
