# 30011: 겹다각형의 각
# 출처: 선린인터넷고등학교 제1회 선린 프로그래밍 챌린지 Open Contest E번
# 알고리즘 분류: 수학/기하학

# 1. 다각형의 개수 N 입력 (1 ≤ N ≤ 1000)
# 2. 각 다각형의 꼭지점의 개수를 나타내는 N개의 수 A_1, A_2, ..., A_N을 공백으로 구분해 입력
# [보충설명] 3 ≤ A_i ≤ 100 (1 ≤ i ≤ N), A_i ≥ A_(i + 1) (1 ≤ i < N)
# 3-1. 주어진 다각형이 1개일 경우 내각의 합을 출력
# 3-2. A_i의 다각형에 A_(i + 1)의 정다각형이 내접하는 경우의 각을 계산해 정답에 더함
# 4. 정답 출력

N = int(input())
vertex = list(map(int, input().split()))


def solution(N, vertex):
    if N == 1:
        angle = 180 * (vertex[0] - 2)
    else:
        angle = 0
        for i in range(N):
            angle += 180 * (vertex[i] - 2)
            if i < N - 1:
                angle += 180 * vertex[i + 1] - 180 * (vertex[i + 1] - 2)
    return angle


print(solution(N, vertex))
