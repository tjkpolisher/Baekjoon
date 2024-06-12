# 1515: 수 이어 쓰기
# 알고리즘 분류: 구현/그리디 알고리즘/문자열/브루트포스 알고리즘

# 1. 지우고 남은 수를 한 줄로 이어 붙인 수가 주어짐
# 2. 1부터 증가시키면서 숫자 중 겹치는 부분이 있는지 확인
# 3. 마지막 수까지 증가시켰을 때의 수 출력

import sys
input = sys.stdin.readline

num = input().rstrip()

ans = 0
while True:
    ans += 1
    ans_str = str(ans)
    while len(num) > 0 and len(ans_str) > 0:
        if num[0] == ans_str[0]:
            num = num[1:]
        ans_str = ans_str[1:]
    if not num:
        print(ans)
        break
