# 2003: 수들의 합 2
# 알고리즘 분류: 브루트포스 알고리즘/누적 합/두 포인터

# 1. 수열의 길이 N, 목표값 M 입력 (1 ≤ N ≤ 10,000, 1 ≤ M ≤ 300,000,000)
# 2. 수열 A의 원소 N개를 입력받고 리스트에 저장 (수열의 원소는 30,000 이하의 자연수)
# 3. 투 포인터를 구성해 부분 합 구성
# 3-1. 부분 합이 M을 초과할 경우 다음 인덱스로 이동 후 3-1을 반복
# 3-2. 그렇지 않으면 두번째 포인터를 이동할 때마다 현재 부분 합에 포인터가 가리키는 변수를 더함
# 3-3. 정확히 M이 될 경우 카운터에 1을 더한 후 루프 종료
# 4. 카운터 출력

N, M = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0
for i in range(N):
    suffix_sum = 0
    for j in range(i, N):
        suffix_sum += A[j]
        if suffix_sum == M:
            cnt += 1
            break
        elif suffix_sum > M:
            break
    else:
        if suffix_sum < M:
            break
print(cnt)
