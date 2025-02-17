# 25957: 단어 우월 효과 (캠브릿지 대학의 연구결과)
# 출처: 2022 아주대학교 프로그래밍 경시대회 APC C번
# 알고리즘 분류: 자료 구조/문자열/정렬/해시를 사용한 집합과 맵/트리를 사용한 집합과 맵

# 1. 원래 문장에 쓰인 단어의 수 N 입력 (1 ≤ N ≤ 200,000)
# 2. N개의 줄에 걸쳐 길이가 1 이상 8 이하인 단어 입력
# 3. 문장 S에 들어있는 단어의 수 M 입력 (1 ≤ M ≤ 200,000)
# 4. 총 M개의 섞여 있는 단어로 이루어진 문장 S 입력
# 5. 단어 리스트의 중간 문자들을 정렬한 후 첫 글자 + 마지막 글자와 함께 딕셔너리의 키로 사용
# 6. S의 각 단어들을 같은 방식으로 변환한 후, 딕셔너리를 참고해 원래 단어를 찾아 복원
# 7. 원래의 문장 출력

import sys
input = sys.stdin.readline

N = int(input())
word = list(input().rstrip() for _ in range(N))
M = int(input())
S = input().rstrip()


def key_generator(word):
    key = word

    if len(word) > 2:
        key = "-".join([word[0], word[-1], "".join(sorted(word[1:-1]))])
    elif len(word) == 2:
        key = "-".join(list(word))

    return key


def word_matching_dict(word_list):
    matching_dict = {}
    for word in word_list:
        key = key_generator(word)
        matching_dict[key] = word
    return matching_dict


def word_superiority_effect(word_list, S):
    matching_dict = word_matching_dict(word_list)
    word_S_list = S.split()
    answer = []
    for word in word_S_list:
        key = key_generator(word)
        answer.append(matching_dict.get(key, word))
    return " ".join(answer)


print(word_superiority_effect(word, S))
