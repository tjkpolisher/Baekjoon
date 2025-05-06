# 1678: 기차
# 알고리즘 분류: 수학/정렬

# 1. 기차의 종류 수 T(< 30), 이 사장의 출발 시간 M(< 60), N(< 1,000,000,000) 입력
# 2. T개의 줄에 걸쳐 각 기차별로 기차의 번호와 그 기차가 0번 역에서 출발하는 시간을 분 단위로 입력
# [보충설명] 기차 번호는 길이 10 이하의 문자열. 각 줄의 끝은 -1. 출발 시간은 분 단위(< 60).
# 3. 기차 종류별로 출발 시각을 수집해 딕셔너리에 저장
# 4. 0번 역에서 출발하는 시간을 오름차순으로 정렬
# 5. 정렬된 리스트를 순회하면서 0번 역에서 탈 첫 번째 기차 인덱스 찾기
# 6. N역 이동 후 최종 인덱스를 계산 후 출력

import sys
input = sys.stdin.readline

T, M, N = map(int, input().split())
type_map = {}
offsets = []

for _ in range(T):
    train_id, *time = input().split()
    time.pop()  # 입력받은 값의 맨 마지막의 -1을 제거
    for t in time:
        type_map[int(t)] = train_id
        offsets.append(int(t))

offsets.sort()
K = len(offsets)

start_idx = 0
for i, t in enumerate(offsets):
    if t >= M:
        start_idx = i
        break
else:
    start_idx = 0

final_idx = (start_idx + (N - 1)) % K
print(type_map[offsets[final_idx]])
