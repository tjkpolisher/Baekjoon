# 5602: 問題1
# 특이사항: 다국어(일본어)

# 1. 학생의 수 n, 여행 후보지의 수 m 입력
# 2. [반복문]
# 2-1. n줄에 걸쳐 설문조사 결과를 담은 m개의 정수 입력(1은 찬성, 0은 반대)
# 2-2. 정수를 리스트로 입력받아 1이 나올 때마다 딕셔너리의 값에 1을 더함
# 3. 가장 투표수가 많은 순서대로 딕셔너리의 키를 내림차순으로 정렬 후 출력

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
d = {i: 0 for i in range(1, m + 1)}
for _ in range(n):
    result = list(map(int, input().split()))
    for j in range(m):
        d[j + 1] += result[j]

d_items = d.items()
d_items = sorted(d_items, reverse=True, key=lambda x: x[1])
for k in d_items:
    print(k[0], end=' ')
