# 23895: Allocation
# 특이사항: 서브태스크, 다국어(영어)
# 출처: Google Kick Start 2020 Round A A번
# 알고리즘 분류: 그리디 알고리즘/정렬

# 1. 테스트 케이스의 개수 T 입력 (1 ≤ T ≤ 100)
# 2. 팔고 있는 집의 개수 N과 자신이 가진 예산 B 입력. (1 ≤ B ≤ 10^5)
# [보충설명] 서브태스크 - Test set 1에서 1 ≤ N ≤ 100, Test set 2에서 1 ≤ N ≤ 10^5
# 3. 집값을 나타내는 N개의 정수 입력
# 4. 집값 리스트를 오름차순으로 정렬
# 5. 누적 합을 계산하면서 B를 초과하면 그 직전 인덱스를 정답으로 설정
# 6. 주어진 양식에 맞춰 정답 출력

import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    N, B = map(int, input().split())
    houses = sorted(list(map(int, input().split())))
    ans = 0
    for j in range(N):
        if ans + houses[j] > B:
            print(f"Case #{i + 1}: {j}")
            break
        ans += houses[j]
    else:
        print(f"Case #{i + 1}: {N}")
