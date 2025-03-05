# 12892: 생일 선물
# 알고리즘 분류: 정렬/두 포인터

# 1. 친구의 수 N, 미안함을 느끼는 최소가격차 D 입력 (1 ≤ N ≤ 100,000, 1 ≤ D ≤ 1,000,000,000)
# 2. N개의 줄에 걸쳐 각 선물의 가격 P와 만족도 V 입력 (0 ≤ P ≤ 1,000,000,000, 0 ≤ V ≤ 1,000,000,001)
# 3. 입력받은 P와 V를 가격 순으로 오름차순 정렬
# 4. 투 포인터를 이용해 p2 가격 - p1 가격이 D 미만일 경우 만족도를 임시 변수 tmp에 더하기
# 5. D 이상이 되면 정답을 max(ans, tmp)로 갱신
# 6. 두 번째 포인터가 N이 되면 종료 후, 정답을 한 번 더 갱신
# 7. 정답 출력

import sys
input = sys.stdin.readline

N, D = map(int, input().split())
gift = []
for _ in range(N):
    P, V = map(int, input().split())
    gift.append((P, V))

gift.sort(key=lambda x: x[0])

ans = 0  # 정답(실제 만족도)
tmp = 0  # 만족도를 저장하는 임시 변수
i = 0  # 포인터 1
j = 0  # 포인터 2

while j < N:
    if gift[j][0] - gift[i][0] < D:
        tmp += gift[j][1]
        j += 1
    else:
        ans = max(ans, tmp)
        p = gift[j][0] - D + 1
        while p > gift[i][0]:
            tmp -= gift[i][1]
            i += 1

ans = max(ans, tmp)
print(ans)
