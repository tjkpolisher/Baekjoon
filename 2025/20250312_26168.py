# 26168: 배열 전체 탐색하기
# 특이사항: 서브태스크
# 알고리즘 분류: 정렬/이분 탐색

# 1. 배열의 크기 n, 질의의 개수 m 입력
# 2. n개의 A의 원소 입력 후 리스트 정렬
# 3. m개의 줄에 걸쳐 m개의 질의를 순서대로 입력
# 4. 입력받은 질의를 split 후, 타입에 따라 이진 탐색을 통해 해당 원소의 개수를 구하는 연산 수행
# 4-1. 1번 유형: A의 원소 중 k보다 크거나 같은 원소의 개수 출력
# 4-2. 2번 유형: A의 원소 중 k보다 큰 원소의 개수 출력
# 4-3. 3번 유형: A의 원소 중 i보다 크거나 같고 j보다 작거나 같은 원소의 개수 출력

import sys
import bisect
input = sys.stdin.readline

n, m = map(int, input().split())
A = sorted(list(map(int, input().split())))

for _ in range(m):
    query = input().rstrip().split()
    qtype = query[0]

    if qtype == "1":
        k = int(query[1])
        result = n - bisect.bisect_right(A, k - 1)
    elif qtype == "2":
        k = int(query[1])
        result = n - bisect.bisect_right(A, k)
    else:
        i = int(query[1])
        j = int(query[2])
        result = bisect.bisect_right(A, j) - bisect.bisect_left(A, i)

    print(result)
