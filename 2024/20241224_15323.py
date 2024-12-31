# 15323: ZigZag
# 특이사항: 다국어(영어)
# 출처: COCI 2017/2018 Contest #2 2번
# 알고리즘 분류: 자료 구조/문자열/정렬/해시를 사용한 집합과 맵

# 1. 단어의 개수 K, 문자의 개수 N 입력
# [보충설명] 1 ≤ K ≤ 100,000, 1 ≤ N ≤ 100,000
# 2. K줄에 걸쳐 영어 소문자로 구성된 21자 이내의 단어 입력 후 저장
# 3. N개의 줄에 걸쳐 영어 소문자 입력
# 4. 각 영어 소문자로 시작하는 단어를 정리해 딕셔너리에 사전 순서대로 정렬하여 저장
# 5. 영어 소문자를 순서대로 순회하면서 딕셔너리의 단어 순회
# 6. 소문자에 해당하는 단어를 출력하면서 종료할 때까지 반복

import sys
from collections import deque
input = sys.stdin.readline

K, N = map(int, input().rstrip().split())
words = [input().rstrip() for _ in range(K)]
letters = [input().rstrip() for _ in range(N)]

word_dict = {}
distinct_letter = list(set(letters))
for word in words:
    first_letter = word[0]
    if first_letter not in word_dict:
        word_dict[first_letter] = []
    word_dict[first_letter].append(word)

for letter in distinct_letter:
    word_dict[letter] = deque(sorted(word_dict[letter]))

for letter in letters:
    word_to_print = word_dict[letter].popleft()
    print(word_to_print)
    word_dict[letter].append(word_to_print)
