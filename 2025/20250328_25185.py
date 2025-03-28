# 25185: 카드 뽑기
# 출처: 2022 서강대학교 청정수컵 청정수 Round C번
# 알고리즘 분류: 구현

# 1. 정수 T 입력 (1 ≤ T ≤ 100)
# 2. T개의 줄에 걸쳐 i일 후에 해당하는 뽑은 카드 4장을 공백으로 구분해 입력(1 ≤ i ≤ T)
# 3. 각 줄에 대해 다음 규칙을 적용하고, 하나라도 조건을 만족하면 쉬는 날로 판정
# 3-1. 적힌 알파벳이 같으면서 숫자가 연속되는 세 장이 존재(연속한 세 숫자는 서로 다른 숫자)
# 3-2. 적힌 알파벳과 숫자가 모두 같은 세 장이 존재.
# 3-3. 두 장씩 짝지었을 때, 짝을 지은 카드끼리 적힌 숫자와 알파벳이 같을 때.
# 4. 판정에 따라 쉬는 날이면 ":)", 아니라면 ":("를 출력

import sys
from collections import Counter
input = sys.stdin.readline


def is_true(numbers):
    if numbers[0] + 1 == numbers[1] and numbers[1] + 1 == numbers[2]:
        return True
    return False


def rule1(cards):
    # 알파벳이 같으면서 숫자가 연속되는 세 장이 존재.
    alphabets = [cards[i][1] for i in range(4)]
    cnt = Counter(alphabets)
    if 2 in cnt.values():
        return False

    for i in range(4):
        if cnt[alphabets[i]] >= 3:
            pivot_alphabet = alphabets[i]
            break
    numbers = [int(cards[i][0]) for i in range(4) if cards[i][1] == pivot_alphabet]
    numbers = list(set(numbers))
    if len(numbers) < 3:
        return False
    numbers.sort()
    if len(numbers) == 3:
        if is_true(numbers):
            return True
    else:
        if is_true(numbers[:3]) or is_true(numbers[1:]):
            return True

    return False


def rule2(cards):
    # 적힌 알파벳과 숫자가 모두 같은 세 장이 존재.
    if cards[0] == cards[1] == cards[2] or cards[0] == cards[1] == cards[3] \
      or cards[0] == cards[2] == cards[3] or cards[1] == cards[2] == cards[3]:
        return True
    return False


def rule3(cards):
    # 두 장씩 짝지었을 때, 짝을 지은 카드끼리 적힌 숫자와 알파벳이 똑같을 때
    cnt = Counter(cards)
    if list(cnt.values()) == [2, 2]:
        return True
    return False


T = int(input())
for _ in range(T):
    cards = list(input().rstrip().split())
    flag1 = rule1(cards)
    flag2 = rule2(cards)
    flag3 = rule3(cards)

    if flag1 or flag2 or flag3:
        print(":)")
    else:
        print(":(")
