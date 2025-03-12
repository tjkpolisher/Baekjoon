# 3652: 새트리
# 특이사항: 다국어(영어)
# 출처: NWERC 2011 B번
# 알고리즘 분류: 수학/재귀

# 1. 문자열 'a/b'를 입력 후 split(a는 기약분수의 분자, b는 분모. 둘 다 동시에 1인 경우는 없음)
# [보충설명] 기약분수이므로 a, b의 최대공약수는 1. 1 ≤ a,b ≤ 10^9
# 2. 재귀 종료 조건: a와 b가 모두 1이 되면 종료
# 3-1. a > b이면 R을 출력하고 b, a - b를 입력해 재귀 호출하여 부모 노드로 이동
# 3-2. a < b이면 L을 출력하고 b - a, a를 입력해 재귀 호출하고 부모 노드로 이동

import sys
sys.setrecursionlimit(10 ** 4)

a, b = map(int, input().split('/'))


def bird(a, b):
    if a == 1 and b == 1:
        return
    if a > b:
        print("R", end="")
        bird(b, a - b)
    else:
        print("L", end="")
        bird(b - a, a)


bird(a, b)
