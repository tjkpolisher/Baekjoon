# 25497: 기술 연계마스터 임스
# 알고리즘 분류: 구현/자료 구조/스택

# 1. 총 기술 사용 횟수 N 입력 (1 ≤ N ≤ 200,000)
# 2. 임스가 사용할 N개의 기술 입력(공백 없이 주어짐)
# [보충설명]: 1~9는 연계 없이 단독 사용할 수 있는 기술, L은 R의 사전 기술, S은 K의 사전 기술
# 3-1. 단독 사용 가능한 기술이면 그대로 팝 후 카운터에 1을 더함
# 3-2. 문자로 표기된 기술이면 사전 기술은 다른 스택에 넣고 있다가 본 기술이 등장하면 pop 후 카운터에 1을 더함
# 3-3. 단, 각각의 사전 기술 스택이 빈 상태로 R 또는 K가 팝된 경우 그대로 반복문 종료
# 4. 카운터 출력

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
skills = deque(input().rstrip())
cnt = 0
stack_L = []  # 사전 기술 L을 담을 스택
stack_S = []  # 사전 기술 S를 담을 스택

for i in range(N):
    p = skills.popleft()
    # L 또는 S인 경우 본 기술이 나오기 전까지 별도의 스택에 저장
    if p == 'L':
        stack_L.append(p)
    elif p == 'S':
        stack_S.append(p)
    # R인 경우 stack_L에 L이 있는 경우 스택에서 L을 빼고 카운터 증가
    elif p == 'R':
        if not stack_L:
            break
        else:
            stack_L.pop()
            cnt += 1
    # K인 경우 stack_S에 S이 있는 경우 스택에서 S을 빼고 카운터 증가
    elif p == 'K':
        if not stack_S:
            break
        else:
            stack_S.pop()
            cnt += 1
    # 나머지 일반 기술들의 경우 그대로 카운터 증가
    else:
        cnt += 1

print(cnt)
