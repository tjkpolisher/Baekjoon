# 2175: 땅 자르기
# 특이사항: 다국어(영어)(한국어 번역), 스페셜 저지
# 출처: ICPC 2003 East Central Regional Contest H번
# 알고리즘 분류: 브루트포스 알고리즘/기하학/다각형의 넓이

# 1. 사각형의 네 꼭짓점의 좌표를 순서대로 입력(시계 방향 또는 반시계 방향)
# [보충설명] 각 꼭짓점의 좌표는 절대값이 10000을 넘지 않는 정수
# 2. 각 꼭지점 사이의 중점을 계산
# 3. 분할된 영역을 삼각형을 나누고, 각 삼각형들의 조합에 따라 넓이 차이가 가장 작은 경우 계산
# 4. 정답을 소수점 셋째 자리까지 반올림하여 출력

def middle(dot1, dot2):
    # 두 꼭지점의 중점을 계산하는 함수
    return [(dot1[0] + dot2[0]) / 2, (dot1[1] + dot2[1]) / 2]


def t_area(dot1, dot2, dot3):
    # 분할된 삼각형의 각 넓이를 계산하는 함수
    return abs(((dot2[0] - dot1[0]) * (dot3[1] - dot1[1]) - (dot3[0] - dot1[0]) * (dot2[1] - dot1[1])) / 2)


arr = list(map(int, input().split()))
vertex = []
for i in range(4):
    vertex.append([arr[2 * i], arr[2 * i + 1]])

vertex_with_middle = [0] * 8
for i in range(8):
    if i % 2 == 0:
        vertex_with_middle[i] = vertex[i // 2]
    else:
        vertex_with_middle[i] = middle(vertex[i // 2], vertex[(i // 2 + 1) % 4])

left_half, right_half = 0, 10 ** 9
# 8개의 점에 대하여 반복
for i in range(8):
    target_dots = []
    if i % 2 == 0:  # 꼭짓점인 경우
        for j in range(2, 7):
            target_dots.append((i + j) % 8)
        triangles = []
        for k in range(4):
            triangles.append(t_area(vertex_with_middle[i],
                                    vertex_with_middle[target_dots[k]],
                                    vertex_with_middle[target_dots[k + 1]]))
        # 기존의 값보다 나눈 넓이의 차이가 작으면 기존 값과 교환
        for l in range(3):
            x = sum(triangles[:l + 1])
            y = sum(triangles[l + 1:])
            if abs(x - y) < abs(left_half - right_half):
                left_half, right_half = x, y
    else:  # 중점인 경우
        for j in range(1, 8):
            target_dots.append((i + j) % 8)
        triangles = []
        for k in range(6):
            triangles.append(t_area(vertex_with_middle[i],
                                    vertex_with_middle[target_dots[k]],
                                    vertex_with_middle[target_dots[k + 1]]))
        for l in range(5):
            x = sum(triangles[:l + 1])
            y = sum(triangles[l + 1:])
            if abs(x - y) < abs(left_half - right_half):
                left_half, right_half = x, y

left_half, right_half = round(left_half, 3), round(right_half, 3)

if left_half > right_half:
    left_half, right_half = right_half, left_half

print(left_half, right_half)
