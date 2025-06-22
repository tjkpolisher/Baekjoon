# 9196: 정수 직사각형
# 특이사항: 다국어(영어)(한국어 번역)
# 출처: ICPC 2013 Japan Domestic Contest A번
# 알고리즘 분류: 브루트포스 알고리즘/정렬/런타임 전의 전처리

# 0-1. 가능한 모든 직사각형 조합을 미리 생성 후 리스트에 저장
# 0-2. 리스트에 저장된 요소의 첫 번째 원소(대각선 길이의 제곱)에 대해 오름차순 정렬
# 0-3. 정렬된 리스트 내에서 인덱스를 추가로 맵핑해 딕셔너리에 저장
# 1. 테스트 케이스마다 직사각형의 높이 h, 너비 w 입력(h와 w는 0보다 크고 100보다 작음, h < w)
# 1-1. 입력의 마지막 줄에는 0이 두 개 주어짐.
# 2. h, w를 이용해 인덱스 딕셔너리에서 다음 원소를 추출
# 3. 추출된 원소를 이용해 다음 원소의 높이와 너비 추출
# 4. 높이와 너비 값을 출력

import sys
input = sys.stdin.readline

rectangles = []
for i in range(1, 151):
    for j in range(i + 1, 151):
        rectangles.append((i ** 2 + j ** 2, i, j))
rectangles.sort(key=lambda x: x[0])

idx = {(h, w): i for i, (_, h, w) in enumerate(rectangles)}

while True:
    test_case = input().rstrip()
    if test_case == '0 0':
        break
    h, w = map(int, test_case.split())
    i = idx[(h, w)]
    _, ans1, ans2 = rectangles[i + 1]
    print(ans1, ans2)
