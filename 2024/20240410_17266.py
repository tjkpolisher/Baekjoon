# 17266: 어두운 굴다리
# 알고리즘 분류: 구현/이분 탐색

# 1. 굴다리의 길이 N 입력
# 2. 가로등의 개수 M 입력
# 3. M개의 가로등의 위치 입력
# 4-1. 가로등이 한 개라면 가로등으로부터 끝점까지의 거리 중 더 긴 거리를 선택
# 4-2. 가로등이 여러 개일 때
# 4-2-1. 가로등 사이의 거리가 홀수일 경우, 거리를 2로 나눈 몫에 1을 더함
# 4-2-2. 짝수일 경우 거리를 2로 나눈 몫을 그대로 취함
# 4-2-3. 단, 마지막 가로등일 경우에는 N에서 가로등 위치를 뺌
# 4-2-4. 위 분기를 거치면서 얻은 값과 이전까지 가장 높은 가로등 높이 중 최대값을 취함
# 5. 가로등 높이 출력

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
lamps = list(map(int, input().split()))

if M == 1:
    height = max(lamps[0], N - lamps[0])
else:
    height = lamps[0]
    for i in range(M):
        # 마지막 가로등일 때
        if i == M - 1:
            tmp = N - lamps[-1]
        # 나머지 가로등
        else:
            distance = lamps[i + 1] - lamps[i]
            # 가로등 사이의 거리가 홀수일 경우, 가로등이 1만큼 더 높아야 모든 거리를 비출 수 있음
            # 짝수일 경우는 그대로 가져가도 무방
            tmp = distance // 2 + 1 if distance % 2 == 1 else distance // 2

        height = max(height, tmp)

print(height)
