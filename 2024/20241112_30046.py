# 30046: HJS
# 출처: 한양대학교 ERICA 캠퍼스 Zero One Algorithm Contest 2023 B번
# 알고리즘 분류: 브루트포스 알고리즘/많은 조건 분기

# 1. 세 문자열 P, Q, R의 길이인 N 입력 (1 ≤ N ≤ 300,000)
# 2. 세 개의 줄에 걸쳐 문자열 P, Q, R 입력 (세 문자열에 들어가는 숫자는 서로 중복되지 않음)
# 3-1. P, Q, R 중 같은 문자열이 하나라도 있다면 "Hmm..." 출력 후 종료
# 3-2. P, Q, R이 같은 문자로 시작한다면 서로 다른 문자가 등장할 때까지 같은 문자들을 제거
# 3-3. 제거 후 가장 앞에 있는 문자 a, b, c에 대해 다음과 같이 판단
# 3-3-1-1. a = b, b ≠ c일 경우 P, Q의 맨 앞 문자가 달라질 때까지 제거한 d, e 생성
# 3-3-1-2. d = c이면서 e = a인 경우만 "Hmm..." 출력, 나머지 경우 "HJS! HJS! HJS!" 출력 후 종료
# 3-3-2-1. a ≠ b, b = c일 경우 Q, R의 맨 앞 문자가 달라질 때까지 제거한 d, e 생성
# 3-3-2-2. d = b이면서 e = a인 경우만 "Hmm..." 출력, 나머지 경우 "HJS! HJS! HJS!" 출력 후 종료
# 3-3-3. a ≠ b, a = c인 경우 어떻게 해도 p < q < r일 수 없으므로 "Hmm..." 출력 후 종료
# 3-3-4. a ≠ b, b ≠ c, a ≠ c인 경우 항상 조건을 만족할 수 있으므로 "HJS! HJS! HJS!" 출력 후 종료

import sys
input = sys.stdin.readline

N = int(input())
P = input().rstrip()
Q = input().rstrip()
R = input().rstrip()


def solution(N, P, Q, R):
    # P, Q, R 중 같은 문자열이 하나라도 있다면 Hmm... 출력
    if P == Q or Q == R or R == P:
        return "Hmm..."

    idx = 0
    # 공통 문자열 제거
    while idx < N and P[idx] == Q[idx] == R[idx]:
        idx += 1
    if idx == N:
        return "Hmm..."

    a, b, c = P[idx], Q[idx], R[idx]
    if a == b:
        # Case 1
        if b != c:
            d, e = P, Q
        else:
            return "Hmm..."
    elif b == c:
        # Case 2
        if a != b:
            d, e = Q, R
        else:
            return "Hmm..."
    elif a == c:
        # Case 3
        return "Hmm..."
    else:
        # Case 4
        return "HJS! HJS! HJS!"

    # Case 1과 Case 2를 통과한 d, e에 대하여 추가 비교
    while idx < N and d[idx] == e[idx]:
        idx += 1
    if idx < N and d[idx] == c and e[idx] == a:
        return "Hmm..."
    else:
        return "HJS! HJS! HJS!"


print(solution(N, P, Q, R))
