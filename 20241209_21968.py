# 21968: 선린의 터를
# 출처: 선린인터넷고등학교 제5회 천하제일 코딩대회 예선 E번
# 알고리즘 분류: 수학/정수론/비트마스킹

# 1. 찾아야 하는 선린의 터의 개수 T 입력 (1 ≤ T ≤ 2000)
# 2. T개의 줄에 걸쳐 찾아야 하는 선린의 터에 대한 정보 N 입력 (1 ≤ N ≤ 123,456,789,123)
# 3. N을 이진수로 표현한 뒤, 그 이진 표현을 3진법으로 해석

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    N_bin = bin(N)[2:]
    ans = int(N_bin, 3)
    print(ans)
