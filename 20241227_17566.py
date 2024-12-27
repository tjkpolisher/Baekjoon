# 17566: Bus Logic
# 특이사항: 다국어(영어)
# 출처: UKIEPC 2018 B번
# 알고리즘 분류: 브루트포스 알고리즘/비트마스킹

# 1. 출발점 m, 버스의 대수 b, 정류장의 개수 s 입력(1 ≤ m ≤ s ≤ 50, 1 ≤ b ≤ 50)
# 2. 편의상 m -= 1
# 3. b줄에 걸쳐 버스 노선을 뜻하는 길이 s의 문자열 입력(1은 정차하는 정류장을, 0은 지나치는 정류장을 의미)
# 4. 입력받은 문자열 중 m번째 인덱스의 원소가 1인지 판단
# 4-1. 해당되지 않으면 패스
# 4-2. 해당되면 1이 위치한 인덱스를 집합에 기록
# 5. 집합의 크기 출력

import sys
input = sys.stdin.readline

m, b, s = map(int, input().split())
m -= 1

bus_routes = [list(input().rstrip()) for _ in range(b)]

stops = set()

for route in bus_routes:
    if route[m] == '1':
        for i in range(s):
            if route[i] == '1' and i != m:
                stops.add(i)

print(len(stops))
