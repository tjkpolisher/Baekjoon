# 21194: Meditation
# 특이사항: 다국어(영어)
# 출처: ICPC SWERC 2020-2021 연습 세션 PB번
# 알고리즘 분류: 그리디 알고리즘/정렬

# 1. 두 정수 n, k 입력 (1 ≤ k ≤ n ≤ 100,000)
# 2. n개의 줄에 거쳐 운동의 등급을 뜻하는 정수 g_i를 입력
# 3. g_i의 리스트를 내림차순으로 정렬
# 4. 앞쪽 k개를 슬라이스 합을 출력

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
grades = []
for _ in range(n):
    grades.append(int(input()))

grades.sort(reverse=True)

print(sum(grades[:k]))
