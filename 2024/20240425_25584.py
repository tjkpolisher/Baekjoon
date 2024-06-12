# 25584: 근무 지옥에 빠진 푸앙이 (Large)
# 출처: 2022 중앙대학교 프로그래밍 경진대회(CPC) Division 1 A번
# 알고리즘 분류: 구현/자료 구조/문자열/해시를 사용한 집합과 맵

# 1. 주의 개수 N 입력 (1 ≤ N ≤ 5,000)
# 2. 둘째 줄부터 근무표 입력 (각 주는 4개의 줄로 구성)
# [보충설명] 첫째 줄은 0800~1200, 둘째 줄은 1200~1800, 셋째 줄은 1800~2200, 넷째 줄은 2200~0800까지 근무하는 인원 이름
# 단, '-'는 근무자가 없음을 의미.
# 각 줄은 요일별로 그 시간대에 누가 근무하는지를 의미.
# 3. 입력받은 줄이 몇 번째 줄이었는지에 따라 근무자 이름과 근무시간을 저장한 해시 테이블에 근무시간을 더함
# 4. 모든 입력이 끝났을 때 근무 시간의 최대, 최소값을 비교해 12시간 이하인지 판단
# 5. 결과에 따라 "Yes", "No" 출력(단, 아무도 근무하지 않으면 공평한 것으로 간주)

import sys
input = sys.stdin.readline

N = int(input())
work_table = dict()
work_time = [4, 6, 4, 10]
for _ in range(N):
    for i in range(4):
        in_service = list(input().rstrip().split())
        for s in in_service:
            if s != '-':
                if s not in work_table:
                    work_table[s] = work_time[i]
                else:
                    work_table[s] += work_time[i]

# 근무 시간이 없는 경우도 공평하다고 취급
if not work_table:
    print("Yes")
else:
    times = list(work_table.values())
    if max(times) - min(times) > 12:
        print("No")
    else:
        print("Yes")
