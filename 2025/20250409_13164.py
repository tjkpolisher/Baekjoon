# 13164: 행복 유치원
# 출처: UCPC 2016 F번
# 알고리즘 분류: 그리디 알고리즘/정렬

# 1. 유치원에 있는 원생의 수 N 입력 (1 ≤ N ≤ 300,000)
# 2. 나누려는 조의 개수 K 입력 (1 ≤ K ≤ N)
# 3. 원생들의 키를 나타내는 자연수 N개 입력 후 덱으로 구성(키는 오름차순으로 입력됨, 키는 10^9 이하의 자연수)
# 3-1. K >= N이거나 N = 1이면 각 그룹에 한 명씩 들어가므로 0 출력 후 종료
# 4. 인접한 원생 사이의 차이를 리스트에 저장
# 5. 모든 원생을 한 그룹에 묶었을 때의 비용에서 차이 리스트 중 가장 큰 K-1개의 차이를 빼서 출력

N, K = map(int, input().split())
heights = list(map(int, input().split()))  # 원생들의 키는 오름차순으로 정렬된 상태

if N == 1 or K >= N:
    print(0)
    exit()

diffs = []
for i in range(1, N):
    diffs.append(heights[i] - heights[i - 1])
diffs.sort(reverse=True)

ans = heights[-1] - heights[0] - sum(diffs[:K - 1])

print(ans)
