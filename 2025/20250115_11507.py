# 11507: 카드셋트
# 특이사항: 다국어(영어)(한국어 번역)
# 출처: COCI 2015/2016 Contest #1 1번
# 알고리즘 분류: 자료 구조/문자열/해시를 사용한 집합과 맵/파싱

# 1. 문자열 S 입력 (1 ≤ |S| ≤ 1000)
# [보충설명] P, K, H, T는 각각 스페이드/하트/다이아몬드/클로버의 네 문양을 상징
# [보충설명] 또한 문자열의 숫자는 카드의 번호를 의미하며 01~13까지 두자리의 숫자로 구성.
# 2. 문자열을 3개씩 끊어서 순회하면서 각 문양별로 문자열을 딕셔너리에 수집
# 3-1. 딕셔너리에 이미 존재하는 카드가 식별되면 GRESKA를 출력하고 종료
# 3-2. 순회가 완전히 끝나면 카테고리의 각 숫자 중 빠진 카드의 숫자를 출력

S = input()
card_table = {"P": set(), "K": set(), "H": set(), "T": set()}
for i in range(len(S) // 3):
    card = S[i * 3:i * 3 + 3]
    category = card[0]
    if card in card_table[category]:
        print("GRESKA")
        exit()
    card_table[category].add(card)
for category in card_table.keys():
    print(13 - len(card_table[category]), end=' ')
