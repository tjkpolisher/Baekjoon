# 1676: 팩토리얼 0의 개수
# 알고리즘 분류: 수학

# 1. 정수 N 입력
# 1-1. N이 4 이하면 0 반환 후 종료
# 2. 팩토리얼 N 계산
# 3. 2에서 계산한 결과를 문자열화 후 뒤집기
# 4. 두 문자열의 길이를 뺀 후 출력

from math import factorial
N = int(input())
if N <= 4:
    print(0)
else:
    f = str(factorial(N))
    length = len(f)
    f_flipped = str(int(f[::-1]))
    length_f = len(f_flipped)
    print(length - length_f)
