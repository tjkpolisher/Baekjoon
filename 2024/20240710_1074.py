# 1074: Z
# 알고리즘 분류: 분할 정복/재귀

# 1. N, r, c 입력 (1 ≤ N ≤ 15, 0 ≤ r, c < 2^N)
# 2. r, c가 2배가 될 때마다 값이 4배씩 커지는 것에 착안해 재귀 함수 구성
# 3. 정답 출력

N, r, c = map(int, input().split())


def solution(N, r, c):
    # 재귀 종료 조건
    if not N:
        return 0
    return 2 * (r % 2) + (c % 2) + 4 * solution(N - 1, int(r / 2), int(c / 2))


print(solution(N, r, c))
