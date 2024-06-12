# 1158: 요세푸스 문제

## 1. N, K 입력
## 2. 1번부터 N번까지의 수를 담은 큐 생성
## 3. [반복문]
## 3-1. 맨 앞 사람부터 K-1번째 사람을 큐의 뒤로 이동
## 3-2. K번째 사람을 큐에서 제거 후 요세푸스 순열에 입력 
## 4. 주어진 형식에 맞게 요세푸스 순열 출력

from collections import deque
N, K = map(int, input().split())
d = deque(range(1, N + 1))
josephus = []
while d:
    cnt = 1
    while cnt < K:
        i = d.popleft()
        d.append(i)
        cnt += 1
    josephus.append(d.popleft())

print("<", end='')
for i, j in enumerate(josephus):
    if i == len(josephus) - 1:
        print(f"{j}>")
    else:
        print(j, end=', ')
