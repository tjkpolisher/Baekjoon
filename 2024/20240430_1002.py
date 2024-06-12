# 1002: 터렛
# 알고리즘 분류: 수학/기하학/많은 조건 분기

# 1. 테스트 케이스의 개수 T 입력
# 2. 여섯 정수 x1, y1, r1, x2, y2, r2가 주어짐
# [보충 설명] x1, y1: 조규현의 좌표
# y1, y2: 백승환의 좌표
# -10,000 ≤ x1, y1, x2, y2 ≤ 10,000
# r1, r2: 조규현이 계산한 류재명과의 거리, 백승환이 계산한 류재명과의 거리 (1 ≤ r1, r2 ≤ 10,000)
# 3. 두 원의 중심 사이의 거리 d를 기준으로 개수 판별
# 3-1. 두 원이 완전히 동일한 경우(즉, 겹쳐 있을 때)는 위치의 개수가 무한하다고 판정.
# 3-2. 한 원이 다른 원 내부에 있을 경우 0
# 3-3. d > r1 + r2 또는 d < |r1 - r2|일 경우 0
# 3-4. d = r1 + r2 또는 d = |r1 - r2|일 경우 1
# 3-5. 그 외의 경우 2
# 위치의 개수 출력. 단, 위치의 개수가 무한할 때는 -1을 출력

from math import sqrt
import sys
input = sys.stdin.readline


def circle_point(x1, y1, r1, x2, y2, r2):
    # 두 원의 중심이 동일할 때
    if (x1, y1) == (x2, y2):
        # 반지름까지 동일해 두 원이 완전히 동일할 때
        if r1 == r2:
            return -1
        # 그렇지 않은 경우(한 원이 다른 원 내부에 있을 때)
        else:
            return 0
    else:
        d = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)  # 두 원의 중심 사이의 거리
        # 두 원의 어떤 점에서도 접하지 않을 때
        if d > r1 + r2 or d < abs(r1 - r2):
            return 0
        # 두 원이 한 점에서 접할 때
        elif d == r1 + r2 or d == abs(r1 - r2):
            return 1
        # 두 원이 두 점에서 접할 때
        else:
            return 2


T = int(input().rstrip())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().rstrip().split())
    print(circle_point(x1, y1, r1, x2, y2, r2))
