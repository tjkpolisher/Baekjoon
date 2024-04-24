# 11723: 집합
# 특이사항: 언어 제한(node.js 금지), 언어별 메모리 제한 상이함
# 알고리즘 분류: 비트마스킹/구현

# 1. 집합 연산의 수 M 입력 (1 ≤ M ≤ 3,000,000)
# 2. 공집합 s 생성
# 3. M개의 줄에 걸쳐 연산이 주어짐(check 연산이 주어질 때마다 결과 출력)

import sys

M = int(input())
s = set()
for _ in range(M):
    cmd = sys.stdin.readline().rstrip()
    if cmd == "all":
        s = set(range(1, 21))
    elif cmd == "empty":
        s = set()
    else:
        c, x = cmd.split()
        x = int(x)
        if c == "add" and x not in s:
            s.add(x)
        elif c == "remove" and x in s:
            s.remove(x)
        elif c == "check":
            if x in s:
                print(1)
            else:
                print(0)
        elif c == "toggle":
            if x in s:
                s.remove(x)
            else:
                s.add(x)
