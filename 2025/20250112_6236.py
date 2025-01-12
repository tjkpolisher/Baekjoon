# 6236: 용돈 관리
# 특이사항: 다국어(영어)(한국어 번역)
# 출처: USACO March 2007 Contest Silver 3번
# 알고리즘 분류: 이분 탐색/매개 변수 탐색

# 1. 용돈을 사용할 기간 N, 인출 횟수 M을 공백으로 구분해 입력 (1 ≤ N ≤ 100,000, 1 ≤ M ≤ N)
# 2. N개의 줄에 걸쳐 현우가 i번째 날에 이용할 금액 입력 (금액은 10,000 이하의 자연수)
# 3. 이분 탐색을 위한 중간점을 (left + right) // 2로 설정
# 4. 주어진 K로 M번 안에 모든 금액을 사용할 수 있는지 확인
# 4-1. 부족할 경우 left를 mid + 1로 변경
# 4-2. 그 외의 경우 정답을 mid로 변경한 뒤 right를 mid - 1로 변경
# 5. 이분 탐색 종료 후 정답 출력

import sys
input = sys.stdin.readline


def withdraw_check(k, m, amounts):
    cnt = 1
    current_sum = 0

    for amount in amounts:
        if current_sum + amount > k:
            cnt += 1
            current_sum = 0

        current_sum += amount

    return cnt <= m


N, M = map(int, input().split())
amounts = [int(input()) for _ in range(N)]

left, right = max(amounts), sum(amounts)
ans = right

while left <= right:
    mid = (left + right) // 2
    if withdraw_check(mid, M, amounts):
        ans = mid
        right = mid - 1
    else:
        left = mid + 1

print(ans)
