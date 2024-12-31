# 5525: IOIOI
# 특이사항: 서브태스크, 다국어(일본어)(한국어 번역)
# [서브태스크] 1. (50점) N ≤ 100, M ≤ 10000. 2. (50점) 추가적인 제약 조건 없음.
# 출처: JOI(Japanese Olympiad in Informatics) 2008/2009 1번, 2012/2013 P4번, 2013/2014 P4번
# 알고리즘 분류: 문자열

# 1. 문자열 P_N 내의 알파벳 'O'의 개수 N 입력 (1 ≤ N ≤ 1,000,000)
# [보충설명] P_N은 I와 O가 교대로 나오는 문자로, O가 N개 포함됨.
# 2. 문자열 S의 길이 M 입력 (2N+1 ≤ M ≤ 1,000,000)
# 3. S 입력
# 4. 반복문을 실행해 현재 위치에서 3개 떨어진 인덱스까지의 문자열이 'IOI'가 맞는지 확인.
# 4-1. 아니라면 위치를 한 칸 뛰고 OI의 개수 카운터를 초기화.
# 4-2. 맞다면 위치를 두 칸 뛰고 카운터에 1을 더함
# 4-3. N과 카운터가 동일하다면 결과값에 1을 더해줌.
# 5. 결과값 - 1을 출력

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().rstrip()

cursor, cnt, ans = 0, 0, 0

while cursor < (M - 1):
    if S[cursor:cursor + 3] == 'IOI':
        cnt += 1
        cursor += 2
        if cnt == N:
            ans += 1
            cnt -= 1
    else:
        cursor += 1
        cnt = 0

print(ans)
