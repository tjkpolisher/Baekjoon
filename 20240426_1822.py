# 1822: 차집합
# 알고리즘 분류: 자료 구조/정렬/해시를 사용한 집합과 맵/트리를 사용한 집합과 맵

# 1. 두 집합 A, B의 원소의 개수 입력 (1 ≤ n(A), n(B) ≤ 500,000)
# 2. 집합 A의 원소 입력
# 3. 집합 B의 원소 입력
# 4. 차집합 연산 A - B 수행 후 원소의 개수 출력

import sys
input = sys.stdin.readline

n_a, n_b = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))
sub = sorted(list(A - B))
print(len(sub))
if sub:
    print(*sub)
