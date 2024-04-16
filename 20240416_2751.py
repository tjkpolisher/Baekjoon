# 2751: 수 정렬하기 2
# 알고리즘 분류: 정렬

# 1. 수의 개수 N 입력 (1 ≤ N ≤ 1,000,000)
# 2. N개의 줄에 걸쳐 수 입력
# 3. 리스트를 오름차순으로 정렬
# 4. 정렬 결과를 한 줄에 하나씩 출력

import sys
input = sys.stdin.readline

N = int(input())
num_list = []
for _ in range(N):
    num_list.append(int(input()))

num_list.sort()
for n in num_list:
    print(n)
