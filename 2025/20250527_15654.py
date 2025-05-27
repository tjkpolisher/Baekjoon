# 15654: N과 M (5)
# 알고리즘 분류: 백트래킹

# 1. 두 자연수 N, M 입력 (1 ≤ M ≤ N ≤ 8)
# 2. N개의 수 입력 후 리스트에 저장 (10,000 이하의 자연수)
# 3. 리스트의 수를 오름차순으로 정렬
# 4. 첫 번째 수부터 시작해 하나씩 정답 리스트에 넣었다 빼는 과정을 재귀적으로 수행
# 5. 종료 조건: 정답 리스트의 길이가 M이 될 때 출력 후 종료료

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
sequence = list(map(int, input().split()))

sequence.sort()
answer = []


def backtrack():
    if len(answer) == M:
        print(' '.join(map(str, answer)))
        return

    for i in range(N):
        next = sequence[i]
        if next in answer:
            continue
        answer.append(next)
        backtrack()
        answer.pop()


backtrack()
