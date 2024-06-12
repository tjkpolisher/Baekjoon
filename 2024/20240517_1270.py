# 1270: 전쟁 - 땅따먹기
# 알고리즘 분류: 구현/자료 구조/해시를 사용한 집합과 맵/보이어-무어 다수결 투표

# 1. 땅의 개수 n 입력 (n ≤ 200)
# 2. n개의 줄에 걸쳐 i번째 땅의 병사 수를 나타내는 Ti와 Ti개의 숫자 입력
# 3. 병사 수를 저장한 리스트를 순회하며, 번호를 키로 삼고 그 번호가 나타낸 횟수를 값으로 삼는 딕셔너리 생성
# 4-1. 딕셔너리의 값 중 어느 것도 Ti / 2보다 크지 않으면 지배되지 않음
# 4-2. 절반을 넘어선 번호가 땅을 지배한 나라의 번호
# 3. 땅이 지배되었다면 지배한 병사의 번호 출력, 아니라면 "SYJKGW"를 출력

import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    table = defaultdict(int)
    T = list(map(int, input().rstrip().split()))
    Ti = T[0]
    for i in range(1, Ti + 1):
        table[T[i]] += 1
    keys = list(table.keys())
    numbers = list(table.values())
    for i, n in enumerate(numbers):
        if n > (Ti / 2):
            print(keys[i])
            break
    else:
        print("SYJKGW")
