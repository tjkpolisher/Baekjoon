# 1418: K-세준수
# 알고리즘 분류: 수학/브루트포스 알고리즘/정수론/소수 판정/에라토스테네스의 체

# 1. N 입력
# 2. K 입력
# 3. [반복문]
# 3-1. 1부터 N까지의 자연수에 대한 소인수를 구함
# 3-2. 3-1에서 구한 소인수 중 K보다 크지 않은 수를 카운팅
# 4. 3에서 구한 K-세준수의 개수 출력

N = int(input())
K = int(input())
prime_factors = set(range(2, N + 1))

for i in range(2, N + 1):
    multiple = set(range(2 * i, N + 1, i))
    prime_factors -= multiple

# N보다 작으면서 K 이상인 소수의 배수들은 K-세준수가 아님
nums = [1] * (N + 1)
for i in range(2, N + 1):
    if i in prime_factors and i > K:
        for j in range(i, N + 1, i):
            nums[j] = 0

print(sum(nums) - 1)
