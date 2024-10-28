# 2670: 연속부분최대곱
# 출처: 한국정보올림피아드 (KOI) 1996 중등부 1번
# 알고리즘 분류: 다이나믹 프로그래밍/브루트포스 알고리즘

# 1. 양의 실수의 개수 N 입력 (N은 10000 이하의 자연수)
# 2. N개의 줄에 걸쳐 실수를 하나씩 입력(실수는 소수점 첫째 자리까지 주어짐, 0.0 이상 9.9 이하)
# 3. 두 번째 인덱스부터 이전 인덱스의 곱을 배열의 값으로 바꿔가며 누적 곱 계산
# 4. 정답을 소수점 이하 셋째 자리까지 출력

import sys
input = sys.stdin.readline

N = int(input())
array = []
for _ in range(N):
    array.append(float(input()))

for i in range(1, N):
    array[i] = max(array[i], array[i] * array[i - 1])

print(f"{max(array):.3f}")
