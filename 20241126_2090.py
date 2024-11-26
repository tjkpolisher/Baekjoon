# 2090: 조화평균
# 알고리즘 분류: 수학/구현/정수론/유클리드 호제법

# 1. 자연수 N 입력 (1 ≤ N ≤ 9)
# 2. N개의 자연수를 공백으로 구분해 입력 후 리스트에 저장
# 3. 입력받은 수들의 조화 평균을 구한 뒤, 분수 형태로 변환해 출력
# [보충설명] 이 문제 한정으로 조화 평균은 1/(1/A[1] + 1/A[2] + … + 1/A[N])으로 계산해야 함!

from fractions import Fraction

N = int(input())
numbers = list(map(int, input().split()))

numbers_fraction_sum = [Fraction(1, numbers[i]) for i in range(N)]

if len(numbers_fraction_sum) > 1:
    harmony_average = Fraction(1, sum(numbers_fraction_sum))
    print(harmony_average)
else:
    print(f"{numbers[0]}/1")
