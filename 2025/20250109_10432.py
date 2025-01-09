# 10432: 데이터 스트림의 섬
# 특이사항: 다국어(영어)(한국어 번역)
# 출처: 2014 Greater New York Programming Contest B번
# 알고리즘 분류: 브루트포스 알고리즘

# 1. 테스트 케이스의 수 P 입력 (1 ≤ P ≤ 1000)
# 2. 테스트 케이스의 번호 T와 12개의 음이 아닌 정수 입력(처음과 마지막 정수는 항상 0)
# 3. 스택에 맨 아래에 0을 넣고 반복문 시작
# 4-1. 스택이 비어있지 않고 맨 위 원소가 수열의 현재 원소보다 크면 원소 이하가 될 때까지 pop 후 카운터에 1 추가
# 4-2. 맨 위 원소가 수열의 현재 원소와 같으면 continue
# 4-3. 그렇지 않을 경우 스택에 원소 append
# 5. T와 카운터를 한 줄에 공백으로 구분해 출력

import sys
input = sys.stdin.readline

P = int(input())
for _ in range(P):
    data = list(map(int, input().split()))
    T = data[0]
    sequence = data[1:]

    stack = [0]
    island_count = 0

    for num in sequence:
        while stack and stack[-1] > num:
            stack.pop()
            island_count += 1

        if stack and stack[-1] == num:
            continue
        else:
            stack.append(num)

    print(T, island_count)
