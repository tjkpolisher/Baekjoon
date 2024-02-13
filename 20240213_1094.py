# 1094: 막대기
# 알고리즘 분류: 수학/비트마스킹

## 1. 원하는 막대의 길이 X 입력
## 2. 가지고 있는 막대의 길이 모두 더하기
## 2-1. 만약 합이 X보다 크다면 아래 과정 반복
## 2-1-1. 가지고 있는 막대 중 가장 짧은 것을 반으로 나눅;
## 2-1-2. 위에서 자른 막대의 절반 중 하나를 버리고 남은 막대의 길이의 합이 X보다 크면, 위에서 자른 막대의 절반 중 하나를 버림
## 2-1-3. 남은 막대를 풀로 붙여서 Xcm를 만들기
## 3. 막대의 개수 출력

from collections import deque
X = int(input())
sticks = deque([64])
shortest = 64
while shortest >= 1:
    shortest /= 2
    sticks.append(shortest)
    if sticks[0] > X:
        sticks.popleft()

cnt = 0
ans = 0
while ans < X:
    stick = sticks.popleft()
    if ans + stick <= X:
        ans += stick
        cnt += 1
print(cnt)
