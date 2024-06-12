# 1835: 카드
# 특이사항: 다국어(영어)(한국어 번역)
# 출처: ICPC Northwestern European Regional Contest NCPC 2006 E번
# 알고리즘 분류: 자료 구조/덱/구현/시뮬레이션

# 1. 카드의 개수 N 입력 (1 ≤ N ≤ 1,000)
# 2. 1부터 N까지의 숫자가 입력된 덱(deque)을 가정
# 3. [문제에서 요구한 과정]
# 3-1. 첫 번째 카드를 큐 뒤로 옮김
# 3-2. 다시 첫 번째 카드를 책상 위에 놓음(이 카드는 1이 되어야 함)
# 3-3. 3-1을 두 번 반복한 후 첫 번째 카드를 책상 위에 놓음(2가 되어야 함)
# 3-4. 같은 방식으로 3-1을 N-1번 반복한 후 책상에 놓는 카드가 N-1번 카드가 되어야 함.
# 3-5. 큐에 N번 카드만 남으면 종료.
# 4. N번 카드부터 큐에 넣고 시작.
# 5. N - 1번 카드를 덱 맨 앞에 넣고 N - 1회 맨 뒤 카드를 맨 앞으로 돌림
# 6. 5번 과정을 N - 2 ~ 1번 카드에 대해 진행
# 7. 모든 과정을 거친 뒤 카드 덱의 순서대로 카드 출력

from collections import deque

N = int(input())
deck = deque([N])
num = N

while len(deck) < N:
    num -= 1
    deck.appendleft(num)
    for _ in range(num):
        p = deck.pop()
        deck.appendleft(p)

print(*deck)
