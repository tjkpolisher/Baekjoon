# 1925: 삼각형
# 알고리즘 분류: 구현/기하학/많은 조건 분기/피타고라스 정리

# 1. 세 줄에 걸쳐 한 줄 씩 각각 삼각형을 이루는 세 점의 x좌표, y좌표 입력
# 2. 세 점 간의 기울기 계산
# 2-1. 세 기울기가 모두 같을 경우, 일직선 위에 있으므로 "X" 출력 후 종료
# 3. 세 점 간의 길이 계산
# 3-1. 세 변의 길이가 모두 같을 경우, "JungTriangle" 출력 후 종료
# 4. 세 변이 이루는 각도 계산
# 5. 두 변의 길이가 같을 경우
# 5-1. 가장 큰 각이 90°이면 "Jikkak2Triangle" 출력 후 종료
# 5-2. 가장 큰 각이 90°보다 크면 "Dunkak2Triangle" 출력 후 종료
# 5-3. 가장 큰 각이 90°보다 작으면 "Yeahkak2Triangle" 출력 후 종료
# 6. 세 변의 길이가 모두 다를 경우
# 6-1. 가장 큰 각이 90°이면 "JikkakTriangle" 출력 후 종료
# 6-2. 가장 큰 각이 90°보다 크면 "DunkakTriangle" 출력 후 종료
# 6-3. 가장 큰 각이 90°보다 작으면 "YeahkakTriangle" 출력 후 종료

import sys
from math import acos, pi, inf
input = sys.stdin.readline

points = []
for _ in range(3):
    a, b = map(int, input().split())
    points.append((a, b))


def get_slope(a, b):
    x1, y1 = a
    x2, y2 = b
    if x2 == x1:
        return inf
    return (y2 - y1) / (x2 - x1)


def get_length(a, b):
    x1, y1 = a
    x2, y2 = b
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2)


def get_angle(a, b, c):
    return acos((a + b - c) / (2 * (a ** 0.5) * (b ** 0.5))) * 180 / pi


def solve(points):
    # 기울기 계산
    slopes = []
    for i in range(3):
        slopes.append(get_slope(points[i], points[(i + 1) % 3]))
    if len(set(slopes)) == 1:
        return "X"

    # 세 변의 길이 계산
    lengths = []
    for i in range(3):
        lengths.append(get_length(points[i], points[(i + 1) % 3]))
    if len(set(lengths)) == 1:
        return "JungTriangle"
    else:
        angles = []
        for i in range(3):
            angles.append(get_angle(lengths[i], lengths[(i + 1) % 3], lengths[(i + 2) % 3]))
        MAX_ANGLE = max(angles)

        if len(set(lengths)) == 2:
            if MAX_ANGLE > 90:
                return "Dunkak2Triangle"
            elif MAX_ANGLE == 90:
                return "Jikkak2Triangle"
            else:
                return "Yeahkak2Triangle"
        else:
            if MAX_ANGLE > 90:
                return "DunkakTriangle"
            elif MAX_ANGLE == 90:
                return "JikkakTriangle"
            else:
                return "YeahkakTriangle"


print(solve(points))
