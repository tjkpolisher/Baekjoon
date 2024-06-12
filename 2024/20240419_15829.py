# 15829: Hashing
# 특이사항: 서브태스크
# 알고리즘 분류: 구현/문자열/해싱
# 출처: 아주대학교 2018 Ajou Programming Contest - Division 2 C번

# 1. 문자열의 길이 L 입력
# 2. 문자열 입력(영문 소문자로만 구성)
# 3. 해시 함수 연산(r = 31, M = 1,234,567,891)
# 3-1. 연산식: H = sum(a_i * r_i) % M
# 4. 해시값을 정수로 출력

import sys
input = sys.stdin.readline

L = int(input())
string = input().rstrip()
characters = "abcdefghijklmnopqrstuvwxyz"
c_to_a = {characters[i]: i + 1 for i in range(len(characters))}
r = 31
result = 0
M = 1234567891
for i, c in enumerate(string):
    a = c_to_a[c]
    result += (a * r ** i)

result %= M
print(result)
