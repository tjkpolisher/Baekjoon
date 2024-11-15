# 21921: 블로그
# 알고리즘 분류: 누적 합/슬라이딩 윈도우

# 1. 블로그 시작 후 지난 일수 N과 X 입력 (1 ≤ X ≤ N ≤ 250,000)
# 2. 시작 1일차부터 N일차까지의 하루 방문자 수 입력 후 리스트에 저장
# [보충설명] 0 ≤ 방문자 수 ≤ 8,000
# 3. 첫 번째 원소부터 시작해 해당 인덱스로부터 X번째 인덱스까지의 부분합을 구해 초기화
# 4. 인덱스 i + X번의 원소를 부분합에 더함
# 5. 다음 인덱스로 넘어가기 전 기존 인덱스 i의 원소만큼을 부분합에서 뺌
# 6. 부분합과 현재의 정답 중 최대값으로 정답을 갱신하고 딕셔너리에 그 정답의 횟수를 저장
# 7. 정답을 출력하되, 0명이라면 SAD를 출력
# 8. 최대 방문자 수가 0명이 아닌 경우, 다음 줄에 그러한 기간이 몇 개 있는지 출력

N, X = map(int, input().split())
visitor = list(map(int, input().split()))
sum_visitor = {}
answer = 0
partial_sum = sum(visitor[:X - 1])

for i in range(N - X + 1):
    partial_sum += visitor[i + X - 1]

    if partial_sum not in sum_visitor:
        sum_visitor[partial_sum] = 1
    else:
        sum_visitor[partial_sum] += 1

    if answer < partial_sum:
        answer = partial_sum
    partial_sum -= visitor[i]

if not answer:
    print('SAD')
else:
    print(answer)
    print(sum_visitor[answer])
