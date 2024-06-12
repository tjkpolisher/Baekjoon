# 25631: 마트료시카 합치기
# 알고리즘 분류: 자료 구조/그리디 알고리즘/정렬

# 1. 마트료시카의 개수 N 입력 (1 ≤ N ≤ 1000)
# 2. 마트료시카의 크기 N개 입력
# 3. 크기를 오름차순으로 정렬
# 4. 리스트를 집합으로 만든 별도의 set을 만든 뒤, 집합 내 원소들을 차례대로 삭제
# 5. 같은 숫자가 모두 삭제되면 카운터에 1을 더함
# 6. 카운터 출력

import sys
input = sys.stdin.readline

N = int(input().rstrip())
sizes = list(map(int, input().rstrip().split()))
sizes.sort()

cnt = 0
while sizes:
    sizes_set = set(sizes)
    for n in sizes_set:
        del sizes[sizes.index(n)]
    cnt += 1

print(cnt)
