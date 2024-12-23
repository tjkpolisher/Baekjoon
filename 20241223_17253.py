# 17253: 삼삼한 수 2
# 출처: 2019 전북대학교 프로그래밍 경진대회 J번
# 알고리즘 분류: 수학

# 1. 9,223,372,036,854,775,807보다 작거나 같은 음이 아닌 정수 N 입력
# 2. 주어진 N 이하의 가장 큰 3의 거듭제곱을 먼저 찾아서 N에서 빼기
# 3. 다음으로 작은 3의 거듭제곱을 찾아서 N에서 뺄 수 있는지 판단
# 3-1. 거듭제곱이 N보다 작거나 같으면 해당 거듭제곱만큼 N에서 빼고 다음 단계 진행
# 3-2. N보다 크면 바로 다음 거듭제곱으로 이행하여 진행
# 4. 가장 작은 거듭제곱까지 진행해서 N이 남아있으면 NO, 0이 남아있으면 YES 출력

N = int(input())
if N == 0:
    print("NO")
    exit(0)

exponent = 1  # 3의 거듭제곱의 지수
while 3 ** exponent <= N:
    exponent += 1
exponent -= 1

while True:
    c = int(3 ** exponent)
    if c <= N:
        N -= c
    exponent -= 1
    if exponent < 0 or N <= 0:
        break

if N:
    print("NO")
else:
    print("YES")
