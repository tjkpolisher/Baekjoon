# 1929: 소수 구하기
# 알고리즘 분류: 수학/정수론/소수 판정/에라토스테네스의 체

# 1. 두 자연수 M과 N 입력 (1 ≤ M ≤ N ≤ 1,000,000)
# 2. M부터 N까지의 자연수를 가진 집합 입력
# 3. 집합 연산을 통해 2부터 N까지의 소수가 아닌 수를 걸러내는 차집합 연산 수행
# 4. 소수 정렬 후 출력

M, N = map(int, input().split())
number_set = set(range(M, N + 1))
if 1 in number_set:
    number_set -= set([1])

for i in range(2, N + 1):
    prime_numbers = set(range(i * 2, N + 1, i))
    number_set -= prime_numbers

number_set = list(number_set)
number_set.sort()
for n in number_set:
    print(n)
