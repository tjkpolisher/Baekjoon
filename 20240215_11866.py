# 11866: 요세푸스 문제 0
# 알고리즘 분류: 구현/자료구조/큐

## 1. N, K 입력
## 2. 1부터 N까지의 원소를 갖는 큐 생성
## 3. [반복문] N명의 사람들이 모두 큐에서 제거될 때까지 반복
## 3-1. 맨 앞 번호로부터 K번째 사람이 나올 때까지 번호들을 순서대로 큐의 맨 앞에서 뒤로 이동
## 3-2. K번째 사람이 나올 경우 그대로 큐에서 제거 후 요세푸스 순열에 입력
## 4. 요세푸스 순열을 출력

from collections import deque

N, K = map(int, input().split())
numbers = deque(range(1, N + 1))
josephus = []

while numbers:
    cnt = 1
    while cnt < K:
        n = numbers.popleft()
        numbers.append(n)
        cnt += 1
    josephus.append(numbers.popleft())

print("<", end='')
for i, j in enumerate(josephus):
    if i == len(josephus) - 1:
        print(j, end='>')
    else:
        print(j, end=', ')
