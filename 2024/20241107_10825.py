# 10825: 국영수
# 알고리즘 분류: 정렬

# 1. 도현이네 반 학생의 수 N 입력 (1 ≤ N ≤ 100,000)
# 2. N개의 줄에 걸쳐 각 학생의 이름, 국어, 영어, 수학 점수 입력 (점수는 1 이상 100 이하의 자연수)
# 2-1. 입력받은 목록을 리스트로 묶은 뒤, 전체 목록을 저장하는 별도의 리스트에 append
# 3. 리스트를 정렬(국어 내림차순 - 영어 오름차순 - 수학 내림차순 - 이름 오름차순 순서대로)
# 4. 정렬된 리스트의 이름 출력

import sys
input = sys.stdin.readline

N = int(input())
total_list = []
for _ in range(N):
    name, score1, score2, score3 = input().rstrip().split()
    score1 = int(score1)
    score2 = int(score2)
    score3 = int(score3)
    total_list.append([name, score1, score2, score3])

total_list.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
for t in total_list:
    print(t[0])
