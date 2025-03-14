# 6582: Artificial Intelligence?
# 특이사항: 다국어(영어)
# 출처: University of Ulm Local Contest 1998 A번
# 알고리즘 분류: 구현/문자열/파싱

# 1. 테스트 케이스의 개수 입력
# 2. 테스트 케이스 입력 후 데이터 필드를 추출해 그 값을 입력
# [보충설명] 데이터 필드는 세 가지 중 유형 중 하나(I=xA, U=xV or P=xW. x는 해당 물리량의 값.)
# 3. 문제에서 주어지지 않은 필드를 P = U * I 공식에 맞게 계산
# 4. 계산된 필드를 형식에 맞게 출력

import sys
input = sys.stdin.readline


def extract_value(unit):
    prefix_table = {'m': 1e-3, 'k': 1e3, 'M': 1e6}
    if unit[-1] in (',', '.'):
        unit = unit[:-1]
    if unit[-2] in ('m', 'k', 'M'):
        value = float(unit[:-2]) * prefix_table[unit[-2]]
    else:
        value = float(unit[:-1])
    return value


T = int(input())
for i in range(T):
    test_case = list(input().rstrip().split())
    field1, field2 = None, None
    for word in test_case:
        if not field1 and "=" in word:
            field1 = word
        if field1 and '=' in word:
            field2 = word

    concept1, unit1 = field1.split('=')
    concept2, unit2 = field2.split('=')
    value1 = extract_value(unit1)
    value2 = extract_value(unit2)

    power, voltage, current = None, None, None

    for concept, value in zip((concept1, concept2), (value1, value2)):
        if concept == 'P':
            power = value
        elif concept == 'U':
            voltage = value
        else:
            current = value

    if not power:
        ans1 = 'P'
        ans2 = voltage * current
        ans3 = 'W'
    elif not voltage:
        ans1 = 'U'
        ans2 = power / current
        ans3 = 'V'
    else:
        ans1 = 'I'
        ans2 = power / voltage
        ans3 = 'A'

    print(f"Problem #{i + 1}")
    print(f"{ans1}={ans2:.2f}{ans3}")
    if i != T - 1:
        print()
