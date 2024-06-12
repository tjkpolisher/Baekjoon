# 1476: 날짜 계산
# 알고리즘 분류: 수학/브루트포스 알고리즘/정수론

# 1. E, S, M 입력 (1 ≤ E ≤ 15, 1 ≤ S ≤ 28, 1 ≤ M ≤ 19)
# 2. 각 자리에 1을 더하되, 각 숫자의 범위를 넘어가면 1로 돌아감
# 3. E, S, M으로 표시되는 가장 빠른 연도 출력

esm = list(map(int, input().split()))
calendar = [1, 1, 1]
ans = 1
while True:
    if calendar == esm:
        print(ans)
        break

    ans += 1
    for i in range(3):
        calendar[i] += 1

    if calendar[0] > 15:
        calendar[0] = 1
    if calendar[1] > 28:
        calendar[1] = 1
    if calendar[2] > 19:
        calendar[2] = 1
