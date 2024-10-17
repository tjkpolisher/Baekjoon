# 2110: 공유기 설치
# 특이사항: 다국어(영어)(한국어 번역)
# 출처: USA Computing Olympiad February 2005 Contest Gold 3번
# 알고리즘 분류: 이분 탐색/매개 변수 탐색

# 1. 집의 개수 N과 공유기의 개수 C 입력 (2 ≤ N ≤ 200,000, 2 ≤ C ≤ N)
# 2. N개의 줄에 걸쳐 집의 좌표를 나타내는 x_i 입력 후 리스트에 저장 (0 ≤ x_i ≤ 1,000,000,000)
# 3. 집의 좌표 리스트를 오름차순으로 정렬
# 4. 거리의 최소값과 최대값을 기준으로 이진 탐색 개시
# 4-1. 가장 인접한 두 공유기 사이의 거리를 mid로 설정(start + end // 2)
# 4-2. 현재의 mid값을 이용해 공유기 설치
# 4-3. C개 이상의 공유기를 설치할 수 있으면 거리 증가, 그렇지 않으면 거리 감소
# 5. 최적의 결과를 저장 뒤 출력

import sys
input = sys.stdin.readline

N, C = map(int, input().split())
houses = []
for _ in range(N):
    houses.append(int(input()))

houses.sort()

start = 1  # 최소 거리
end = houses[-1] - houses[0]  # 최대 거리
result = 0

while (start <= end):
    mid = (start + end) // 2
    value = houses[0]
    cnt = 1

    for i in range(1, N):
        if houses[i] >= value + mid:
            value = houses[i]
            cnt += 1
    if cnt >= C:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)
