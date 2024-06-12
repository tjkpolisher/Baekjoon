# 1120: 문자열
# 알고리즘 분류: 문자열/브루트포스 알고리즘

# 1. 두 문자열 A와 B 입력 (A의 길이는 B의 길이 이하)
# [보충설명] A와 B의 길이는 최대 50
# 2. A를 맨 앞부터 한 칸 씩 옮겨가면서 중복되지 않는 문자의 개수를 카운트해 저장
# 3. 저장된 값 중 최소값을 출력

import sys
input = sys.stdin.readline

A, B = input().rstrip().split()
ret = []
for i in range(len(B) - len(A) + 1):  # a의 시작점을 변경하여 b문자열을 탐색할 수 있는 횟수
    cnt = 0
    for j in range(len(A)):  # a 길이 만큼 전체
        if A[j] != B[i + j]:  # b 문자열의 시작점을 변경해가며 a 전체 문장 탐색
            cnt += 1
    ret.append(cnt)
print(min(ret))  # 차이가 가장 적은 경우 선택
