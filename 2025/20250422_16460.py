# 16460: Cupid
# 특이사항: 다국어(영어)
# 출처: 제5회 한양대학교 프로그래밍 경시대회 Beginner Division B번
# 알고리즘 분류: 구현/문자열/정렬

# 1. 프리미엄 유저의 이름, 성적 취향, 최대 허용 거리 입력
# 2. 사람의 수 N 입력
# 3. N줄에 걸쳐 입력을 받으면서 다음 조건을 만족하는지 체크
# 3-1. 성적 취향이 일치하는지 확인
# 3-2. 최대 허용 거리 이내에 있는지 확인
# 3-3. 3-1과 3-2를 허용했을 경우, 정답 리스트에 이름을 추가
# 4. 리스트가 비었으면 "No one yet"을, 그렇지 않으면 사전 순서대로 이름을 한 줄에 하나씩 출력

import sys
input = sys.stdin.readline

p_user_info = list(input().rstrip().split())
preference = list(p_user_info[1])
max_distance = int(p_user_info[2])

N = int(input())

ans = []

for _ in range(N):
    name, sex, distance = input().rstrip().split()
    distance = int(distance)

    if sex not in preference:  # 성적 취향 체크
        continue
    if distance > max_distance:  # 최대 거리 체크
        continue
    ans.append(name)

if not ans:
    print("No one yet")
else:
    ans.sort()  # 사전 순서대로 리스트 정렬
    for name in ans:
        print(name)
