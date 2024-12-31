# 14888: 연산자 끼워넣기
# 출처: 삼성전자 SW 역량테스트
# 알고리즘 분류: 브루트포스 알고리즘/백트래킹

# 1. 수의 개수 N 입력
# 2. N개의 수를 입력
# 3. 덧셈, 뺄셈, 곱셈, 나눗셈 연산자의 개수 입력
# 4. dfs를 실행하여 각 연산자를 사용할 때마다 결과를 현재의 최소값, 최대값과 비교
# 5. 연산이 완료된 후 최대값, 최소값 순서대로 출력

import sys

input = sys.stdin.readline
N = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))  # 연산자의 개수

maximum = -1e9
minimum = 1e9


def dfs(depth, total, plus, minus, multiply, divide):
    global maximum, minimum
    if depth == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    if plus:
        dfs(depth + 1, total + num[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - num[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * num[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(total / num[depth]), plus, minus, multiply, divide - 1)


dfs(1, num[0], op[0], op[1], op[2], op[3])
print(maximum)
print(minimum)
