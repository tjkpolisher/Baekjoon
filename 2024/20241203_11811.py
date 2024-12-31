# 11811: 데스스타
# 특이사항: 스페셜 저지, 다국어(영어)(한국어 번역)
# 출처: COCI 2015/2016 Contest #4 3번
# 알고리즘 분류: 수학/비트마스킹

# 1. 행렬의 크기 N 입력 (1 ≤ N ≤ 1000)
# 2. N개의 줄에 걸쳐 행렬의 각 원소인 N개의 숫자 m_ij 입력 (1 ≤ m_ij ≤ 10^9)
# 3. 각 행의 모든 값에 대하여 or 연산을 해서 a_i 리스트에 저장
# 4. 수열 a_i를 한 줄에 공백으로 구분하여 출력

import sys
input = sys.stdin.readline

N = int(input())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

a = [0] * N  # 음이 아닌 정수의 수열 a_i를 담은 리스트
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        a[i] |= matrix[i][j]

print(*a)
