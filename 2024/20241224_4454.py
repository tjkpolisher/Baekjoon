# 4454: 상근이의 여자친구
# 특이사항: 다국어(영어)(한국어 번역)
# 출처: ICPC 2011 Pacific Northwest Region Programming Contest H번
# 알고리즘 분류: 이분 탐색/매개 변수 탐색

# 1. 테스트 케이스 입력
# 1-1. 입력이 없을 경우 종료
# [보충설명] 모든 입력값은 1000을 넘지 않는 음이 아닌 실수. c, d, m, t는 양수.
# 2. 시작점을 0, 끝점을 충분히 큰 값으로 설정하고 이분 탐색 시작
# 3. 계산식 m / mid * (a * mid ** 4 + b * mid ** 3 + c * mid ** 2 + d * mid)가 t를 넘는지 판단
# 3-1. 넘을 경우 끝점을 중간점으로 이동
# 3-2. 그렇지 않을 경우 시작점을 중간점으로 이동
# 4. 정답을 소수점 둘째 자리까지 출력

import sys
from math import floor
input = sys.stdin.readline

while True:
    try:
        # a, b, c, d: 연료 소비율 계수, m: 달려야 하는 거리, t: 총 연료량
        a, b, c, d, m, t = map(float, input().split())
    except ValueError:
        break

    # 이진 탐색 범위 설정
    start = 1
    end = 10 ** 9
    v = 0  # 찾고자 하는 속도

    for _ in range(100):
        mid = (start + end) / 2
        if m / mid * (a * mid ** 4 + b * mid ** 3 + c * mid ** 2 + d * mid) > t:
            end = mid
        else:
            start = mid
            v = mid

    print(f"{floor(v * 100) / 100:0.2f}")
