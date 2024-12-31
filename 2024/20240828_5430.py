# 5430: AC
# 특이사항: 다국어(영어)(한국어 번역)
# 알고리즘 분류: 구현/자료 구조/문자열/파싱/덱

# 1. 테스트 케이스의 개수 T 입력 (T는 100 이하의 자연수)
# 2. 수행할 함수 p 입력 (1 ≤ len(p) ≤ 100,000)
# [보충설명] 함수 p는 R(뒤집기)와 D(버리기)의 문자열로 구성됨
# 3. 배열에 들어있는 수의 개수 n 입력 (0 ≤ n ≤ 100,000)
# 4. 배열에 들어있는 정수를 입력받아 덱으로 만듦 (1 ≤ x_i ≤ 100)
# [보충설명] 전체 테스트 케이스에 주어지는 p 길이의 합과 n의 합은 700,000을 넘지 않음
# 5. 기본적으로 popleft()로 값을 빼내되, R이 나올때마다 pop()과 popleft()를 바꾸면서 R 연산 수행
# 6. 도중에 덱이 비어있게 되면 error 출력 후 종료
# 7. 그렇지 않고 모든 연산이 끝나면 함수를 주어진 형식에 따라 출력

import sys
from collections import deque
input = sys.stdin.readline

T = int(input())


def flip(flag):
    return True if not flag else False


def direction_pop(flag, array):
    if flag:  # 뒤집힌 상태
        array.pop()
    else:  # 뒤집히지 않은 상태
        array.popleft()
    return array


for _ in range(T):
    p = input().rstrip()
    n = int(input())
    array = deque(input().rstrip()[1:-1].split(","))
    if not n:  # 빈 문자열이 들어올 경우 다시 덱으로 처리해야 함
        array = deque()

    is_flipped = False
    error_occured = False
    for i in range(len(p)):
        if p[i] == 'R':
            is_flipped = flip(is_flipped)
        elif p[i] == 'D':
            if not array:
                print("error")
                error_occured = True
                break
            array = direction_pop(is_flipped, array)
    if not error_occured:
        if is_flipped:
            array.reverse()
        print("[" + ",".join(array) + "]")
