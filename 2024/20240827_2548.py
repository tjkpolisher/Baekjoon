# 2548: 대표 자연수
# 출처: KOI 2009 초등부 1번
# 알고리즘 분류: 브루트포스 알고리즘/정렬

# 1. 자연수의 개수 N 입력 (1 ≤ N ≤ 20,000)
# 2. N개의 자연수가 공백으로 구분되어 입력(자연수는 1 이상 10,000 이하)
# 3. 자연수를 오름차순으로 정렬
# 4. 맨 앞 자연수부터 시작해, 나머지 자연수와의 차의 합을 구함
# 5. 차이가 이전보다 작을 경우 대표 자연수를 현재의 대표 자연수와 지금 인덱스의 자연수 중 작은 것으로 교체

import sys
input = sys.stdin.readline

N = int(input())
natural_numbers = list(map(int, input().split()))
natural_numbers.sort()

ans = 20000
diff = 20000 ** 2
for i in range(N):
    diff_cur = 0
    n = natural_numbers[i]
    for j in range(N):
        diff_cur += abs(n - natural_numbers[j])
        if diff_cur > diff:
            break
    if diff_cur > diff:
        continue
    if diff_cur == diff:
        diff = diff_cur
        ans = min(n, ans)
    elif diff_cur < diff:
        diff = diff_cur
        ans = n
print(ans)

"""
더 빠른 코드
출처: baekjoon - mgu3495님의 풀이

n = int(input())
L = list(map(int,input().split()))
L.sort()
left, right = divmod(n, 2)
print(L[left+right-1])
"""
