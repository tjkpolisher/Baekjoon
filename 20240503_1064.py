# 1064: 평행사변형
# 특이사항: 스페셜 저지
# 알고리즘 분류: 수학/기하학/피타고라스 정리

# 1. 세 개의 서로 다른 점의 x, y 좌표를 나타내는 정수 입력
# [보충설명] A(xA,yA), B(xB,yB), C(xC,yC)의 좌표들은 절대값이 5000 이하인 정수
# 2. 세 직선 AB, BC, CA의 기울기와 y절편 계산
# 3-1. 세 직선이 같은 직선 상에 있으면 -1을 출력 후 종료
# 3-2. 그렇지 않으면 세 선분 AB, BC, CA의 길이 계산
# 3-3. 세 길이를 기반으로 둘레의 길이를 계산해 리스트에 저장
# 3-4. 최대 둘레 길이와 최소 둘레 길이의 차이를 출력


def incline_and_bias(x1, y1, x2, y2):
    # 두 점을 지나는 직선의 기울기를 구하는 함수
    if x1 == x2:
        incline = 0
    elif y1 == y2:
        incline = float('inf')
    else:
        incline = (y2 - y1) / (x2 - x1)
    return incline


def total_length(l1, l2):
    return 2 * (l1 + l2)


x_a, y_a, x_b, y_b, x_c, y_c = map(int, input().split())
i_ab = incline_and_bias(x_a, y_a, x_b, y_b)
i_bc = incline_and_bias(x_b, y_b, x_c, y_c)
i_ca = incline_and_bias(x_c, y_c, x_a, y_a)
if i_ab == i_bc == i_ca:
    print(-1.0)
else:
    l_ab = ((x_b - x_a) ** 2 + (y_b - y_a) ** 2) ** 0.5
    l_bc = ((x_c - x_b) ** 2 + (y_c - y_b) ** 2) ** 0.5
    l_ca = ((x_a - x_c) ** 2 + (y_a - y_c) ** 2) ** 0.5

    lengths = [total_length(l_ab, l_bc),
               total_length(l_bc, l_ca),
               total_length(l_ca, l_ab)]
    print(max(lengths) - min(lengths))
