# 31066: 비 오는 날
# 특이사항: 다국어(영어)(한국어 번역), 예제는 채점하지 않음
# 출처: 서울과학고등학교 SciOI 2023 A-1번
# 알고리즘 분류: 구현/그리디 알고리즘/시뮬레이션

# 1. 테스트 케이스의 개수 T 입력
# 2. T개의 줄에 걸쳐 i번째 테스트 케이스를 나타내는 세 정수 N, M, K 입력(학생 수, 우산 개수, 한 우산에 들어갈 수 있는 최대 사람 수)
# [보충설명] 1 ≤ T ≤ 1000, 1 ≤ i ≤ T, 1 ≤ N,M,K ≤ 10
# 3. 초기 변수 a, b, c, d를 a = N, b = M, c = d = 0으로 설정(c = N이 되는 최소 횟수를 구하는 것이 목적)
# 3-1. 사람 수가 우산 수보다 많으면서, K와 M이 모두 1인 경우 -1 출력 후 다음 테스트 케이스 진행
# 4. 다음의 두 시행 중 하나를 실행
# 4-1. x명의 학생이 y개의 우산을 이용해 융합인재관으로 이동하므로 a -= x, b -= y, c += x, d += y
# 4-1-1. 우산 수 * 우산 개당 허용 가능한 사람 수가 건너감
# 4-2. z명의 학생이 w개의 우산을 이용해 창의인재관으로 돌아오므로 a += z, b += w, c -= z, d -= w
# 4-2-1. 한 사람이 모든 우산을 가지고 돌아오도록 구현
# 4-3. 융합인재관에 모든 학생이 모이면 반복문 break
# [보충설명] 0 < x ≤ a, 0 < y ≤ b, x ≤ Ky, 0 < z ≤ c, 0 < w ≤ d, z ≤ Kw
# 5. 종료 후 시행의 최소 횟수 출력

T = int(input())


def go_to(a, b, c, d, x, y):
    return a - x, b - y, c + x, d + y


def coming_back(a, b, c, d, z, w):
    return a + z, b + w, c - z, d - w


for _ in range(T):
    N, M, K = map(int, input().split())
    a, b, c, d = N, M, 0, 0
    cnt = 0
    if K == 1 and M == 1 and N > M:
        print(-1)
        continue

    while True:
        x = min(K * M, a)
        y = M
        a, b, c, d = go_to(a, b, c, d, x, y)
        cnt += 1
        if c == N:
            break

        z = 1
        w = M
        a, b, c, d = coming_back(a, b, c, d, z, w)
        cnt += 1

    print(cnt)
