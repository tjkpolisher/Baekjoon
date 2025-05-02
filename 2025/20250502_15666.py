# 15666: N과 M (12)
# 알고리즘 분류

# 1. 두 자연수 N과 M 입력 (1 ≤ M ≤ N ≤ 8)
# 2. N개의 수를 공백으로 구분해 입력 (입력되는 수는 10,000 이하의 자연수)
# 3. 입력받은 수를 리스트에 넣고 오름차순으로 정렬
# 4. 첫 번째 수부터 시작해 재귀적으로 다음의 함수 실행
# 4-1. 종료 조건: 리스트의 길이가 M이면 함수 종료 후 정답 리스트를 한 줄에 출력
# 4-2. 리스트의 현재 인덱스의 수가 이전 수보다 크거나 같으면 정답 리스트에 append

import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
ans = []
ans_set = []


def answer(idx, ans):
    if len(ans) == M:
        print(*ans)
        return
    for i in range(idx, N):
        if ans + [numbers[i]] in ans_set:
            continue
        ans_set.append(ans + [numbers[i]])
        answer(i, ans + [numbers[i]])
    return


answer(0, ans)
