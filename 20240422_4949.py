# 4949: 균형잡힌 세상
# 특이사항: 다국어(영어)(한국어 번역)
# 알고리즘 분류: 자료 구조/문자열/스택

# 1. 문자열 입력(맨 마지막 줄에는 온점(.) 하나가 들어옴)
# 2. 문자를 순회하면서 소괄호와 대괄호를 순서대로 스택에 집어넣음
# 3. 스택에서 괄호의 짝을 지을 수 있으면 그 쌍을 pop
# 4. 순회 종료 후 스택이 비어있지 않으면 "no", 비어 있으면 "yes" 출력

import sys
input = sys.stdin.readline

while True:
    string = input().rstrip()
    if string == '.':
        break

    stack = []
    for c in string:
        if c in ("(", ")", "[", "]"):
            if not stack:
                stack.append(c)
                if c in (")", "]"):
                    break
            elif stack[-1] == "(" and c == ")":
                stack.pop()
            elif stack[-1] == "[" and c == "]":
                stack.pop()
            else:
                stack.append(c)
    if stack:
        print("no")
    else:
        print("yes")
