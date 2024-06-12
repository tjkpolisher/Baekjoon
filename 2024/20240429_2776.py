# 2776: 암기왕
# 알고리즘 분류: 자료 구조/정렬/이분 탐색/해시를 사용한 집합과 맵

# 1. 테스트 케이스의 개수 T 입력
# 2. 수첩 1에 적어놓은 정수의 개수 N 입력 (1 ≤ N ≤ 1,000,000)
# 3. N개의 줄에 걸쳐 수첩 1에 적힌 정수 N개 입력
# 4. 수첩 2에 적어놓은 정수의 개수 M 입력 (1 ≤ M ≤ 1,000,000)
# 5. N개의 줄에 걸쳐 수첩 2에 적힌 정수 M개 입력
# 6. 수첩 2에 적혀 있는 M개의 숫자 순서대로, 수첩 1에 있으면 1을 없으면 0을 출력

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    num1 = set(map(int, input().split()))

    M = int(input())
    num2 = list(map(int, input().split()))

    for m in num2:
        if m in num1:
            print(1)
        else:
            print(0)
