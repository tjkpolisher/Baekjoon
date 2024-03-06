# 2750: 수 정렬하기
# 알고리즘 분류: 구현/정렬

# 1. 수의 개수 N 입력
# 2. [반복문] N개의 줄에 걸쳐 수 입력(중복 없음)
# 3. 리스트 오름차순으로 정렬 후 첫 번째 원소부터 출력

N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))

for n in sorted(nums):
    print(n)
