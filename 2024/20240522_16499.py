# 16499: 동일한 단어 그룹화하기
# 출처: 한양대학교 ERICA 캠퍼스/2018 ERICA Software- Up Programming Contest League B A번
# 알고리즘 분류: 자료 구조/문자열/정렬/해시를 사용한 집합과 맵

# 1. 단어의 개수 N 입력 (2 ≤ N ≤ 100)
# 2. N개의 줄에 걸쳐 단어 입력 (알파벳 소문자로만 구성, 길이는 10 이하)
# 3. 단어를 각 문자로 쪼개, 문자를 키/문자의 개수를 값으로 하는 딕셔너리로 구성
# 4-1. 동일한 딕셔너리로 판정될 경우, 리스트에 추가하지 않고 패스
# 4-2. 그렇지 않으면 별개의 딕셔너리로 구분하고 리스트에 추가
# 5. 리스트의 원소의 개수를 출력

from collections import defaultdict

N = int(input())
words = []
for _ in range(N):
    word = input()
    word_dict = defaultdict(int)
    for c in word:
        word_dict[c] += 1
    if word_dict not in words:
        words.append(word_dict)

print(len(words))
