# 1302: 베스트셀러
# 알고리즘 분류: 자료 구조/문자열/정렬/해시를 사용한 집합과 맵

# 1. 책의 개수 N 입력 (1 ≤ N ≤ 1,000)
# 2. N개의 줄에 걸쳐 책의 제목 입력

import sys
input = sys.stdin.readline
book_sell = dict()

N = int(input())
for _ in range(N):
    book = input().rstrip()
    if book not in book_sell:
        book_sell[book] = 1
    else:
        book_sell[book] += 1

book_sell_list = list(book_sell.items())
book_sell_list.sort(key=lambda x: (-x[1], x[0]))
print(book_sell_list[0][0])
