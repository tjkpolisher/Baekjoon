# 1747: 소수&팰린드롬
# 알고리즘 분류: 수학/브루트포스 알고리즘/정수론/소수 판정/에라토스테네스의 체

# 1. 정수 N 입력 (1 ≤ N ≤ 1,000,000)
# 2. N 이하인 소수를 연산해 집합에 저장
# 3. 집합에 저장된 소수 중 가장 큰 수를 확인
# 4. 소수 여부를 확인
# 4-1. 소수일 경우 팰린드롬인지 확인
# 4-2. 소수이면서 팰린드롬일 경우 그 수를 출력 후 종료
# 4-3. 그렇지 않으며 수를 1씩 더해가면서 4-1과 4-2를 반복

N = int(input())
if N == 1:
    print(2)
    exit()

# 소수만 남기는 집합 연산
prime = set(range(2, N + 1))
for i in range(2, int((N + 1) ** 0.5) + 1):
    if i in prime:
        prime -= set(range(2 * i, N + 1, i))


def is_prime(num):
    for i in range(2, int(num ** 0.5 + 1)):
        if num % i == 0:
            return False
    return True


tmp = N
while True:
    if is_prime(tmp):
        prime.add(tmp)

    str_tmp = str(tmp)
    if str_tmp == str_tmp[::-1] and tmp in prime:
        print(tmp)
        break
    tmp += 1
