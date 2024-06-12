# 1448: 삼각형 만들기
# 알고리즘 분류: 수학/그리디 알고리즘/정렬

# 1. 빨대의 개수 N 입력 (3 ≤ N ≤ 1,000,000)
# 2. N개의 줄에 걸쳐 빨대의 길이 입력 (1,000,000 이하의 자연수)
# 3. 빨대의 길이 리스트 내림차순으로 정렬
# 4. 리스트 중 앞에서부터 두 원소를 고르고, 그 길이에 맞게 삼각형을 만들 수 있는 길이가 존재하는 지 탐색
# [보충설명] 삼각형이 만들어지려면, 가장 긴 변의 길이가 다른 두 변의 길이의 합보다 짧아야 함
# 5. 세 변의 길이의 합의 최대값을 출력하되, 만약 삼각형을 만들 수 없으면 -1 출력

import sys
input = sys.stdin.readline

N = int(input())
length = list()

for _ in range(N):
    length.append(int(input()))

length.sort(reverse=True)

ans = -1
for i in range(N - 2):
    l1 = length[i]
    l2 = length[i + 1]
    l3 = length[i + 2]
    if l1 < l2 + l3:
        ans = l1 + l2 + l3
        break

print(ans)
