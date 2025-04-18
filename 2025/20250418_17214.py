# 17214: 다항 함수의 적분
# 출처: 2019 HEPC ROOKIE League E번
# 알고리즘 분류: 수학/문자열/많은 조건 분기/파싱/미적분학

# 1. 최대 차수가 1인 일변수 다항식 입력 후 연산자를 기준으로 분할
# [보충설명] 다항식의 항은 최대 2개, 변수는 항상 x로 주어짐, 계수는 절대값 10,000 이하의 0이 아닌 2의 배수
# [보충설명] 상수는 절대값이 10,000을 넘지 않는 정수, 계수의 절대값이 1이면 1을 생략, 다항식은 내림차순으로 입력
# 1-1. 0이 입력되면 W를 출력 후 프로그램 종료
# 2. 일차항이면 계수를 2로 나누고 xx를 더해서 정답 리스트에 저장(계수의 절대값이 1이면 1은 생략)
# 3. 상수항이면 뒤에 x를 붙여서 정답 리스트에 저장
# 4. 리스트의 맨 마지막에 '+W'를 append
# 5. 정답 리스트의 각 항 사이에 연산자를 넣어서 출력

import sys
input = sys.stdin.readline

polynomial = input().rstrip()  # 다항식(최대 1차식)

if polynomial == "0":
    print("W")
    exit()

terms = []

if polynomial.startswith('-'):
    terms.append('-')
    polynomial = polynomial[1:]

for i in range(len(polynomial)):
    if polynomial[i] in ('+', '-'):
        terms.append(polynomial[:i])  # 연산자 이전까지의 항
        terms.append(polynomial[i])  # 연산자
        terms.append(polynomial[i+1:])  # 연산자 다음 항
        break
else:
    terms.append(polynomial)

ans = []
for term in terms:
    # 연산자일 때
    if term in ('+', '-'):
        ans.append(term)
    # 일차항일 때
    elif term.endswith('x'):
        coeff = int(term[:-1])  # 계수
        if coeff == 2:
            ans.append('xx')
        else:
            ans.append(f'{coeff // 2}xx')
    # 0일 때
    elif term == '0':
        continue
    # 상수항일 때
    else:
        if int(term) == 1:
            ans.append('x')
        else:
            ans.append(f"{term}x")

ans.append('+W')
print(''.join(ans))
