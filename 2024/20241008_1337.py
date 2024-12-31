# 1337: 올바른 배열
# 알고리즘 분류: 구현/정렬/두 포인터

# 1. 배열의 크기 N 입력 (N은 50 이하의 자연수)
# 2. N개의 줄에 걸쳐 배열의 원소가 한 줄에 하나씩 입력
# [보충설명] 원소는 1,000,000,000보다 작거나 같은 음이 아닌 정수, 원소는 중복되지 않음
# 3. 배열을 오름차순으로 정렬
# 4. 배열을 순회하면서 해당 원소부터 해당 원소 + 5까지의 숫자가 배열에 있는지 확인
# 4-1. 배열에 없는 수의 개수만큼 temp라는 리스트에 저장
# 5. 리스트의 최소값 출력

import sys
input = sys.stdin.readline

N = int(input())
array = []
for _ in range(N):
    array.append(int(input()))

array.sort()

temp = []
for i in range(N):
    cnt = 0
    for j in range(array[i], array[i] + 5):
        if j not in array:
            cnt += 1
    temp.append(cnt)

print(min(temp))
