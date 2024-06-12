# 2161: 카드1
# 알고리즘 분류: 구현/자료구조/큐

## 1. 카드의 수 N 입력
## 1-1. 1번 카드가 제일 위에, N번 카드가 제일 아래인 상태로 시작
## 2. [반복문] 카드가 한 장 남을 때까지 반복
## 2-1. 제일 위에 있는 카드를 버림(버린 카드를 순서대로 출력)
## 2-2. 1을 시행한 이후에 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮기기
## 3. 마지막에 남은 카드를 출력

from collections import deque
N = int(input())
card_deck = deque(range(1, N + 1))
while len(card_deck) > 1:
    print(card_deck[0], end=' ')
    card_deck.popleft()
    next_card = card_deck.popleft()
    card_deck.append(next_card)
print(card_deck[0], end=' ')