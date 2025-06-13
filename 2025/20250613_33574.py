# 33574: 끊임없는 정렬과 창조함으로
# 출처: 제2회 한국디지털미디어고등학교 프로그래밍 챌린지 D번
# 알고리즘 분류: 구현/정렬/시뮬레이션

# 1. 쿼리의 개수 Q 입력 (1 ≤ Q ≤ 3000) 후 배열 S 초기화
# 2. Q개의 줄에 걸쳐 쿼리 입력
# 3-1. 쿼리가 1 x 일 경우 x의 값에 따라 S 정렬
# 3-1-1. x=1이면 오름차순 정렬
# 3-1-2. x=2이면 내림차순 정렬
# 3-2. 쿼리가 2 x t일 경우 S_x와 S_{x+1} 사이에 t 삽입
# [보충설명] 0 ≤ x ≤ |S|, -10^9 ≤ t ≤ 10^9
# 4. Q개의 쿼리를 모두 수행한 뒤, S의 원소를 공백으로 구분해 출력(단, 빈 배열은 출력하지 않음)

import sys
input = sys.stdin.readline

Q = int(input())
S = []
cnt = 0

for _ in range(Q):
    query = input().rstrip()
    if query.startswith('1'):
        x = int(query.split()[1])
        if x == 1:
            S.sort()
        elif x == 2:
            S.sort(reverse=True)
    elif query.startswith('2'):
        _, x, t = map(int, query.split())
        if x == 0:
            S.insert(0, t)
        elif x == len(S):
            S.append(t)
        else:
            S.insert(x, t)
        cnt += 1

if S:
    print(cnt)
    print(*S)
