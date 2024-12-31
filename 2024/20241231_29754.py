# 29754: 세상에는 많은 유튜버가 있고, 그중에서 버츄얼 유튜버도 존재한다
# 특이사항: 다국어(영어)(한국어 번역)
# 출처: 2023 국민대학교 알고리즘 콘테스트 D번/2023 중앙대학교 CPC
# 알고리즘 분류: 구현/자료 구조/문자열/해시를 사용한 집합과 맵

# 1. 방송의 수 N, 형식이가 방송을 마지막으로 본 날짜 M 입력
# [보충설명] 1 ≤ N ≤ 36400, 7 ≤ M ≤ 364, M은 7의 배수
# 2. N줄에 걸쳐 name day hh:mm hh:mm 형식으로 버튜버 이름/방송 날짜/시작 시각/종료 시각 입력
# [보충설명] 이름은 최대 20자의 영어 소문자, 버튜버끼리의 이름은 중복되지 않음. 최대 100명.
# [보충설명] 방송은 한 번에 최대 23시간 59분 진행. 밤을 새는 경우는 없고 방송 시작 날짜와 종료 날짜는 항상 동일.
# [보충설명] 방송은 하루에 최대 한 번 진행.
# 3. 버튜버 이름과 그 방송 시간을 계산하여 방송 횟수와 함께 딕셔너리에 저장
# 3-1. 단, 1주일 단위로 방송 시간과 방송 횟수를 별도로 저장
# 4. 모두 입력받은 후 방송 횟수가 1주일에 5회 이상, 매주 60시간 이상 라이브를 한 버튜버의 이름 저장
# [보충설명] 매주 5회/60시간 조건을 모두 충족하는지를 검사
# 5. 저장한 이름을 사전 순으로 정렬 후 출력(단, 저장된 이름이 없다면 -1을 출력)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
streaming_table = {}
real_Vtuber = []
weeks = M // 7

for _ in range(N):
    name, day, start, end = input().rstrip().split()
    day = int(day)
    week_idx = (day - 1) // 7
    sh, sm = map(int, start.split(':'))
    eh, em = map(int, end.split(':'))

    streaming_time = (eh * 60 + em) - (sh * 60 + sm)
    streaming_time *= 60

    if name not in streaming_table:
        streaming_table[name] = {
            "time": [0] * weeks,
            "day": [0] * weeks
        }

    streaming_table[name]["time"][week_idx] += streaming_time
    streaming_table[name]["day"][week_idx] += 1

for name, value in streaming_table.items():
    stream_time, stream_day = value["time"], value["day"]

    is_real = True
    for i in range(weeks):
        if stream_time[i] < 60 * 3600 or stream_day[i] < 5:
            is_real = False
            break

    if is_real:
        real_Vtuber.append(name)

if not real_Vtuber:
    print(-1)
else:
    real_Vtuber.sort()
    for Vtuber in real_Vtuber:
        print(Vtuber)
