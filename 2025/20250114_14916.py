# 14916: 거스름돈
# 출처: 2017 ERICA Programming Contest League B (초보) H번
# 알고리즘 분류: 수학/다이나믹 프로그래밍/그리디 알고리즘

# 1. 거스름돈 액수 n 입력 (1 ≤ n ≤ 100,000)
# 2. n을 5로 최대한 나누면서 개수를 cnt에 더함
# 3. 남은 n을 2로 최대한 빼면서 개수를 cnt에 더함
# 4-1. n이 0이 되면 동전의 최소 개수를 출력
# 4-2. n이 0보다 작으면 -1을 출력

n = int(input())
cnt = 0
i = 0

while True:
    if n % 5 == 0:
        cnt += n // 5
        break
    else:
        n -= 2
        cnt += 1

    if n < 0:
        break

if n < 0:
    print(-1)
else:
    print(cnt)
