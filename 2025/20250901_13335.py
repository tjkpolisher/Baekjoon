# 13335: 트럭
# 특이사항: 다국어(영어)(한국어 번역)
# 출처: ICPC Daejeon Nationalwide Internet Competition 2016 L번
# 알고리즘 분류: 구현/자료 구조/시뮬레이션/큐

# 1. 트럭의 수 n, 다리의 단위 길이 w, 최대 하중 L 입력
# [보충사항] 1 ≤ n ≤ 1,000, 1 ≤ w ≤ 100, 10 ≤ L ≤ 1,000
# 2. n개의 정수 a_1, a_2, ⋯ , a_n (1 ≤ a_i ≤ 10) 입력(a_i는 i번째 트럭의 무게)
# 3. 길이 w의 덱 생성(모든 원소는 0으로 초기화)
# 4. 현재의 총 하중 변수와 최단 시간 변수를 0으로 초기화
# 5. 첫 번째 트럭의 무게부터 덱에 넣고, 덱의 맨 뒤 원소를 빼는 연산을 진행
# 5-1. 이때, 더해지는 무게를 총 하중에 더하고 빠지는 무게를 총 하중에서 빼기
# 5-2. 단, 넣을 무게가 총 하중을 초과할 경우 총 하중보다 작아질 때까지 5-1의 연산 반복
# 5-3. 5-1 연산이 끝날 때마다 최단 시간 변수에 1을 추가
# 6. 모든 트럭이 다리를 건너면 최단시간 변수 출력

import sys
from collections import deque
input = sys.stdin.readline

n, w, L = map(int, input().split())
trucks = deque(map(int, input().split()))
bridge = deque([0] * w)
total_weight = 0
time = 0


def step(q, w_in):
    # 매 초 다리 위의 트럭 무게를 연산하는 함수
    global total_weight, time
    q.appendleft(w_in)
    w_out = q.pop()
    total_weight += w_in
    total_weight -= w_out
    time += 1


while trucks:
    if total_weight + trucks[0] - bridge[-1] <= L:
        step(bridge, trucks.popleft())
    else:
        step(bridge, 0)

if any(bridge):
    # 트럭이 한 대라도 다리 위에 남아있을 경우
    while any(bridge):
        step(bridge, 0)

print(time)
