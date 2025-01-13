# 18125: 고양이 사료
# 출처: 제1회 가톨릭대학교 프로그래밍 경진대회(CCPC) Div. 2 2번
# 알고리즘 분류: 구현

# 1. 사료 그림의 열과 행을 나타내는 정수 R, C 입력 (1 ≤ R, C ≤ 100)
# 2. 행과 열의 수에 맞게 사료 위치를 1과 0으로 입력
# 3. 학생들이 나눠준 사료 입력
# [보충설명] 사료 그림은 반시계 방향으로 90도 돌아간 것이므로, 학생들 사료의 행과 열은 그와 정반대
# 4. 사료 그림 2차원 리스트를 전치 후 각 행을 앞뒤로 뒤집음
# 5. 사료 그림과 학생 사료의 리스트가 완전히 일치하는지 확인
# 5-1. 완전히 일치하지 않으면 놀란 고양이 그림 문자열 출력
# 5-2. 완전히 일치하면 윙크하는 고양이 출력

import sys
input = sys.stdin.readline

string1 = '''|>___/|     /}
| O O |    / }
( =0= )""""  \\
| ^  ____    |
|_|_/    ||__|
'''
string2 = '''|>___/|        /}
| O < |       / }
(==0==)------/ }
| ^  _____    |
|_|_/     ||__|
'''

R, C = map(int, input().split())
picture = [list(map(int, input().split())) for _ in range(C)]
students = [list(map(int, input().split())) for _ in range(R)]

picture_T = list(map(list, zip(*picture)))
for i in range(R):
    picture_T[i].reverse()

for i in range(R):
    for j in range(C):
        if picture_T[i][j] and not students[i][j]:
            print(string1, end='')
            exit()
else:
    print(string2, end='')
