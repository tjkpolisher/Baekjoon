# 1503: 세 수 고르기
# 알고리즘 분류: 브루트포스 알고리즘

# 1. 자연수 N과 집합 S의 크기 M 입력 (1 ≤ N ≤ 1,000, 0 ≤ M ≤ 50)
# 2. S에 들어갈 M개의 수 입력 (집합의 원소는 1,000 이하의 자연수)
# 3. 1부터 N까지의 자연수를 담은 집합과 S의 차집합 생성
# 4. 3중 반복문을 통해 x * y * z 계산
# 5. abs(N - x*y*z)가 작아지는 경우 갱신
# 6. 정답 출력

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
try:
    S = set(map(int, input().split()))
except ValueError:
    # 집합의 크기가 0인 경우 둘째 줄은 빈 줄
    S = set()

xyz_set = set(range(1, 1002)) - S

ans = 10 ** 9
for x in xyz_set:
    for y in xyz_set:
        for z in xyz_set:
            temp = x * y * z
            ans = min(ans, abs(N - temp))
            if N + 1 < temp:
                break

print(ans)
