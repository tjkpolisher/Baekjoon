# 1654: 랜선 자르기
# 알고리즘 분류: 이분 탐색/매개 변수 탐색

# 1. 이미 가지고 있는 랜선의 개수 K, 필요한 랜선의 개수 N 입력 (K ≤ N)
# 2. K줄에 걸쳐 이미 가지고 있는 랜선의 길이가 cm 단위의 정수로 입력
# 3. 1에서 최대 길이까지의 범위에서 랜선 개수에 대한 이진 탐색 진행
# 4. 이진 탐색이 종료되면 끝점의 길이 출력

import sys
K, N = map(int, input().split())
lan = []
for _ in range(K):
    lan.append(int(sys.stdin.readline().rstrip()))

start = 1
end = max(lan)

while start <= end:
    mid = (start + end) // 2
    lines = 0
    for i in lan:
        lines += (i // mid)

    if lines >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)
