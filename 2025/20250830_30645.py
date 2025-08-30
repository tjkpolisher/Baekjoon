# 30645: 인형 전시
# 출처: 인하대학교 2023 IGRUS Newbie Programming Contest C번
# 알고리즘 분류: 그리디 알고리즘/정렬

# 1. 탁자의 행의 개수 R과 열의 개수 C 입력 (1 ≤ R,C ≤ 1,000)
# 2. 탁자의 전시할 수 있는 인형의 개수 N 입력 (1 ≤ N ≤ 1,000,000)
# 3. N개의 인형의 높이 h_i 입력 (1 ≤ h_i ≤ 1,000,000)
# 4. 높이 리스트를 정렬
# 5. 각 열의 마지막 높이와 개수 저장 리스트를 각각 생성
# 6. 정렬된 인형을 배치하면서, 배치 가능한 열 중 가장 적게 차 있는 열 선택
# 7. 배치가 가능하면 사이즈와 최적 열 갱신
# 8. 갱신된 열이 -1이 아닐 경우 카운터에 1을 더함
# 9. 카운터 출력

import sys
input = sys.stdin.readline

R, C = map(int, input().split())
N = int(input())
heights = list(map(int, input().split()))

heights.sort()
last_heights = [0] * C
col_counts = [0] * C

visible_count = 0

for height in heights:
    best_col = -1
    min_size = R + 1

    for col in range(C):
        if col_counts[col] < R and last_heights[col] < height:
            if col_counts[col] < min_size:
                min_size = col_counts[col]
                best_col = col

    if best_col != -1:
        last_heights[best_col] = height
        col_counts[best_col] += 1
        visible_count += 1

print(visible_count)
