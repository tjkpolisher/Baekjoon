# 16953: A → B
# 알고리즘 분류: 그래프 이론/그리디 알고리즘/그래프 탐색/너비 우선 탐색

# 1. 두 정수 A, B 입력 (1 ≤ A < B ≤ 10^9)
# 2. 두 가지 연산 정의
# 2-1. 수를 2로 나누기
# 2-2. 마지막 자릿수에 1이 붙은 연산을 역으로 (x - 1) // 10
# 3. B에서 시작해 위의 두 가지 연산을 실행하면서 횟수 카운팅
# 4-1. A에 도달했을 경우, 연산 횟수에 1을 더해 출력
# 4-2. 도달할 수 없는 경우 -1을 출력

import sys
input = sys.stdin.readline

A, B = map(int, input().split())
cnt = 0
tmp = B

while tmp > A:
    if tmp % 10 == 1:
        tmp = (tmp - 1) // 10
        cnt += 1
    elif tmp % 2 == 0:
        tmp //= 2
        cnt += 1
    else:
        print(-1)
        sys.exit()

if tmp == A:
    print(cnt + 1)
else:
    print(-1)
