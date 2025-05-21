# 2212: 센서
# 출처: ICPC Seoul Nationalwide Internet Competition 2005 E번
# 알고리즘 분류

# 1. 센서의 개수 N 입력 (1 ≤ N ≤ 10000)
# 2. 집중국의 개수 K 입력 (1 ≤ K ≤ 1000)
# 3. 센서의 좌표를 나타내는 N개의 정수 입력(좌표의 절대값은 1,000,000 이하)
# 3-1. K가 센서의 개수보다 크거나 같으면 0 출력 후 종료
# 4. 센서의 좌표를 오름차순으로 정렬
# 5. 인접한 센서들의 거리의 차이를 계산해 리스트에 저장
# 6. 거리 리스트를 내림차순으로 정렬
# 7. K-1번째 인덱스부터 끝까지의 거리 합을 출력

import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
sensors = list(map(int, input().split()))
# K가 센서의 개수보다 크거나 같으면 0 출력 후 종료
if K >= N:
    print(0)
    exit()

sensors.sort()

distances = []
for i in range(1, N):
    distances.append(sensors[i] - sensors[i - 1])
distances.sort(reverse=True)

print(sum(distances[K - 1:]))
