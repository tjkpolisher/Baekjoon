# 11899: 괄호 끼워넣기
# 출처: GENIUSainta.com - oj.uz Contest GA6 1번
# 알고리즘 분류: 자료 구조/문자열/스택

# 1. 올바르지 않은 괄호열 S 입력 (길이는 1 이상 50 이하)
# 2. S의 문자들을 순서대로 스택에 집어넣으면서 올바른 괄호열에 해당하는 부분을 우선 제거
# 3. 스택에 남은 괄호의 개수를 출력

S = input()
stack = []
for ch in S:
    if not stack:
        stack.append(ch)
    elif stack[-1] == '(' and ch == ')':
        stack.pop()
    else:
        stack.append(ch)

print(len(stack))
