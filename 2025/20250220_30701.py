# 30701: 돌아온 똥게임
# 출처: 2023 고려대학교 프로그래밍 경시대회 (KCPC) Div. 1 A번
# 알고리즘 분류: 그리디 알고리즘/정렬

# 1. 방의 수 N, 근호의 시작 전투력 D 입력 (1 ≤ N ≤ 100,000, 1 ≤ D ≤ 10^9)
# 2. N개의 줄에 걸쳐 방의 정보 A_i, 몬스터 또는 장비의 전투력 X_i 입력
# [보충설명] A_i는 1(몬스터가 있는 방) 또는 2(장비가 있는 방), 2 ≤ X_i ≤ 10^9
# 2-1. 몬스터 방과 장비 방의 정보를 각각 별도의 힙에 저장
# 3. 아래 방식으로 전투력을 연산하면서, 통과할 수 있으면 돌파한 방의 개수에 1을 더하기
# 3-1. 남은 장비 중 가장 낮은 전투력의 장비부터 사용해 전투력에 곱하기
# 3-2. 현재 전투력보다 전투력이 작은 몬스터들을 pop해서 전투력에 더하기
# 4. 최대로 돌파할 수 있는 방의 개수 출력

import sys
import heapq
input = sys.stdin.readline

N, D = map(int, input().split())

monsters = []
equipments = []

for _ in range(N):
    a, x = map(int, input().split())
    if a == 1:
        heapq.heappush(monsters, x)
    else:
        heapq.heappush(equipments, x)

cnt = len(equipments)  # 장비 방은 전투력과 무관하게 무조건 돌파 가능하므로 장비 방의 개수로 초기화

while monsters:
    while equipments and monsters[0] >= D:
        D *= heapq.heappop(equipments)
    if monsters[0] < D:
        cnt += 1
        D += heapq.heappop(monsters)
    else:
        break

print(cnt)
