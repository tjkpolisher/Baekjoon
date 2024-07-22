# 25496: 장신구 명장 임스
# 출처: 2022 ICPC Sinchon Summer Algorithm Camp Contest 초급 C번
# 알고리즘 분류: 그리디 알고리즘/정렬

# 1. 현재 쌓인 피로도 P와 만들 수 있는 장신구의 개수 N 입력  (1 ≤ P ≤ 200, 1 ≤ N ≤ 1000)
# 2. 피로도를 나타내는 N개의 정수 A_i 입력 후 리스트에 저장 (1 ≤ A_i ≤ 200)
# 3. 피로도 리스트를 오름차순으로 정렬 후 큐로 변환
# 4. 큐에 저장된 요소를 하나씩 꺼내면서 P에 더하고 장신구 개수에 1을 더함
# 5. 어떤 요소를 더했을 때 P가 200 이상이 되거나 큐가 비어있으면 연산을 종료하고 지금까지의 장신구 개수 출력

import sys
from collections import deque
input = sys.stdin.readline

P, N = map(int, input().split())
A_array = list(map(int, input().split()))

n_items = 0
A_queue = deque(sorted(A_array))
while P < 200 and A_queue:
    A = A_queue.popleft()
    P += A
    n_items += 1

print(n_items)
