# 11399: ATM
# 알고리즘 분류: 그리디 알고리즘/정렬

# 1. 사람의 수 N (1 ≤ N ≤ 1,000) 입력
# 2. 각 사람이 돈을 인출하는데 걸리는 시간 P_i 입력 (1 ≤ P_i ≤ 1,000)
# 3. P_i를 저장한 리스트를 오름차순으로 정렬
# 4. 리스트의 n번째 항까지의 합을 원소로 갖는 또다른 메모이제이션 리스트 생성
# 5. 메모이제이션 리스트의 합 출력

import sys
input = sys.stdin.readline

N = int(input())
p_list = list(map(int, input().split()))
p_list.sort()
mem = []
sum_n = 0
for p_i in p_list:
    p = p_i + sum_n
    mem.append(p)
    sum_n += p_i
print(sum(mem))
