# 9291: 스도쿠 채점
# 특이사항: 다국어(영어)(한국어 번역)
# 출처: UVa HSPC 2013 F번
# 알고리즘 분류: 구현/브루트포스 알고리즘

# 1. 테스트 케이스의 개수 T 입력 (T는 100 이하의 자연수)
# 2. 각 테스트 케이스마다 9개의 줄에 걸쳐 9개의 정수를 공백으로 구분(테스트 케이스 사이에 빈 줄 있음)
# 3. 행을 검사해 중복 없는 숫자가 9개인지, 합이 45인지 검사
# 4. 열을 검사해 중복 없는 숫자가 9개인지, 합이 45인지 검사
# 5. 3x3 정사각형 내의 중복 없는 숫자가 9개인지, 합이 45인지 검사
# 6. 검사 결과를 주어진 형식에 맞게 출력

T = int(input())


def is_valid_sudoku(grid):
    # 행 검사
    for row in grid:
        if len(set(row)) != 9 or sum(row) != 45:
            return False

    # 열 검사
    for col in range(9):
        column = [grid[row][col] for row in range(9)]
        if len(set(column)) != 9 or sum(column) != 45:
            return False

    # 3x3 그룹 검사
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            group = [grid[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if len(set(group)) != 9 or sum(group) != 45:
                return False

    return True


for case in range(1, T + 1):
    grid = []
    for _ in range(9):
        row = list(map(int, input().split()))
        grid.append(row)

    result = "CORRECT" if is_valid_sudoku(grid) else "INCORRECT"
    print(f"Case {case}: {result}")

    if case < T:
        input()  # 빈 줄 처리
