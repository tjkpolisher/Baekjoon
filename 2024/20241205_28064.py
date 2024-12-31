# 28064: 이민희진
# 출처: 서강대학교 2023 청정수컵 Open Contest D번
# 알고리즘 분류: 문자열/브루트포스 알고리즘

# 1. 사람의 수 N 입력 (1 ≤ N ≤ 100)
# 2. N개의 줄에 걸쳐 사람의 이름 입력 후 리스트에 저장 (이름은 소문자, 최소 1자, 최대 20자)
# 3. 리스트의 이름 중 2개를 뽑는 조합을 생성한 뒤, 각 조합의 문자열 S, T 선택
# 4. S, T의 길이 중 최소값을 k로 지정
# 5. S의 앞쪽 k개 글자와 T의 뒤쪽 k개 글자가 일치 또는 S의 뒤쪽 k글자와 T의 앞쪽 k글자가 같으면 카운터에 1을 더함
# 6. 모든 조합을 시험할 때까지 3~5를 반복
# 7. 카운터 개수 출력

import sys
from itertools import combinations
input = sys.stdin.readline

N = int(input())
names = []
for _ in range(N):
    names.append(input().rstrip())

combs = combinations(names, 2)

ans = 0
for comb in combs:
    S, T = comb
    k = min(len(S), len(T))
    for i in range(1, k + 1):
        if S[:i] == T[-i:] or S[-i:] == T[:i]:
            ans += 1
            break

print(ans)
