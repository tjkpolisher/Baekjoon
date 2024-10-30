# 6032: Toy Shopping
# 특이사항: 다국어(영어)
# 출처: USACO 2009-2010 Season February 2010 Contest Bronze 3번
# 알고리즘 분류: 그리디 알고리즘/정렬

# 1. 정수 N 입력 (3 ≤ N ≤ 25,000)
# 2. N개의 줄에 걸쳐 행복도 J_i와 가격 P_i 입력
# [보충설명] 0 ≤ J_i ≤ 1,000,000, 0 < P_i ≤ 100,000,000
# 3. HFM = J_i/P_i 기준으로 정렬
# 4. 정렬된 리스트에서 최대 HFM을 갖는 장난감의 가격 합을 출력
# 5. 최대 HFM을 기준으로 정렬된 장난감의 인덱스 + 1를 한 줄에 하나씩 출력

import sys
input = sys.stdin.readline

N = int(input())
HFM = []
for i in range(N):
    J_i, P_i = map(int, input().split())
    HFM.append([i, P_i, J_i/P_i])

HFM.sort(key=lambda x: x[2], reverse=True)
price = HFM[0][1] + HFM[1][1] + HFM[2][1]
print(price)
for i in range(3):
    print(HFM[i][0] + 1)
