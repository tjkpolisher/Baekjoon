# 3020: 개똥벌레
# 특이사항: 다국어(영어)(한국어 번역)
# 출처: Croatian Highschool Competitions in Informatics 2007 3번
# 알고리즘 분류: 이분 탐색/누적 합

# 1. 동굴의 길이 N, 높이 H 입력 (2 ≤ N ≤ 200,000, 2 ≤ H ≤ 500,000, N은 짝수)
# 2. N개의 줄에 걸쳐 장애물의 크기 입력 (H보다 작은 양수)
# [보충설명] 첫 번째 장애물은 항상 바닥에서 자라는 석순, 그 다음에는 종유석과 석순이 번갈아가며 등장
# 3. 길이 H의 리스트에 모든 원소를 0으로 초기화
# 4. 석순의 시작점을 1로, 끝을 -1로 처리한 뒤 H의 리스트에 1과 -1의 합을 입력
# 5. 입력된 리스트의 누적합을 계산
# 6. 최소값과 그 인덱스들을 공백으로 구분해 출력

import sys
input = sys.stdin.readline

N, H = map(int, input().split())
hazards = {i: 0 for i in range(H)}
for i in range(1, N + 1):
    if i % 2 == 1:  # 첫번째 및 홀수 번째 장애물은 석순
        hazards[0] += 1
        hazards[int(input())] -= 1
    else:
        hazards[H - int(input())] += 1

array = list(hazards.values())
prefix = [array[0]]
for i in range(H - 1):
    prefix.append(prefix[i] + array[i + 1])

minimum_collision = min(prefix)  # 최소 충돌 횟수
num_lane = 0  # 최소 충돌 구간의 개수
for i in range(H):
    if prefix[i] == minimum_collision:
        num_lane += 1

print(minimum_collision, num_lane)
