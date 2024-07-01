# 9375: 패션왕 신해빈
# 특이사항: 다국어(영어)(한국어 번역)
# 출처: ICPC Northwestern European Regional Contest BAPC 2013 I번
# (BAPC: Benelux Algorithm Programming Contest)
# 알고리즘 분류: 수학/자료 구조/조합론/해시를 사용한 집합과 맵

# 1. 테스트 케이스의 개수 입력(최대 100)
# 2-1. 각 테스트 케이스의 첫째 줄에 해빈이가 가진 의상의 수 n 입력 (0 ≤ n ≤ 30)
# 2-2. 다음 n개 줄에 걸쳐 의상의 이름과 의상의 종류가 공백으로 구분됨(같은 종류의 의상은 하나만 입을 수 있음)
# 3. 입력받은 의상의 종류를 키로 사용하는 딕셔너리의 값에 리스트를 할당하고 의상의 이름을 리스트에 저장
# 4. 모든 리스트의 길이를 곱한 후 1을 뺌(알몸인 경우의 수 제외)
# 5. 결과를 출력

import sys
input = sys.stdin.readline

t = int(input())  # 테스트 케이스의 개수
for _ in range(t):
    n = int(input())  # 의상의 개수
    clothes = {}  # 의상의 종류를 키로 사용하는 딕셔너리
    for _ in range(n):
        name, kind = input().rstrip().split()  # 의상의 이름과 종류
        if kind in clothes:
            clothes[kind].append(name)
        else:
            clothes[kind] = [name]

    result = 1
    for key in clothes.keys():
        result *= (len(clothes[key]) + 1)  # 해당 의상 종류의 의상 개수

    print(result - 1)  # 알몸인 경우를 제외
