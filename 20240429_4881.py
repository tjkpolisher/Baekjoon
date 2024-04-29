# 4881: 자리수의 제곱
# 특이사항: 다국어(영어)(한국어 번역), 백트래킹 알고리즘 적용 필요
# 출처: ICPC 2010 Arab Collegiate Programming Contest B번
# 알고리즘 분류: 구현/자료 구조/브루트포스 알고리즘/해시를 사용한 집합과 맵

# 1. 두 정수 A와 B 입력 (0 < A, B < 10^9)
# 1-1. 마지막 줄에는 0이 두 개 주어짐
# 2. 자릿수의 제곱을 더해서 집합에 더하기
# 3-1. 연산 결과가 이미 집합에 존재해서 사이클이 생성된 경우 그 리스트는 더 이상 연산하지 않음
# 3-2. 그렇지 않고 연산 결과가 다른 쪽 집합에 존재할 경우 전체 연산 중지
# 3-3. 어떻게 해도 같은 수가 나타나지 않으면 0을 출력하게 됨
# 4. A와 B, 횟수 출력


def num_square_sum(n):
    n_list = [n]
    while n_list.count(n_list[-1]) < 2:
        cal = n_list[-1]
        new_num = 0
        for i in str(cal):
            new_num += int(i) ** 2
        n_list.append(new_num)
    return n_list


def backtracking(list1, list2):
    minimum_num = 0
    for i in list1:
        if i in list2:
            minimum_num = list1.index(i) + list2.index(i) + 2
    for j in list2:
        if j in list1 and minimum_num > list1.index(j) + list2.index(j) + 2:
            minimum_num = list1.index(j) + list2.index(j) + 2

    return minimum_num


while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    else:
        list1 = num_square_sum(A)
        list2 = num_square_sum(B)
        print(A, B, backtracking(list1, list2))
