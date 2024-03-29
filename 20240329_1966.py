# 1966: 프린터 큐
# 특이사항: 다국어(영어)(한국어 번역)
# 알고리즘 분류: 구현/자료 구조/시뮬레이션/큐

# 1. 테스트 케이스의 수 t 입력
# 2. [반복문]
# 2-1. 문서의 개수 N, 알고자 하는 문서가 큐의 몇 번째에 놓여 있는지를 나타내는 M 입력(맨 왼쪽이 0번째)
# 2-2. 문서의 중요도를 나타내는 정수 N개 입력(중요도는 중복 가능)
# 2-3. 큐에서 pop한 원소가 가장 높은 중요도가 아닐 경우 맨 뒤로 append
# 2-4. 현재 가장 높은 중요도일 경우 인쇄 후 cnt + 1
# 2-5. 중요도 M의 문서가 인쇄될 때 루프 종료 후 cnt 출력

from collections import deque

t = int(input())
for _ in range(t):
    N, M = map(int, input().split())
    priority = list(map(int, input().split()))
    priority = deque([(i, idx) for idx, i in enumerate(priority)])

    cnt = 0
    while True:
        if priority[0][0] == max(priority, key=lambda x: x[0])[0]:
            cnt += 1
            if priority[0][1] == M:
                print(cnt)
                break
            else:
                priority.popleft()
        else:
            priority.append(priority.popleft())
