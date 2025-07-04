# 28381: Mischievous Math
# 특이사항: 다국어(영어)
# 출처: GCPC 2023 M번
# 알고리즘 분류: 수학/브루트포스 알고리즘/해 구성하기/사칙연산

# 1. 정수 d 입력 (1 ≤ d ≤ 100)
# 2. 1 ≤ a,b,c ≤ 100인 a, b, c 조합을 탐색
# 2-1. a, b, c, d 중 중복이 있을 경우 continue
# 2-2. 그렇지 않은 경우 판정 시작
# 3-1. 1개, 2개, 3개의 숫자를 사용하는 경우에 대해 d가 만들어지는지 확인
# 3-2. 괄호 위치에 따라 구조 확인
# 3-3. 모든 경우를 확인했지만 d를 만들지 못할 때만 False를 반환
# 4. False가 반환되면 a, b, c를 한 줄에 출력

from itertools import permutations


def is_solvable(a, b, c, d):
    nums = [a, b, c]
    for k in range(1, 4):
        for p in permutations(nums, k):
            # --- Case 1: 숫자 1개를 사용하는 경우 ---
            if k == 1:
                if p[0] == d:
                    return True

            # --- Case 2: 숫자 2개를 사용하는 경우 ---
            elif k == 2:
                x, y = p[0], p[1]
                if x + y == d:
                    return True
                if x - y == d:
                    return True
                if x * y == d:
                    return True
                # 나눗셈은 나누어 떨어지는 경우에만 유효합니다.
                if y != 0 and x % y == 0 and x // y == d:
                    return True

            # --- Case 3: 숫자 3개를 사용하는 경우 ---
            elif k == 3:
                x, y, z = p[0], p[1], p[2]

                # 괄호 위치에 따라 두 가지 주요 구조를 확인합니다.
                # 구조 1: (x op1 y) op2 z
                # 중간 결과 res1을 계산하고, 이어서 z와 두 번째 연산을 수행합니다.
                res1_options = {x + y, x - y, x * y}
                if y != 0 and x % y == 0:
                    res1_options.add(x // y)

                for res1 in res1_options:
                    if res1 + z == d:
                        return True
                    if res1 - z == d:
                        return True
                    if res1 * z == d:
                        return True
                    if z != 0 and res1 % z == 0 and res1 // z == d:
                        return True

                # 구조 2: x op1 (y op2 z)
                # 중간 결과 res2를 계산하고, x와 첫 번째 연산을 수행합니다.
                res2_options = {y + z, y - z, y * z}
                if z != 0 and y % z == 0:
                    res2_options.add(y // z)

                for res2 in res2_options:
                    if x + res2 == d:
                        return True
                    if x - res2 == d:
                        return True
                    if x * res2 == d:
                        return True
                    if res2 != 0 and x % res2 == 0 and x // res2 == d:
                        return True

    # 모든 경우를 확인했지만 d를 만들지 못한 경우
    return False


d = int(input())
for a in range(1, 101):
    for b in range(1, 101):
        for c in range(1, 101):
            if len({a, b, c, d}) != 4:
                continue
            if not is_solvable(a, b, c, d):
                print(a, b, c)
                exit()
