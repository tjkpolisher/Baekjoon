# 9872: Record Keeping
# 특이사항: 다국어(영어)
# 출처: USACO December 2013 Contest Bronze 1번
# 알고리즘 분류: 자료 구조/문자열/정렬/해시를 사용한 집합과 맵

# 1. 존이 기록한 시간의 개수 N 입력 (1 ≤ N ≤ 1000)
# 2. 한 줄에 세 마리의 소 이름을 정렬해 고유 그룹 리스트에 저장
# [보충설명] 한 번 등장한 그룹은 다시 등장할 수 있으나, 그룹 내에서의 순서는 변할 수 있음.
# 3-1. 그룹이 새로 등장하면 고유 그룹 리스트에 기록한 뒤 그룹과 그 등장 횟수를 함께 리스트에 저장
# 3-2. 기존에 등장한 그룹일 경우, 해당 그룹의 인덱스를 찾아 등장 횟수만 1회 올림
# 4. 그룹-등장 횟수 저장 리스트를 등장 횟수를 기준으로 내림차순으로 정렬
# 5. 최대 등장 횟수를 출력

import sys
input = sys.stdin.readline

N = int(input())
groups = []
distinct_group = []
for _ in range(N):
    group = sorted(list(input().rstrip().split()))
    if group not in distinct_group:
        groups.append([group, 1])
        distinct_group.append(group)
    else:
        groups[distinct_group.index(group)][1] += 1

groups.sort(key=lambda x: x[1], reverse=True)
print(groups[0][1])
