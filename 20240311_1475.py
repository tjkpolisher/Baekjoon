# 1475: 방 번호
# 알고리즘 분류: 구현

# 1. 방 번호 N 입력
# 2. N의 각 자릿수를 분해한 후 그 수를 집계
# 3. 6의 개수와 9의 개수는 합하고 2로 나누고 소수점 아래를 올림
# 4. 각 자릿수의 개수 중 최대값을 출력

import math
N_list = list(map(int, input()))
nums = dict()
for n in N_list:
    if n not in nums:
        nums[n] = 1
    else:
        nums[n] += 1

if 6 in nums and 9 in nums:
    nums[6] += nums[9]
    del nums[9]
    nums[6] = math.ceil(nums[6] / 2)
elif 6 in nums:
    nums[6] = math.ceil(nums[6] / 2)
elif 9 in nums:
    nums[9] = math.ceil(nums[9] / 2)

print(max(nums.values()))
