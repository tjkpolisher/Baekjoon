# 18706: Coffee
# 특이사항: 다국어(영어)
# 출처: ICPC 2018 Arab Collegiate Programming Contest C번
# 알고리즘 분류: 수학/구현/자료 구조/문자열/사칙연산/해시를 사용한 집합과 맵/트리를 사용한 집합과 맵

# 1. 테스트 케이스의 개수 T 입력
# 2. 커피의 종류를 뜻하는 정수 C, 손님의 수를 뜻하는 정수 P 입력 (1 ≤ C,P ≤ 100)
# 3. C개의 줄에 걸쳐 커피의 종류를 뜻하는 문자열 N과 사이즈별 가격을 뜻하는 S, M, L 입력(1 ≤ S,M,L ≤ 100)
# 4. P개의 줄에 걸쳐 주문자 이름 X, 커피 사이즈 Y, 커피 이름 Z 입력
# [보충설명] 이 문제에서 문자열 변수는 모두 길이가 15 이하.
# 5. 딕셔너리에 저장된 정보를 바탕으로 커피값과 배송비를 더해서 이름과 함께 출력
# 5-1. 단, 5의 배수에서 1 적거나 1 큰 경우에는 5의 배수로 맞춰서 출력

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    C, P = map(int, input().split())
    delivery_fee = int(100 // P)  # 배달비 (100달러를 P명이서 나눔)

    coffee = {}  # 종류 및 사이즈별 커피 가격
    for i in range(C):
        N, S, M, L = input().rstrip().split()
        S, M, L = int(S), int(M), int(L)
        coffee[N] = (S, M, L)

    for i in range(P):
        X, Y, Z = input().rstrip().split()
        if Y == 'small':
            price = coffee[Z][0]
        elif Y == 'medium':
            price = coffee[Z][1]
        else:
            price = coffee[Z][2]

        result = delivery_fee + price
        if result % 5 == 1:
            print(X, result - 1)
        elif result % 5 == 4:
            print(X, result + 1)
        else:
            print(X, result)
