# 18870: 좌표 압축
# 알고리즘 분류: 정렬/값_좌표 압축

# 1. N 입력 (1 ≤ N ≤ 1,000,000)
# 2. 수직선 위의 좌표 X_i가 N개 입력 (-10^9 ≤ X_i ≤ 10^9)
# 3. 수직선 좌표를 중복을 제거한 뒤 오름차순으로 정렬
# 4. 정렬 후 좌표 리스트에 대해 좌표를 키로, 인덱스를 값으로 하는 딕셔너리 생성
# 5. 값을 원래 좌표 리스트의 순서대로 출력

import sys
input = sys.stdin.readline

N = int(input())
coords = list(map(int, input().split()))
coords_sorted = sorted(list(set(coords)))

coords_dict = {coords_sorted[i]: i for i in range(len(coords_sorted))}
for i in coords:
    print(coords_dict[i], end=' ')
