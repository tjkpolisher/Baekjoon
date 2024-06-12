# 17202: 핸드폰 번호 궁합
# 알고리즘 분류: 구현/다이나믹 프로그래밍/문자열/시뮬레이션

# 1. A의 번호 입력(단, 010과 하이픈은 제외)
# 2. B의 번호 입력(단, 010과 하이픈은 제외)
# 3. A의 번호 자릿수와 B의 번호 자릿수를 번갈아가며 배치한 새 숫자 생성
# 4. 첫번째 자릿수부터 시작해 다음 자릿수와 더해 일의 자릿수만 취함
# 5. 두 자리가 남을 때까지 반복
# 6. 정수를 출력(단, 십의 자리가 0이어도 앞에 0을 붙여 두자리로 출력해야 함)

import sys
input = sys.stdin.readline

a = list(input().rstrip().split('-'))
b = list(input().rstrip().split('-'))

a = ''.join(a)
b = ''.join(b)

number = ''
for i in range(len(a)):
    number += a[i]
    number += b[i]

while len(number) > 2:
    ans = ''
    for i in range(len(number) - 1):
        tmp = int(number[i]) + int(number[i + 1])
        ans += str(tmp)[-1]
    number = ans
print(number)
