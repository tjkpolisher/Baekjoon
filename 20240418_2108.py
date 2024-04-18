# 2108: 통계학
# 알고리즘 분류: 수학/구현/정렬

# 1. 수의 개수 N 입력 (1 ≤ N ≤ 500,000이며 N은 홀수)
# 2. N개의 줄에 걸쳐 리스트에 정수 입력(정수의 절대값은 4,000 이하) 및 정수와 그 개수를 해시 테이블에 입력
# 3. 리스트 오름차순으로 정렬
# 4. 산술 평균을 소수점 이하 첫째 자리에서 반올림해 출력
# 5. 중앙값 탐색 후 출력
# 6. 해시 테이블의 최대값을 최빈값으로 출력
# 7. 최대값 및 최소값의 차이 출력

import sys
input = sys.stdin.readline

N = int(input())
numbers = []
numbers_table = dict()
for _ in range(N):
    n = int(input())
    numbers.append(n)
    if n not in numbers_table:
        numbers_table[n] = 1
    else:
        numbers_table[n] += 1

numbers = sorted(numbers)
# 산술 평균
print(int(round(sum(numbers) / N)))
# 중앙값
print(numbers[N // 2])
# 최빈값
f = max(numbers_table.values())
f_list = []
for i in numbers_table:
    if f == numbers_table[i]:
        f_list.append(i)
f_list.sort()
if len(f_list) > 1:
    print(f_list[1])
else:
    print(f_list[0])
# 범위
print(numbers[-1] - numbers[0])
