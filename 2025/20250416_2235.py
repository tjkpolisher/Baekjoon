# 2235: GPS Encoding
# 특이사항: 다국어(영어)
# 출처: NZPC 2005 G번
# 알고리즘 분류: 구현/다이나믹 프로그래밍/문자열/백트래킹

# 1. 각 테스트 케이스마다 영어 대문자로 구성된 암호문 입력 (암호문의 길이는 26)
# 1-1. '#'이 입력될 경우 종료
# 1-2. 암호문의 각 문자를 키로 삼고 그 인덱스를 값으로 하는 딕셔너리 생성
# 2. 숫자 문자열 입력 (길이는 3 이상 20 이하)
# 2-1. '0'이 입력될 경우 해당 문제 종료
# 2-2. 재귀적으로 dp 딕셔너리를 구성해 함수 실행
# 2-3-1. 더 이상 처리할 문자가 없을 때 빈 문자열과 남은 글자 수 0을 반환하며 종료
# 2-3-2. 각 인덱스에서 한 자리 또는 두 자리를 사용할 수 있는지 확인
# 2-3-3. 확인 후 암호문 딕셔너리에서 문자를 불러오고 최소 글자 수와 사전 순 뒤쪽 암호 선택
# 2-4. 결과 출력된 문자열을 출력
# 3. 문제가 끝나면 문제 번호에 1을 더함

import sys
input = sys.stdin.readline


def decode(s, i, cypher, dp):
    n = len(s)
    # 재귀 종료 조건: 문자열의 끝에 도달하면 cost는 0, 암호문은 빈 문자열
    if i == n:
        return (0, "")
    if i in dp:
        return dp[i]

    best_count = float("inf")  # 최소 글자 수
    best_enc = ""  # 해당되는 암호문(사전 순으로 뒤쪽에 있는 것)

    # Case 1 - 한 자리 숫자일 떄
    num1 = int(s[i])
    next_count, next_enc = decode(s, i + 1, cypher, dp)
    candidate_count = next_count + 1
    candidate_enc = cypher[num1] + next_enc

    best_count = candidate_count
    best_enc = candidate_enc

    # Case 2 - 두 자리 숫자일 때(10 ~ 25)
    if i + 1 < n:
        two_digit = int(s[i:i + 2])
        if two_digit < 26:
            next_count2, next_enc2 = decode(s, i + 2, cypher, dp)
            candidate_count2 = 1 + next_count2
            candidate_enc2 = cypher[two_digit] + next_enc2

            if candidate_count2 < best_count:
                best_count = candidate_count2
                best_enc = candidate_enc2
            elif candidate_count2 == best_count and candidate_enc2 > best_enc:
                best_enc = candidate_enc2

    dp[i] = (best_count, best_enc)
    return dp[i]


problem_num = 1
while True:
    cypher = input().rstrip()
    if cypher == '#':
        break
    else:
        if problem_num > 1:
            # 문제와 문제 사이를 공백으로 구분(첫 문제는 제외)
            print()

    char_dict = {cypher[i]: i for i in range(26)}

    print(f"Problem {problem_num}")

    while True:
        num = input().rstrip()
        if num == '0':
            break

        dp = {}
        _, result = decode(num, 0, cypher, dp)
        print(result)

    problem_num += 1
