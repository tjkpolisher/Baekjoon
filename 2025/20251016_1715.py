# 1715: 카드 정렬하기
# 알고리즘 분류: 자료 구조/그리디 알고리즘/우선순위 큐

# 1. N 입력 (1 ≤ N ≤ 100,000)
# 2. N개의 줄에 걸쳐 숫자 카드 묶음의 크기 입력 (1000 이하의 양의 정수)
# 3. 카드 묶음의 크기를 힙에 입력
# 4. 힙에 원소가 1개 남을 때까지 다음 반복
# 4-1. 가장 작은 2개의 카드 묶음 꺼내기
# 4-2. 꺼낸 두 원소를 합친 뒤 정답에 더하고 다시 힙에 삽입
# 5. 정답 출력

import sys
import heapq
input = sys.stdin.readline

N = int(input())
cards = []
for _ in range(N):
    data = int(input())
    heapq.heappush(cards, data)

result = 0

while len(cards) > 1:
    card1 = heapq.heappop(cards)
    card2 = heapq.heappop(cards)
    new_card = card1 + card2

    result += new_card
    heapq.heappush(cards, new_card)

print(result)
