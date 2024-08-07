# 18311: 왕복
# 알고리즘 분류: 구현

# 1. 코스 개수 N, 이동 거리 K 입력 (1 ≤ N ≤ 100,000) (K는 0 또는 왕복 거리보다 작은 양의 정수)
# 2. 1번부터 N번까지 각 코스의 길이가 공백으로 입력
# 3. 코스 길이 리스트에 코스 길이 리스트를 뒤집은 리스트를 더해 왕복 코스 리스트 생성
# 4. 코스 길이(왕복 코스)의 누적 합을 계산한 리스트 생성
# 5. 누적 합 리스트의 원소에 해당하는 코스 번호를 메겨 별도의 리스트로 생성
# 5-1. 단, N번 코스를 지난 후에는 왕복으로 돌아오므로 코스 번호를 1씩 줄여야 함
# 6. K가 누적 합 리스트의 어떤 원소보다 작을 경우(미만일 경우) 해당 인덱스의 코스 번호 출력

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
courses = list(map(int, input().split()))
courses = courses + courses[::-1]

distance = [0]
d = 0
for c in courses:
    d += c
    distance.append(d)

course_num = list(range(1, N + 1))
course_num = course_num + course_num[::-1]

ans = 1
for i in range(1, 2 * N):
    if distance[i - 1] <= K < distance[i]:
        ans = course_num[i - 1]
        break
print(ans)
