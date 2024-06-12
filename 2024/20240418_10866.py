# 10866: 덱
# 알고리즘 분류: 구현/자료 구조/덱

# 1. 명령의 수 N 입력 (1 ≤ N ≤ 10,000)
# 2. N개의 줄에 걸쳐 명령 입력(명령은 총 여덟 종류)
# 3. 출력 명령(size 명령어 등)이 나올 때마다 현재 덱에 들어있는 정수의 개수 출력

import sys
from collections import deque

N = int(input())
cnt = 0
q = deque()

for _ in range(N):
    cmd = sys.stdin.readline().rstrip()
    if cmd.startswith('push'):
        c1, c2 = cmd.split()
        if c1 == 'push_front':
            q.appendleft(int(c2))
            cnt += 1
        elif c1 == 'push_back':
            q.append(int(c2))
            cnt += 1
    elif cmd.startswith('pop'):
        if not q:
            print(-1)
        elif cmd == 'pop_front':
            p = q.popleft()
            cnt -= 1
            print(p)
        elif cmd == 'pop_back':
            p = q.pop()
            cnt -= 1
            print(p)
    elif cmd == 'size':
        print(cnt)
    elif cmd == 'empty':
        if not q:
            print(1)
        else:
            print(0)
    elif cmd == 'front':
        if not q:
            print(-1)
        else:
            print(q[0])
    elif cmd == 'back':
        if not q:
            print(-1)
        else:
            print(q[-1])
