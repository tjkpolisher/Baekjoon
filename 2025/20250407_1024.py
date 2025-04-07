# 1024: 수열의 합
# 알고리즘 분류: 수학

# 1. 수열의 합 N, 수열의 최소 길이 L 입력 (N은 1,000,000,000 이하의 자연수, L은 2 이상 100 이하의 자연수)
# 2. 리스트의 길이를 L부터 시작해 1씩 늘려나가면서 아래 과정 적용
# [보충설명] 리스트의 각 원소는 음이 아닌 정수로, 모든 원소는 연속됨(원소 간 차이가 1이라는 뜻).
# 2-1. 초기항 a의 값의 범위를 start = N // size - size // 2부터 시작(size = L 이상의 자연수)
# 2-2. start부터 start + size까지의 a 값에 대해 부분합이 N과 같은지 판별
# 2-2. N과 같아지면 반복문 종료 후 초기항부터 1씩 커지는 원소들 생성 후 리스트에 저장
# 3-1. 길이가 100보다 크면 수열이 없으면 -1 출력
# 3-2. 그렇지 않으면 연속된 수를 공백으로 구분해 출력

N, L = map(int, input().split())


def partial_sum(n, a):
    return n * (2 * a + n - 1) // 2


for size in range(L, 101):
    ans_list = []
    start = max(N // size - size // 2, 0)
    for a in range(start, start + size + 1):
        if partial_sum(size, a) == N:
            ans_list = list(range(a, a + size))
            break
    if ans_list:
        print(*ans_list)
        break
else:
    print(-1)
