# 15904: UCPC는 무엇의 약자일까?
# 출처: 전국 대학생 프로그래밍 대회 동아리 연합 UCPC 2018 예선 G번
# 알고리즘 분류: 그리디 알고리즘/문자열

# 1. 문자열 입력 (길이는 최대 1,000자, 문자열 맨 앞과 맨 끝에는 공백이 없고, 공백은 2번 이상 연속으로 주어지지 않음)
# 2. 글자들을 순회하면서 대문자만 별도의 리스트에 저장
# 3. 주어진 리스트에 저장된 글자들을 join
# 4. "UCPC"로 만들 수 있을 경우 "I love UCPC"를 출력, 아니면 "I hate UCPC" 출력

import sys
input = sys.stdin.readline

string = input().rstrip()
characters = []

flags = [False] * 4  # U, C, P, C가 입력되었는지를 나타내는 플래그
for i in range(len(string)):
    if string[i] == 'U' and not flags[0]:
        characters.append(string[i])
        flags[0] = True
    elif string[i] == 'C' and (flags[0] and not flags[1]):
        characters.append(string[i])
        flags[1] = True
    elif string[i] == 'P' and (flags[0] and flags[1] and not flags[2]):
        characters.append(string[i])
        flags[2] = True
    elif string[i] == 'C' and (flags[0] and flags[1] and flags[2] and not flags[3]):
        characters.append(string[i])
        flags[3] = True

ans = ''.join(characters)
if ans == 'UCPC':
    print("I love UCPC")
else:
    print("I hate UCPC")
