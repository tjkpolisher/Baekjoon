# 2358: 평행선
# 알고리즘 분류: 자료 구조/정렬/해시를 사용한 집합과 맵

# 1. n 입력 (1 ≤ n ≤ 100,000)
# 2. n개의 줄에 걸쳐 각 점의 좌표 입력(동일한 점의 좌표 중복 입력 가능하지만, 서로 다른 점으로 간주)
# 3. 해시 테이블 1에 x좌표를 키로 하는 리스트를 값으로 할당해, y좌표를 리스트에 입력
# 4. 같은 방식으로 해시 테이블 2에 y좌표를 키로, x좌표를 그 키의 리스트로 입력
# 5. 두 해시 테이블의 각 키에 대해 값의 길이를 더해서 출력

import sys
input = sys.stdin.readline

n = int(input())
dict1 = {}
dict2 = {}

for _ in range(n):
    x, y = map(int, input().split())

    if x not in dict1:
        dict1[x] = [y]
    else:
        dict1[x].append(y)
    if y not in dict2:
        dict2[y] = [x]
    else:
        dict2[y].append(x)

cnt = 0
for key in dict1:
    if len(dict1[key]) >= 2:
        cnt += 1
for key in dict2:
    if len(dict2[key]) >= 2:
        cnt += 1

print(cnt)
