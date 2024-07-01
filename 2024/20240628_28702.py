# 28702: FizzBuzz
# 특이사항: 스페셜 저지, 다국어(영어)(한국어 번역)
# 출처: solved.ac Grand Arena #2 B번
# 알고리즘 분류: 수학/문자열

# 1. 세 줄에 걸쳐 문자열을 한 개씩 총 세 개 입력(길이는 각각 8 이하)
# 2. 각 문자열이 아래 규칙에 해당되는 지에 따라 번호 유추
# 2-1. 'Fizz'인 경우 3의 배수이지만 5의 배수가 아님
# 2-2. 'Buzz'인 경우 3의 배수가 아니지만 5의 배수임
# 2-3. 'FizzBuzz'인 경우 3의 배수이고 5의 배수임
# 2-4. 아무 것에도 대응되지 않는 경우 숫자가 몇 번째인지를 나타내는 수 i를 그대로 출력
# 3. 세 문자열 다음에 올 문자열 출력(단, 여러 문자열이 올 수 있는 경우 아무거나 하나 출력)

import sys
input = sys.stdin.readline

for i in range(3, 0, -1):
    x = input().rstrip()
    if x not in ['Fizz', 'Buzz', 'FizzBuzz']:
        n = int(x) + i

if n % 3 == 0 and n % 5 == 0:
    print('FizzBuzz')
elif n % 3 == 0:
    print('Fizz')
elif n % 5 == 0:
    print('Buzz')
else:
    print(n)
