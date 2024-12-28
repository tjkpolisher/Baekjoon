# 3699: 주차 빌딩
# 특이사항: 다국어(영어)(한국어 번역)
# 출처: ICPC NWERC 2007 I번
# 알고리즘 분류: 수학/구현

# 1. 테스트 케이스의 개수 입력(최대 100개)
# 2. 주차 빌딩의 높이 h, 컨베이어 벨트의 길이 l 입력 (1 ≤ h ≤ 50, 2 ≤ l ≤ 50)
# 3. h개의 줄에 걸쳐 각각 l개씩 정수를 입력
# [보충설명] i번째 줄의 j번째 숫자는 i번 층의 j번 위치에 있는 차의 정보를 의미. -1은 빈 칸이라는 뜻.
# 4. 입력받은 정수 별로 현재의 층 수와 차가 주차된 위치를 힙에 저장
# 5. 입력이 끝난 뒤 힙에서 가장 작은 수부터 인덱스를 꺼냄
# 6. 꺼낸 인덱스를 기준으로 층 수 * 10 * 2 + min(위치 인덱스, l - 위치 인덱스) * 5를 시간에 더함
# 7. 이후 해당 층수의 컨베이어 벨트 인덱스 기준을 현재 꺼낸 차량의 인덱스로 변경
# 8. 시간 출력

import sys
from heapq import heappush, heappop
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    h, l = map(int, input().split())  # 빌딩 높이, 컨베이어 벨트 길이
    t = 0  # 차를 찾는데 걸리는 총 시간
    heap = []

    for i in range(h):
        for j, car in enumerate(map(int, input().split())):
            if car == -1:
                continue
            heappush(heap, (car, i, j))

    conveyer_loc = {i: 0 for i in range(h)}  # 컨베이어 벨트의 위치(초기값 0)
    while heap:
        car, floor, loc = heappop(heap)
        t += (floor * 10 * 2 + min(abs(loc - conveyer_loc[floor]), l - abs(loc - conveyer_loc[floor])) * 5)
        conveyer_loc[floor] = loc
    print(t)
