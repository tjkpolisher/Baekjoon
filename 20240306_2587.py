# 2587: 대표값2
# 알고리즘 분류: 사칙연산/구현/수학/정렬

# 1. [반복문]다섯 개 줄에 걸쳐 한 줄에 하나씩 자연수 입력
# 2. 평균 및 중앙값 출력(한 줄에 하나씩)

nums = []
for _ in range(5):
    nums.append(int(input()))

nums.sort()
print(sum(nums) // 5)
print(nums[2])
