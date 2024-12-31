# 11659: 구간 합 구하기 4
# 알고리즘 분류: 누적 합

# 1. 수의 개수 N과 합을 구해야 하는 횟수 M 입력 (1 ≤ N ≤ 100,000, 1 ≤ M ≤ 100,000)
# 2. N개의 수 입력 (수는 1000 이하의 자연수)
# 3. 누적 합 리스트를 [0]으로 초기화
# 4. N개의 수를 저장한 리스트를 순회하면서 i번째 원소까지의 합을 누적 합 리스트에 저장
# 5. M개의 줄에 걸쳐 각각 합을 구해야 하는 구간 i와 j 입력 (1 ≤ i ≤ j ≤ N)
# 6. 누적 합 리스트에서 j번째 원소 - (i - 1)번째 원소를 계산 후 출력

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
number_list = list(map(int, input().split()))
prefix_sum = [0]

temp = 0
for n in number_list:
    temp += n
    prefix_sum.append(temp)

for _ in range(M):
    i, j = map(int, input().split())
    print(prefix_sum[j] - prefix_sum[i - 1])
