# 25825: 빠른 무작위 메시지 전달
# 알고리즘 분류: 브루트포스 알고리즘/백트래킹

# 1. 열두 개의 줄에 걸쳐 메시지를 전달하는 데 걸리는 시간 입력
# [보충설명] i번째 줄의 j번째 숫자는 학생 i가 학생 j에게 메시지를 전달하는 데 걸린 시간
# 2. 입력받은 정보를 바탕으로 12 x 12 2차원 리스트 생성
# 3. 친구 집단을 앞에서부터 두 명 씩 묶어 6개의 그룹 생성
# 4. 각 친구 그룹의 순서를 순열로 생성
# 5. 어느 학생에게 먼저 전달할지를 2진 마스크로 나타내어 0과 1의 경우를 모두 고려
# 6. 아래 조건에 맞게 연산을 한 뒤 cost에 더하고 마지막으로 전파받은 학생 갱신
# 6-1. 마스크의 첫 비트가 1일 경우 그룹의 두 번째 학생 -> 첫 번째 학생 순 전파
# 6-2. 마스크의 첫 비트가 0일 경우 그룹의 첫 번째 학생 -> 두 번째 학생 순 전파
# 7. 이후 나머지 그룹에 대해서도 6-1과 6-2의 조건에 맞게 비용 계산
# 8. 계산이 끝난 뒤 최소 비용을 갱신
# 9. 최소 비용 출력

import sys
from itertools import permutations
input = sys.stdin.readline

times = [list(map(int, input().split())) for _ in range(12)]
groups = []
for i in range(6):
    groups.append((2 * i, 2 * i + 1))

min_cost = int(1e9)
for perm in permutations(groups):
    for mask in range(1 << 6):
        cost = 0
        if mask & 1:
            cost += times[perm[0][1]][perm[0][0]]
            last = perm[0][0]
        else:
            cost += times[perm[0][0]][perm[0][1]]
            last = perm[0][1]

        valid = True
        for i in range(1, 6):
            group = perm[i]
            if mask & (1 << i):
                cost += times[last][group[1]] + times[group[1]][group[0]]
                last = group[0]
            else:
                cost += times[last][group[0]] + times[group[0]][group[1]]
                last = group[1]
        min_cost = min(min_cost, cost)

print(min_cost)
