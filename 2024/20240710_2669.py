# 2669: 직사각형 네개의 합집합의 면적 구하기
# 출처: 한국정보올림피아드(KOI) 1996 초등부 3번
# 알고리즘 분류: 구현

# 1. 네 줄에 걸쳐 왼쪽 아래 점의 x, y좌표와 오른쪽 위 점의 x, y좌표를 나타내는 정수를 네 개씩 입력
# [보충설명] 모든 x, y좌표는 1 이상 100 이하의 정수
# 2. 행과 열이 모두 0에서 100까지의 인덱스를 가지는 2차원 배열 생성(모든 원소는 0으로 초기화)
# 2-1. 넓이 변수를 생성하고 0으로 초기화
# 3. 첫 번째 점부터 시작해 왼쪽 아래 점부터 오른쪽 위 점까지 사각형의 면적에 해당하는 점을 1로 변환한 후 넓이에 1 추가
# 3-1. 단, 이미 1로 변환된 점은 건드리지 않고 그대로 넘어감. 위 연산은 해당 배열의 원소가 아직 0일 때만 수행.
# 4. 넓이 출력

import sys
input = sys.stdin.readline

square_array = [[0] * 101 for _ in range(101)]
area = 0

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    # 이중 반복문 수행
    for i in range(x1, x2):
        for j in range(y1, y2):
            if not square_array[i][j]:
                square_array[i][j] = 1
                area += 1

print(area)
