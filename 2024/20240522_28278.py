# 28278: 스택 2
# 알고리즘 분류: 자료 구조/스택

# 1. 명령의 수 N 입력 (1 ≤ N ≤ 1,000,000)
# 2. N개의 줄에 걸쳐 명령 입력
# 2-1. `1 x`: 정수 X를 스택에 입력 (1 ≤ X ≤ 100,000)
# 2-2. `2`: 스택에 정수가 있다면 맨 위 정수를 빼고 출력하고 없으면 -1을 출력
# 2-3. `3`: 스택에 들어있는 정수의 개수 출력
# 2-4. `4`: 스택이 비어있으면 1, 아니면 0 출력
# 2-5. `5`: 스택에 정수가 있다면 맨 위의 정수 출력, 없으면 -1을 출력

import sys
input = sys.stdin.readline

N = int(input())
stack = []


def pop_and_print(stack):
    if stack:
        p = stack.pop()
        print(p)
    else:
        print(-1)
    return stack


def is_empty(stack):
    # 스택이 비어있을 때 1, 아니면 0을 출력해야 하므로 True/False를 원래와 반대로 설정
    return True if not stack else False


def top(stack):
    if stack:
        print(stack[-1])
    else:
        print(-1)


for _ in range(N):
    command = input().rstrip()
    if command.startswith('1'):
        _, x = command.split()
        stack.append(int(x))
    elif command == '2':
        stack = pop_and_print(stack)
    elif command == '3':
        print(len(stack))
    elif command == '4':
        print(int(is_empty(stack)))
    else:
        top(stack)
