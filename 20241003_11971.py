# 11971: 속도 위반
# 특이사항: 다국어(영어)(한국어 번역)
# 출처: USA Computing Olympiad(USACO) December 2015 Contest Bronze 2번
# 알고리즘 분류: 구현

# 1. 도로의 구간 N, 연정이가 달린 도로 구간 M 입력
# [보충설명] 도로 N개의 총합은 100km.
# 2. N개의 줄에 걸쳐 각 구간의 길이 및 해당 구간에서의 제한 속도 입력
# 3. M개의 줄에 걸쳐 연정이가 달린 구간의 길이와 해당 구간의 속도 입력
# 4. 속도 위반 최대값(주어진 구간의 속도 대비 초과한 속도)을 0으로 초기화
# 5. 도로 구간과 연정이의 구간에 기반해 1km ~ 100km까지의 구간 별 속도를 딕셔너리로 구성
# 6. 현재 거리를 키(key) 삼아서 1km씩 올리면서 도로 구간, 연정이의 구간 딕셔너리와 각각 비교
# 6-1. 초과했을 경우 속도 위반 최대값 갱신
# 7. 속도 위반 최대값 출력

N, M = map(int, input().split())
road = {}
rider = {}

interval_orig = 1
for _ in range(N):
    interval, speed = map(int, input().split())
    for i in range(interval_orig, interval_orig + interval):
        road[i] = speed
    interval_orig += interval
interval_orig = 1
for _ in range(M):
    interval, speed = map(int, input().split())
    for i in range(interval_orig, interval_orig + interval):
        rider[i] = speed
    interval_orig += interval

over = 0  # 속도 위반한 최대값
for d in range(1, 101):
    # 1km ~ 100km까지 속도 측정
    diff = max(rider[d] - road[d], 0)
    over = max(diff, over)

print(over)
