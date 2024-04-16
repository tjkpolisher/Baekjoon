# 2164: 카드2
# 알고리즘 분류: 자료 구조/큐

# 1. 카드의 개수 N 입력 (1 ≤ N ≤ 500,000)
# 2. 1부터 N까지의 번호를 가진 리스트 생성(작은 숫자의 카드가 제일 위에 있음)
# 3. [반복문] 카드가 1장 남을 때까지 아래 과정 반복
# 3-1. 제일 위에 있는 카드를 바닥에 버림
# 3-2. 다시 제일 위에 있는 카드를 제일 아래로 옮김
# 4. 마지막에 남게 되는 카드 출력

from collections import deque

N = int(input())
d = deque(range(1, N + 1))

while len(d) > 1:
    d.popleft()
    popped = d.popleft()
    d.append(popped)

print(d[0])
