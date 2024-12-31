# 11597: Excellence
# 특이사항: 다국어(영어)
# 출처: ICPC 2015 Pacific Northwest Region Programming Contest Division 1 E번
# 알고리즘 분류: 그리디 알고리즘/구현

# 1. 학생 수 n 입력 (1 ≤ n ≤ 10^5, n은 짝수)
# 2. n줄에 걸쳐 i번째 학생의 레이팅 s_i 입력 (1 ≤ s_i ≤ 10^6)
# 3. 입력받은 레이팅을 오름차순으로 정렬
# 4. 가장 작은 값과 가장 큰 값을 짝지어 팀을 구성 후 레이팅의 합을 리스트에 저장
# 5. 저장된 리스트의 최소값을 X로 출력

import sys
input = sys.stdin.readline

n = int(input())
ratings = []
for _ in range(n):
    ratings.append(int(input()))

ratings.sort()

min_team_ratings = []
for i in range(n // 2):
    min_team_ratings.append(ratings[i] + ratings[n - 1 - i])

print(min(min_team_ratings))
