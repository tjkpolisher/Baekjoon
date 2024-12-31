# 1541: 잃어버린 괄호
# 알고리즘 분류: 수학/그리디 알고리즘/문자열/파싱

# 1. 식 입력
# 2. '-' 연산자를 기준으로 식을 분해
# 3. 각 식을 '+' 연산자를 기준으로 분해하고 더함
# 4. 더한 값들에 대하여 빼기 연산 실행
# 4. 결과 출력

formula = input()
parsed = list(formula.split('-'))
ans = 0
for i in range(len(parsed)):
    tmp = 0
    c = parsed[i].split('+')
    for j in range(len(c)):
        tmp += int(c[j])
    if i == 0:
        ans = tmp
    else:
        ans -= tmp
print(ans)
