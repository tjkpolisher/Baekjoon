# 1059: 좋은 구간
# 유의사항: 다음 조건을 만족하는 구간 [A, B]를 '좋은 구간'이라고 함.
# 1. A와 B는 양의 정수이고, A < B를 만족한다.
# 2. A ≤ x ≤ B를 만족하는 모든 정수 x가 집합 S에 속하지 않는다.
# 알고리즘 분류: 수학/브루트포스 알고리즘/정렬

# 1. 집합 S의 크기 L 입력
# 2. 집합 S에 포함된 정수(즉, S의 원소) L개 입력
# 3. n 입력
# 4. S에 포함된 정수 중 n을 포함하는 범위의 두 수만 추출하여 각각 변수 A, B로 할당
# 4-1. 만약 n이 S의 원소인 경우 0 출력 후 종료
# 5. 주어진 범위에 맞춰 카운터 계산
# 6. 카운터 출력

import sys
input = sys.stdin.readline

L = int(input())
S = list(map(int, input().split()))
S.sort()
n = int(input())

cnt = 0
if n in S:
    print(cnt)
else:
    A = 0
    B = 0
    for num in S:
        if num < n:
            A = num
        elif num > n and B == 0:
            B = num
    B -= 1
    A += 1
    cnt = (n - A) * (B - n + 1) + (B - n)
    print(cnt)
