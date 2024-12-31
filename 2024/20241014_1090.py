# 1090: 체커
# 알고리즘 분류: 브루트포스 알고리즘

# 1. 체커의 개수 N 입력 (N은 50 이하의 자연수)
# 2. N개의 줄에 걸쳐 각 체커의 x좌표와 y좌표 입력 (값은 각각 1,000,000 이하, 좌표 중복 가능)
# 3. 각각의 체커로부터 하나의 특정 체커로 모이는 거리를 각각 체크
# 3-1. N개 이상의 체커가 모일 경우, 그 점에서 가까운 두 명의 거리만 더하기
# 4. 계산된 값들 중 가장 작은 값을 각각 더한 후 출력

from itertools import product


def solve(N, checkers):
    # 모든 가능한 x, y 좌표 조합 생성
    x_coords = sorted(set(x for x, _ in checkers))
    y_coords = sorted(set(y for _, y in checkers))

    # 결과를 저장할 리스트 초기화
    result = [float('inf')] * N

    # 모든 가능한 중심점에 대해 계산
    for center_x, center_y in product(x_coords, y_coords):
        # 각 체커에서 중심점까지의 거리 계산
        distances = sorted(abs(x - center_x) + abs(y - center_y) for x, y in checkers)

        # 누적 거리 계산
        total_distance = 0
        for i in range(N):
            total_distance += distances[i]
            # i + 1개의 체커를 모으는데 필요한 최소 이동 횟수 갱신
            result[i] = min(result[i], total_distance)

    return result


# 입력 처리
N = int(input())
checkers = [list(map(int, input().split())) for _ in range(N)]

# 문제 해결 및 출력
print(*solve(N, checkers))
