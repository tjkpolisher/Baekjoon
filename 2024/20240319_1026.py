# 1026: 보물
# 알고리즘 분류: 수학/그리디 알고리즘/정렬

# 1. 두 배열 A와 B의 길이인 N 입력
# 2. A의 원소 N개 입력
# 3. B의 원소 N개 입력
# 4. A의 원소를 오름차순으로, B의 원소를 내림차순으로 정렬한 별개의 리스트 생성
# 5. 정렬A와 정렬B에 대하여 같은 인덱스의 원소끼리 곱한 뒤 더해서 S를 구함
# 6. S 출력

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)
S = 0
for i in range(N):
    S += (A[i] * B[i])

print(S)
