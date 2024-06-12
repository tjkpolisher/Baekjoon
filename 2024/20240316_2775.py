# 2775: 부녀회장이 될테야
# 특이사항: 시간 제한 0.5초(추가 시간 없음)
# 유의사항: 점화식의 1항에 해당하는 호, 즉 0층의 i호에는 i명이 살고 있음.
# 알고리즘 분류: 수학/구현/다이나믹 프로그래밍

# 1. Test case의 개수 T 입력
# 2. [반복문]각 케이스마다 입력으로 첫 번째 줄에 층수 k, 두 번째 줄에 호수 n 입력
# 2-1. 점화식: a층의 b호에 살려면 자신의 아래 (a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 함
# 2-2. 이 점화식을 만족하는 k층 n호에 몇 명이 살고 있는지 출력.

T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    floor0 = list(range(1, n + 1))
    for i in range(k):
        for j in range(1, n):
            floor0[j] += floor0[j - 1]
    print(floor0[-1])
