# 10819: 차이를 최대로
# 알고리즘 분류: 브루트포스 알고리즘/백트래킹

# 1. 배열의 크기 N 입력(3 ≤ N ≤ 8)
# 2. N개의 수를 입력받아 배열 A를 생성 (-100 이상 100 이하)
# 3. 배열 A의 원소를 순서대로 정렬하는 순열을 생성
# 4. 각 순열에 대하여 |A[i] - A[i+1]|의 합을 구하고 최대값을 갱신
# 5. 최대값 출력

from itertools import permutations

N = int(input())
A = list(map(int, input().split()))

ans = 0
permutations_list = permutations(A)
for perm in permutations_list:
    tmp = 0
    for i in range(N - 1):
        tmp += abs(perm[i] - perm[i + 1])
    ans = max(ans, tmp)

print(ans)
