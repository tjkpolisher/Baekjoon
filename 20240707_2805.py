# 2805: 나무 자르기
# 특이사항: 다국어(영어)(한국어 번역)
# 출처: Croatian Open Competition in Informatics(COCI) 2011/2012 Contest #5 2번

# 1. 나무의 수 N, 상근이가 집으로 가져가려고 하는 나무의 길이 M 입력
# [보충설명] 1 ≤ N ≤ 1,000,000, 1 ≤ M ≤ 2,000,000,000
# 2. 나무의 높이가 공백으로 입력(나무의 높이의 합은 항상 M보다 크거나 같음)
# 3. 시작점을 0, 끝점을 가장 높은 나무의 높이로 설정한 뒤 이진 탐색 시작
# 4. 나무의 총 길이가 M보다 작으면 끝점을 이동, 그렇지 않으면 시작점 이동 및 높이 갱신
# 5. 길이 출력

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
heights = list(map(int, input().rstrip().split()))  # 이 부분을 collections의 Counter로 바꾸면 속도 상승 가능

start = 0
end = max(heights)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for h in heights:
        if h > mid:
            total += h - mid

    if total < M:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
