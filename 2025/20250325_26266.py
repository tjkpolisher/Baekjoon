# 26266: 비즈네르 암호 해독
# 출처: 2022 서울사이버대학교 프로그래밍 경진대회 (SCUPC) C번
# 알고리즘 분류: 수학/문자열/브루트포스 알고리즘/정수론

# 1. 알파벳 - 숫자로 구성된 딕셔너리 생성
# 2. 알파벳 대문자로 구성된 평문 입력 (길이는 200,000 이하)
# 3. 평문에 대한 (알파벳 대문자로 구성된) 비즈네르 암호문 입력 (길이는 평문과 동일)
# 4. 딕셔너리를 참조해 평문과 암호문을 숫자로 변환
# 5. 변환된 숫자에서 암호문 숫자 - 평문 숫자를 각각 계산
# 5-1. 차이가 0 이하일 경우 그 결과에 26을 더해줌
# 6. 변환된 키를 join해서 문자열로 변환
# 7. 변환된 문자열에서 반복되는 패턴을 찾아 최소 길이의 키로 변환
# 8. 키를 출력

import sys
input = sys.stdin.readline

alphabet_table = {chr(i + 65): i + 1 for i in range(26)}

original = input().rstrip()
biznerre = input().rstrip()


def to_list(string):
    return [alphabet_table[c] for c in string]


def decypher(n, b):
    diff = b - n
    if diff <= 0:
        diff += 26
    return diff


original_list = to_list(original)
biznerre_list = to_list(biznerre)

key = []
n = len(original)
for i in range(n):
    key.append(chr(64 + decypher(original_list[i], biznerre_list[i])))

ans_tmp = ''.join(key)

for i in range(1, n // 2 + 1):
    if n % i != 0:
        continue

    repeat_str = ans_tmp[:i]
    if repeat_str * (n // i) == ans_tmp:
        print(repeat_str)
        break
else:
    print(ans_tmp)
