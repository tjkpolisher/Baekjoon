# 1235: 학생 번호
# 알고리즘 분류: 구현/문자열/브루트포스 알고리즘

# 1. 학생의 수 N (2 ≤ N ≤ 1,000)
# 2. N개의 줄에 걸쳐 각 학생의 번호 입력 (길이는 100 이하)
# 3. 전체 학생의 번호를 역순으로 정렬하고, 길이 1부터 시작해 맨 앞에서부터 슬라이스
# 4. 슬라이스된 번호의 문자열을 집합에 넣어서 그 개수가 N보다 작으면 길이를 1씩 증가
# 5. 집합의 크기가 N과 같아지면 루프를 종료 후 자릿수 출력

import sys
input = sys.stdin.readline

N = int(input())
number_list = []
for _ in range(N):
    number_list.append(input().rstrip()[::-1])

length = len(number_list[0])  # 모든 학생의 번호의 길이는 동일
for i in range(1, length):
    sliced_set = set()

    for j in range(N):
        sliced_set.add(number_list[j][:i])

    if len(sliced_set) == N:
        ans = i
        break
else:
    ans = length

print(ans)
