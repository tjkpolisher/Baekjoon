# 15761: Lemonade Line
# 특이사항: 다국어(영어)
# 출처: USA Computing Olympiad(USACO) 2018 US Open Contest Silver 2번
# 알고리즘 분류: 그리디 알고리즘/정렬

# 1. 레모네이드를 먹일 소(cow...)의 수 N 입력 (1 ≤ N ≤ 100,000)
# 2. N개의 줄에 걸쳐 w_i 입력 (0 ≤ w_i ≤ 10^9) (해당 소가 최대 몇 번째까지 기다릴 수 있는지를 의미)
# 3. w_i의 리스트를 내림차순으로 정렬
# 4. 리스트를 순회하면서 현재 줄에 있는 소의 수가 w_i 이하인 경우에만 소의 수에 1을 더함
# 5. 소의 수 출력

N = int(input())
cows_waiting = list(map(int, input().split()))
cows_waiting.sort(reverse=True)

in_line = 0
for i in range(N):
    if in_line <= cows_waiting[i]:
        in_line += 1

print(in_line)
