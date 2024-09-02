# 15739: 매직스퀘어
# 출처: 한양대학교 ERICA 캠퍼스 2018 HEPC PRIME 3번
# 알고리즘 분류: 구현

# 1. N 입력 (3 ≤ N ≤ 100)
# 2. N개의 줄에 걸쳐 N개의 숫자 입력 (수의 범위는 1 이상 N^2 이하)
# 3. 입력받은 숫자 중 중복되는 수가 있으면 FALSE 출력 후 종료
# 3-1. 동시에 입력받은 가로 행의 합이 n * (n^2 + 1) / 2과 다르면 FALSE 출력 후 종료(가로 조건 충족 x)
# 4. 입력받은 숫자 중 두 대각선에 해당되는 인덱스를 가진 원소를 따로 저장
# 5. 세로, 두 대각선의 수열의 합을 n * (n^2 + 1) / 2로 계산
# 6. 합이 모두 같다면 TRUE, 그렇지 않다면 FALSE 출력 후 종료

N = int(input())
matrix = []
diag1 = 0
diag2 = 0
nums = set()
sum_result = N * (N ** 2 + 1) // 2
broken = False

for i in range(N):
    N_i = list(map(int, input().split()))
    if sum(N_i) != sum_result:
        broken = True
    for num in N_i:
        if num < 1 or num > N ** 2 or num in nums:
            broken = True
        nums.add(num)
    matrix.append(N_i)
    diag1 += N_i[i]
    diag2 += N_i[N - i - 1]

for i in range(N):
    vertical_sum = 0
    for j in range(N):
        vertical_sum += matrix[i][j]
    if vertical_sum != sum_result:
        broken = True

if broken or diag1 != sum_result or diag2 != sum_result:
    print("FALSE")
else:
    print("TRUE")
