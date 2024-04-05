# 17393: 다이나믹 롤러
# 유의사항: 각 타일은 잉크지수와 점도지수를 가짐
# i번째 타일에 서 있을 때, 현재 위치보다 오른쪽에 있으면서
# 현재 타일의 잉크지수보다 점도지수가 낮거나 같은 칸을 칠할 수 있음
# Pypy3로 풀면 3336ms → 712ms로 시간 단축이 가능합니다.
# 알고리즘 분류: 이분 탐색

# 1. 통로의 길이 N 입력
# 2. 각 칸의 잉크지수 N개 입력
# 3. 각 칸의 점도지수 N개 입력(오름차순임)
# 4. 칠할 수 있는 칸의 개수를 담을 result 리스트 생성
# 5.[반복문]
# 5-1. 이진 탐색을 실시해 현재 타일의 잉크지수가 i번째 점도지수보다 커지는 지점을 찾기
# 5-2. 해당 인덱스까지의 원소의 개수를 result에 append
# 6. result의 원소 출력

import sys
input = sys.stdin.readline

N = int(input())
a = list(map(int, input().rstrip().split()))  # 잉크지수
b = list(map(int, input().rstrip().split()))  # 점도지수
result = []


for i in range(N):
    idx = a[i]
    start, end = i + 1, N - 1
    ans = i
    while start <= end:
        mid = (start + end) // 2
        if idx < b[mid]:
            end = mid - 1
        else:
            start = mid + 1
            ans = mid
    result.append(str(ans - i))

print(' '.join(result))
