# 13945: Appearance Analysis
# 특이사항: 다국어(영어)
# 출처: CERC 2016 A번
# 알고리즘 분류: 구현/문자열

# 1. 두 정수 c, r 입력 (3 ≤ r, c ≤ 111)
# 2. r줄에 걸쳐 c개의 문자로 구성된 문자열 입력
# [보충설명] '#'은 벽돌을 의미하며, '.'과 '+'는 창문의 패턴을 구성하는 문자.
# [보충설명] 창문 행 사이에는 '#'으로만 구성된 문자열 행이 존재.
# [보충설명] 같은 행에 있는 창문들도 '#'으로 구분되나, 창 행과 창 열의 벽돌 개수 그리고 창 크기는 임의적.
# [보충설명] 입력되는 모든 창은 동일한 치수를 가짐.
# 3. 입력받은 전체 창문 격자에서 '#' 문자로 구분된 창문을 찾아 리스트로 변환
# 4. 주어진 창문을 90도씩 회전시키면서 모든 회전 형태를 생성
# 5. 생성된 형태 중 사전 순으로 가장 앞서는 형태를 선택
# 6. 추출한 모든 창문에 대하여 3~5 과정 진행
# 7. 6을 통해 추출한 형태를 집합에 저장
# 8. 집합의 길이 출력

import sys
input = sys.stdin.readline

r, c = map(int, input().split())
grid = [input().strip() for _ in range(r)]


def rotate(window):
    return [''.join(row) for row in zip(*window[::-1])]


def all_rotate(window):
    forms = [window]
    for _ in range(3):
        forms.append(rotate(forms[-1]))
    return forms


def normalize_window(window):
    return min(all_rotate(window))


def extract_windows(grid, r, c):
    windows = []
    i = 1
    while i < r - 1:
        j = 1
        while j < c - 1:
            height = 0
            while i + height < r - 1 and grid[i + height][j] != '#':
                height += 1

            width = 0
            while j + width < c - 1 and grid[i][j + width] != '#':
                width += 1

            window = [grid[i + h][j:j + width] for h in range(height)]
            windows.append(window)
            j += (width + 1)
        i += (height + 1)
    return windows


windows = extract_windows(grid, r, c)
unique_windows = set()
for window in windows:
    normalized = normalize_window(window)
    window_str = '\n'.join(normalized)
    unique_windows.add(window_str)

print(len(unique_windows))
