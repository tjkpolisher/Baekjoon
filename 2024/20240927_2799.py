# 2799: 블라인드
# 특이사항: 다국어(영어)(한국어 번역)
# 출처: Croatian Open Competition in Informatics(COCI) 2011/2012 Contest #6 2번
# 알고리즘 분류: 구현

# 1. 건물의 층 수 M, 창문의 개수 N 입력 (1 ≤ M, N ≤ 100)
# 2. 현재 건너편 아파트의 상태가 4x4 그리드로 입력
# [보충설명] 창문과 창문은 '#'으로 구분, 아파트의 정보는 5M + 1줄, 각 줄은 5N + 1개 글자로 이루어짐.
# 3. 한 줄씩 순회하면서 블라인드의 타입을 인식
# 3-1. 1, 6, 11, ...번째 줄은 모두 창틀이므로 continue
# 3-2. 나머지 줄에서 창문에 해당하는 인덱스에 '*'문자가 나오는 행의 개수를 헤아림
# 3-3. 다음 창틀이 입력되었을 때 각 창문에 대한 블라인드 개수에 따라 블라인드 유형 개수를 더함
# 4. 모든 입력이 종료된 후 한 줄에 공백으로 구분하여 각 블라인드 유형의 개수를 출력
# [힌트] 출력하는 숫자의 합은 M x N과 같아야 함.

import sys
input = sys.stdin.readline

M, N = map(int, input().split())
b1, b2, b3, b4, b5 = 0, 0, 0, 0, 0  # 각 블라인드 유형의 개수
blinds = [0] * N  # 한 층의 각 창문의 블라인드 개수를 저장할 리스트

for i in range(1, 5 * M + 2):
    building = input().rstrip()
    if i % 5 == 1:
        # 1, 6, 11, ...번째 줄은 전부 창틀이므로 continue
        if i > 1:
            b1 += blinds.count(0)
            b2 += blinds.count(1)
            b3 += blinds.count(2)
            b4 += blinds.count(3)
            b5 += blinds.count(4)
            blinds = [0] * N
            # print(f"{b1=}, {b2=}, {b3=}, {b4=}, {b5=}")
        continue

    for j in range(N + 1):
        if j < N and building[5 * j + 1] == '*':
            # 한 행에서 블라인드가 처진 모든 행은 '*'이므로 각 창문의 첫 글자만 '*'인지 확인
            blinds[j] += 1
    # print(f"{blinds=}")

print(b1, b2, b3, b4, b5)
