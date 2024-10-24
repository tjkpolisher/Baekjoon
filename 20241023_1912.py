# 1912: 연속합
# 알고리즘 분류: 다이나믹 프로그래밍

# 1. 정수 n 입력 (1 ≤ n ≤ 100,000)
# 2. n개의 정수로 이루어진 수열 입력 (수열에 들어있는 수는 -1000 이상 1000 이하)
# 3. 첫 번째 수부터 마지막 수까지 누적 합을 계산해 리스트에 저장
# 3-1. 단, 현재 인덱스에 들어갈 누적합이 수열의 현재 원소보다 작을 경우, 그 누적합 대신 원소 자체를 저장
# 4. 리스트의 최대값을 출력

n = int(input())
sequence = list(map(int, input().split()))

# 누적 합 계산
prefix = [0 for _ in range(n)]
prefix[0] = sequence[0]
for i in range(n - 1):
    prefix[i + 1] = max(prefix[i] + sequence[i + 1], sequence[i + 1])

print(max(prefix))
