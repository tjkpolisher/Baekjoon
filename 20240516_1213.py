# 1213: 팰린드롬 만들기
# 알고리즘 분류: 구현/그리디 알고리즘/문자열

# 1. 영어 이름 입력(길이는 최대 50)
# 2. 고유 알파벳과 그 개수를 저장한 딕셔너리 생성
# 3. 알파벳 개수가 길이의 절반보다 많을 경우 "I'm Sorry Hansoo" 출력
# 4-1. 개수가 홀수인 알파벳이 2개 이상일 경우 "I'm Sorry Hansoo" 출력 후 종료
# 4-2. 개수가 홀수인 알파벳을 먼저 덱의 중앙에 1개 배치
# 4-3. 나머지 알파벳은 사전 순서로 뒤에 있는 것부터 덱의 양 옆에 append
# 5. 덱의 문자를 join한 후 출력

import sys
from collections import defaultdict, deque
input = sys.stdin.readline


def odd_counter(d):
    odd_counter = 0
    odd_key = ''
    for key in d:
        if d[key] % 2 == 1:
            odd_counter += 1
            odd_key = key
        if odd_counter >= 2:
            return True, ''  # 개수가 홀수인 알파벳이 2개 이상이면 팰린드롬 생성 불가 판정
    return False, odd_key


def palindrome(name):
    alphabet_dict = defaultdict(int)
    for c in name:
        alphabet_dict[c] += 1

    is_odd, odd_key = odd_counter(alphabet_dict)
    if is_odd:  # 개수가 홀수인 알파벳이 2개 이상이면 팰린드롬 생성 불가 판정
        return "I'm Sorry Hansoo"

    palindrome = deque()
    if odd_key:
        palindrome.append(odd_key)
        alphabet_dict[odd_key] -= 1

    sorted_keys = sorted(alphabet_dict.keys(), reverse=True)
    for key in sorted_keys:
        count = alphabet_dict[key]
        for _ in range(count // 2):
            palindrome.appendleft(key)
            palindrome.append(key)

    return ''.join(palindrome)


name = input().rstrip()
print(palindrome(name))
