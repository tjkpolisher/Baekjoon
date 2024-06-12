# 10828: 스택
# 알고리즘 분류: 구현/자료 구조/스택

# 1. 명령의 수 N 입력 (1 ≤ N ≤ 10,000)
# 2. N개의 줄에 걸쳐 명령 입력(명령은 총 다섯 종류)
# 3. 출력 명령(size 명령어 등)이 나올 때마다 현재 스택에 들어있는 정수의 개수 출력

import sys
N = int(input())
cnt = 0
stack = []
for _ in range(N):
    cmd = sys.stdin.readline().rstrip()
    if cmd.startswith('push'):
        c1, c2 = cmd.split()
        stack.append(int(c2))
        cnt += 1
    elif cmd == 'pop':
        if not stack:
            print(-1)
        else:
            p = stack.pop()
            cnt -= 1
            print(p)
    elif cmd == 'size':
        print(cnt)
    elif cmd == 'empty':
        if not stack:
            print(1)
        else:
            print(0)
    elif cmd == 'top':
        if not stack:
            print(-1)
        else:
            print(stack[-1])
