# 25593: 근무 지옥에 빠진 푸앙이 (Small)
# 특이사항: 아무도 근무하지 않을 경우, 근무표는 공평한 것으로 간주
# 각 날에는 4개의 시간대에 모두 근무자가 있거나 모두 근무자가 없음.
# 예를 들어, 12:00~18:00에만 근무자가 있는 날은 없음
# 알고리즘 분류: 구현/자료구조/문자열/해시를 사용한 집합과 맵

## 1. 주의 개수 N 입력 및 근무자별 근무 시간을 입력할 딕셔너리, 시간대별 근무 시간 딕셔너리 생성
## 2. 각 주마다 네 줄에 걸쳐 각 시간대 별 근무자 이름 입력(최대 100명, 없는 경우 '-'가 입력됨)
## 3. '-'를 제거한 값을 근무자별 근무 시간 딕셔너리에 넣을 키로 설정
## 4. 시간대별 근무 시간 딕셔너리를 참조해 딕셔너리의 키에 대한 값에 더해줌
## 5. 근무 시간 딕셔너리에 12시간보다 차이가 큰 값이 없으면 "Yes", 있으면 "No" 출력

N = int(input())
worker_time_table = {}
time_table = {0: 4, 1: 6, 2: 4, 3: 10}
is_fair = "Yes"
for _ in range(N):
    for t in range(4):
        workers = list(input().split())
        workers = [w for w in workers if w != '-']
        if not workers:
            break
        
        for w in workers:
            if w not in worker_time_table:
                worker_time_table[w] = time_table[t]
            else:
                worker_time_table[w] += time_table[t]
    
if worker_time_table:
    values = worker_time_table.values()
    max_time, min_time = max(values), min(values)
    if max_time - min_time > 12:
        is_fair = "No"

print(is_fair)
