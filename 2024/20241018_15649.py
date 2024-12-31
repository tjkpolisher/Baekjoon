# 15649: N과 M (1)
# 알고리즘 분류: 백트래킹

# 1. 자연수 N과 M 입력
# 2. 1부터 N까지의 자연수를 담은 리스트 생성
# 3. permutations를 이용해 중복을 허용하지 않는 수열을 출력
# 4. 사전 순으로 증가하는 순서로 출력

from itertools import permutations

N, M = map(int, input().split())
N_list = list(range(1, N + 1))
p_list = list(permutations(N_list, M))
for p in p_list:
    print(*p)
