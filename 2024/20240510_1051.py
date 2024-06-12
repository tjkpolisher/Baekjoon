# 1051: 숫자 정사각형
# 알고리즘 분류: 구현/브루트포스 알고리즘

# 1. 직사각형의 가로 및 세로 크기 N, M 입력
# 2. N개의 줄에 걸쳐 한 줄마다 M개의 정수 입력
# 3. 네 꼭지점의 정수가 같은 정사각형이 없다면 min(N, M) x min(N, M) 크기가 최대이므로 정답을 min(N, M)부터 시작
# 4. (0, 0) 지점부터 x 인덱스와 y 인덱스를 i만큼 확장시킨 범위의 점(꼭지점)의 정수가 모두 같은지 판단
# 4-1. 같은 케이스가 있으면 정답을 i로 갱신 후 다음 i로 넘어가 4번 과정을 반복
# 4-2. 같은 케이스가 없다면 마지막까지 순회한 후 다음 i로 넘어가 4번 과정을 반복
# 5. i = 1이 될 때까지 4번 과정 진행
# 6. 정답 출력

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
rectangle = []  # 숫자를 담을 직사각형 리스트

for _ in range(N):
    rectangle.append(list(input().rstrip()))


def answer(s):
    for i in range(N - s + 1):  # 행 인덱스
        for j in range(M - s + 1):  # 열 인덱스
            pivot = rectangle[i][j]
            key = (pivot == rectangle[i][j + s - 1]
                   and pivot == rectangle[i + s - 1][j]
                   and pivot == rectangle[i + s - 1][j + s - 1])
            if key:
                return True
    return False


size = min(N, M)
for k in range(size, 0, -1):
    if answer(k):
        print(k ** 2)
        break
