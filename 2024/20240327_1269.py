# 1269: 대칭 차집합
# 알고리즘 분류: 자료 구조/해시를 사용한 집합과 맵/트리를 사용한 집합과 맵

# 1. 두 집합 A와 B의 원소의 개수 입력
# 2. A의 원소들 입력
# 3. B의 원소들 입력
# 4. 두 집합에 대하여 두 차집합 A-B와 B-A 연산
# 5. A-B와 B-A의 합집합 연산
# 6. 5에서 구한 대칭 차집합의 원소 개수 출력

import sys
input = sys.stdin.readline

n_A, n_B = map(int, input().rstrip().split())
A = set(map(int, input().rstrip().split()))
B = set(map(int, input().rstrip().split()))
sub1 = A - B
sub2 = B - A
ans = sub1.union(sub2)
print(len(ans))
