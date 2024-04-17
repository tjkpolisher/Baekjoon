# 9012: 괄호
# 특이사항: 다국어(영어)(한국어 번역)
# 알고리즘 분류: 자료 구조/문자열/스택

# 1. 테스트 데이터 개수 T 입력
# 2. [반복문]
# 2-1. 괄호 문자열 입력
# 2-2. 첫 번째 문자부터 스택에 입력
# 2-3. 스택이 비었으면서 닫는 괄호가 입력되면 NO 출력 후 종료
# 2-4. 괄호의 쌍이 맞으면 두 문자를 스택에서 제거
# 2-5. 마지막 문자까지 입력한 후 스택이 비어있지 않으면 NO, 비었으면 YES 출력


def parentheses(string):
    stack = []
    for c in string:
        if not stack:
            if c == ")":
                return "NO"
            else:
                stack.append(c)
        elif stack[-1] == "(" and c == ")":
            stack.pop()
        else:
            stack.append(c)
    if not stack:
        return "YES"
    else:
        return "NO"


T = int(input())
for _ in range(T):
    string = input()
    print(parentheses(string))
