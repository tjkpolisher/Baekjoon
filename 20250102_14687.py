# 14687: High Tide, Low Tide
# 다국어: 영어
# 출처: CCC 2017 Senior Division 2번
# 알고리즘 분류: 구현/정렬

# 1. 정수 N 입력 (1 ≤ N ≤ 100)
# 2. N개의 정수 입력 (각 정수는 최대 1,000,000)
# [보충설명] low tide일 때부터 측정 시작, 두 번째 측정은 high tide, 이후부터는 두 tide가 번갈아가며 나옴
# [보충설명] 모든 high tide는 low tide 측정값보다 큼
# [보충설명] 시간이 흐름에 따라 high tide 값들은 점점 커지고, low tide 값들은 점점 작아짐.
# 3. 입력받은 정수들을 오름차순으로 정렬한 뒤, 반으로 분할
# [보충설명] N이 짝수일 때는 절반으로, 홀수일 때는 첫 번째 리스트가 두 번째 리스트의 원소보다 1개 더 많도록 분할
# 4. 첫 번째 리스트(low tide)를 내림차순으로, 두 번째 리스트(high tide)를 오름차순으로 정렬
# 5. low tide 리스트와 high tide 리스트의 원소를 번갈아가면서 출력

N = int(input())
tides = sorted(list(map(int, input().split())))
low_tide = tides[:N // 2 + N % 2]
high_tide = tides[N // 2 + N % 2:]
low_tide.reverse()

for i in range(N // 2):
    print(low_tide[i], high_tide[i], end=' ')
if N % 2 == 1:
    print(low_tide[-1])
