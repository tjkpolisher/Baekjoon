# 10989: 수 정렬하기 3
# 특이사항: 언어 제한(node.js 금지), 시간 제한(5초), 메모리 제한(8MB)
# 알고리즘 분류: 정렬

# 1. 수의 개수 N 입력 (1 ≤ N ≤ 10,000,000)
# 2. N개의 줄에 걸쳐 수 입력

import sys
input = sys.stdin.readline

N = int(input())
cnt = [0] * 10001  # 각 수의 등장 횟수를 저장

# 등장하는 수마다 등장 횟수 증가
for _ in range(N):
    num = int(input())
    cnt[num] += 1

for i in range(10001):
    if cnt[i]:
        for j in range(cnt[i]):
            print(i)
