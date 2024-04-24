# 1764: 듣보잡
# 알고리즘 분류: 자료 구조/해시를 사용한 집합과 맵/정렬/문자열

# 1. 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M 입력(둘 다 500,000 이하의 자연수)
# 2. N개의 줄에 걸쳐 듣도 못한 사람의 이름 입력
# 3. M개의 줄에 걸쳐 보도 못한 사람의 이름 입력
# 4. 듣도 못한 사람의 집합과 보도 못한 사람의 집합의 교집합 연산
# 5. 듣보잡의 수와 그 명단을 이름 순으로 정렬해 출력

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
never_heard = set()  # 듣도 못한 사람
never_seen = set()  # 보도 못한 사람

for _ in range(N):
    never_heard.add(input().rstrip())
for _ in range(M):
    never_seen.add(input().rstrip())

# 교집합 연산
cross = never_heard.intersection(never_seen)
# 이름 순으로 정렬
cross = sorted(list(cross))
print(len(cross))
for c in cross:
    print(c)
