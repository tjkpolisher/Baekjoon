# 2630: 색종이 만들기
# 출처: 한국정보올림피아드(KOI) 2001 중등부 1번
# 알고리즘 분류: 분할 정복/재귀

# 1. 전체 종이의 한 변의 길이 N 입력 (N=2^k, k는 1 이상 7 이하의 자연수)
# 2. N줄에 걸쳐 색종이의 각 가로줄의 정사각형 칸의 색들이 입력
# [보충설명] 하얀색으로 칠해진 칸이 0, 파란색으로 칠해진 칸은 1, 각 숫자 사이는 공백으로 구분
# 3. (0, 0) 인덱스의 색을 기준으로 가로 또는 세로가 N // 2 길이에 도달할 때마다 재귀 함수 호출
# 4. 분할된 색종이마다 3의 과정을 반복하고, 최종 분할되었을 경우 하얀색 색종이와 파란색 색종이의 개수 count
# 5. 첫째 줄에 하얀색 색종이의 개수, 둘째 줄에 파란색 색종이의 개수 출력

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = int(input())
paper = []
for _ in range(N):
    paper.append(list(map(int, input().split())))

n_white = 0
n_blue = 0


def slice(x, y, n):
    global n_white, n_blue

    color = paper[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != paper[i][j]:
                slice(x, y, n // 2)
                slice(x, y + n // 2, n // 2)
                slice(x + n // 2, y, n // 2)
                slice(x + n // 2, y + n // 2, n // 2)
                return

    if color == 0:
        n_white += 1
    else:
        n_blue += 1


slice(0, 0, N)

print(n_white)
print(n_blue)
