# 3019: 테트리스
# 특이사항: 다국어(영어)(한국어 번역)
# 출처: 2007 Croatian Regional Competition in Informatics 2007 2번
# 알고리즘 분류: 구현/브루트포스 알고리즘

# 1. 열의 너비 C, 떨어뜨리는 블록의 번호 P 입력 (1 ≤ C ≤ 100, 1 ≤ P ≤ 7)
# 2. 각 칸의 현재 높이 h 입력 (h는 0 < h ≤ 100인 자연수)
# 3. 7가지 블록의 칸 배치와 회전 시의 패턴으로 저장해 각각의 함수 생성
# 4. 해당 칸 배치의 condition과 일치할 경우 가능한 경우의 수에 1을 더하기
# [보충설명] 블록이 떨어졌을 때, 블록과 블록 또는 블록과 바닥 사이에 채워지지 않은 칸이 생기면 안 됨.
# 5. 정답 출력

C, P = map(int, input().split())
current_heights = list(map(int, input().split()))


def count_blocks(patterns):
    cnt = 0
    for length, condition in patterns:
        for i in range(C - length + 1):
            if condition(i):
                cnt += 1
    return cnt


def block1():
    return count_blocks([
        (1, lambda i: current_heights[i] >= 0),
        (4, lambda i: current_heights[i] == current_heights[i + 1] == current_heights[i + 2] == current_heights[i + 3])
    ])


def block2():
    return count_blocks([
        (2, lambda i: current_heights[i] == current_heights[i + 1])
    ])


def block3():
    return count_blocks([
        (3, lambda i: current_heights[i] == current_heights[i+1] == current_heights[i+2] - 1),
        (2, lambda i: current_heights[i] - 1 == current_heights[i+1])
    ])


def block4():
    return count_blocks([
        (3, lambda i: current_heights[i] - 1 == current_heights[i+1] == current_heights[i+2]),
        (2, lambda i: current_heights[i] == current_heights[i+1] - 1)
    ])


def block5():
    return count_blocks([
        (3, lambda i: current_heights[i] == current_heights[i+1] == current_heights[i+2]),
        (3, lambda i: current_heights[i] - 1 == current_heights[i+1] == current_heights[i+2] - 1),
        (2, lambda i: current_heights[i] - 1 == current_heights[i+1]),
        (2, lambda i: current_heights[i] == current_heights[i+1] - 1)
    ])


def block6():
    return count_blocks([
        (3, lambda i: current_heights[i] == current_heights[i+1] == current_heights[i+2]),
        (2, lambda i: current_heights[i] - 2 == current_heights[i+1]),
        (3, lambda i: current_heights[i] == current_heights[i+1] - 1 == current_heights[i+2] - 1),
        (2, lambda i: current_heights[i] == current_heights[i+1])
    ])


def block7():
    return count_blocks([
        (3, lambda i: current_heights[i] == current_heights[i+1] == current_heights[i+2]),
        (2, lambda i: current_heights[i] == current_heights[i+1]),
        (3, lambda i: current_heights[i] - 1 == current_heights[i+1] - 1 == current_heights[i+2]),
        (2, lambda i: current_heights[i] == current_heights[i+1] - 2)
    ])


if P == 1:
    print(block1())
elif P == 2:
    print(block2())
elif P == 3:
    print(block3())
elif P == 4:
    print(block4())
elif P == 5:
    print(block5())
elif P == 6:
    print(block6())
else:
    print(block7())
