# 2713: 규현이의 사랑을 담은 문자메시지
# 특이사항: 다국어(영어)(한국어 번역)
# 출처: ICPC 2007 Greater New York Programming Contest C번
# 알고리즘 분류: 구현

# 1. 테스트 케이스의 개수 T 입력 (1 ≤ T ≤ 1000)
# 2. R, C, 규현이가 보내는 메시지 입력 (1 ≤ R,C ≤ 21)
# [보충설명] 메시지는 알파벳 대문자와 공백으로만 구성됨. 길이는 (R * C) / 53 이하.
# 3. 주어진 메시지의 문자를 숫자로 변환
# [보충설명] 공백 = 0, A = 1, B = 2, ..., Y = 25, Z = 26
# 4. 변환된 숫자를 다섯 자리 이진수로 변환
# 5. 이진수들을 R * C 크기의 2차원 리스트에 소용돌이 패턴으로 행렬에 채우되, 모든 칸을 채우지 못하면 0으로 채우기
# 6. 행렬을 행에 대하여 펼쳐서 한 줄에 공백 없이 출력

import sys
input = sys.stdin.readline

T = int(input())
char_num_dict = {' ': 0}
for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    char_num_dict[char] = ord(char) - ord('A') + 1

for _ in range(T):
    parts = input().rstrip().split(' ', 2)
    R, C = int(parts[0]), int(parts[1])
    message = parts[2] if len(parts) > 2 else ""

    R, C = int(R), int(C)

    matrix = [[None for i in range(C)] for j in range(R)]
    movement = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    x, y = 0, 0
    direction = 0

    for char in message:
        char_num = char_num_dict[char]  # 문자를 숫자로 변환
        char_bin = bin(char_num)[2:].zfill(5)  # 숫자를 다섯 자리 이진수로 변환

        for bit in char_bin:
            matrix[x][y] = bit
            dx, dy = movement[direction]
            nx, ny = x + dx, y + dy

            if 0 <= nx < R and 0 <= ny < C and matrix[nx][ny] is None:
                x, y = nx, ny
            else:
                direction = (direction + 1) % 4
                dx, dy = movement[direction]
                x, y = x + dx, y + dy

    output = []
    for row in matrix:
        for cell in row:
            output.append(cell if cell is not None else '0')
    print(''.join(output))
