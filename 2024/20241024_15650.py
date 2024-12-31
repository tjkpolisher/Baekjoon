# 15650: N과 M (2)
# 알고리즘 분류: 백트래킹

# 1. 자연수 N과 M 입력 (1 ≤ M ≤ N ≤ 8)
# 2. 1부터 시작해 원소를 1씩 증가시키며 수열 구성
# 3. M개가 구성되면 수열을 출력하고, 수가 모자라면
# 3-1. 단, 수열 리스트에 이미 해당 수가 들어 있거나, 오름차순을 만족하지 못하면 continue

N, M = map(int, input().split())
arr = []


def recur(number, output: list):
    if number == M:
        print(*output)
        return

    for i in range(1, N + 1):
        if i in output or (output and i < output[-1]):
            continue
        output.append(i)
        recur(number + 1, output)
        output.pop()  # 재귀 함수 종료 후 출력할 리스트를 원상 복구


recur(0, arr)
