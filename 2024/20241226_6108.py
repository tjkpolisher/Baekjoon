# 6108: The Perfect Cow
# 특이사항: 다국어(영어)
# 출처: USACO March 2009 Contest Bronze 3번
# 알고리즘 분류: 구현/정렬

# 1. 정수 N 입력(2 ≤ N ≤ 99, N은 홀수)
# 2. N개의 줄에 걸쳐 뷰티 레이팅을 뜻하는 정수 R_ij들을 입력 (1 ≤ R_ij ≤ 1000)
# 3. 입력받은 뷰티 레이팅 정수 중 중간값을 별도로 저장
# 4. 모든 중간값을 입력받은 뒤, 그 중에서 중간값을 탐색하여 출력

import sys
input = sys.stdin.readline

N = int(input())
ratings = []
for _ in range(N):
    rating_now = sorted(list(map(int, input().split())))
    ratings.append(rating_now[N // 2])

ratings.sort()
print(ratings[N // 2])
