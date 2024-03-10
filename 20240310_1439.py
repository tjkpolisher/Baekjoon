# 1439: 뒤집기
# 알고리즘 분류: 그리디 알고리즘/문자열

# 1. 문자열 S 입력
# 2. 순서대로 순회하면서 앞 글자와 다른 문자가 나오는 경우 카운터에 1 추가
# 3. (카운터 + 1) // 2 을 출력

import sys
input = sys.stdin.readline

S = input().rstrip()
cnt = 0

for i in range(1, len(S)):
    if S[i - 1] != S[i]:
        cnt += 1

print((cnt + 1) // 2)
