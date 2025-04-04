# 5093: Letter Replacement
# 특이사항: 다국어(영어)
# 출처: NZPC 2011 H번
# 알고리즘 분류: 구현/문자열

# 1. 처리해야 할 단어를 입력
# 1-1. '#'이 입력되면 프로그램 종료
# 2. 이미 등장한 단어를 저장할 집합, 소문자-특수기호 딕셔너리, 중복 횟수를 저장할 변수 생성
# 3. 입력받은 단어의 모든 글자를 순회하면서 아래의 과정 실행
# 3-1. 글자를 소문자로 변환
# 3-2. 이전에 한 번도 등장하지 않았다면 등장한 글자 집합에 추가하고 결과 리스트에 원래 문자 append
# 3-3-1. 이미 등장한 문자라면 처음 중복 확인될 때 특수기호 매핑 후 결과에 첨부
# 3-3-2. symbol_index에 1을 더함
# 4. 리스트를 문자열로 join해서 출력

import sys
input = sys.stdin.readline


def transform_word(word):
    symbols = ['*', '?', '/', '+', '!']
    seen = set()  # 이미 등장한 문자(소문자 변환 기준)
    repeated_symbols = {}  # 중복이 처음 확인된 소문자 -> 할당된 기호
    symbol_index = 0  # 몇 번째로 중복이 발생한 문자인가(0~4)

    result = []

    for char in word:
        lower_char = char.lower()

        if lower_char not in seen:
            # 아직 등장하지 않은 문자
            seen.add(lower_char)
            result.append(char)
        else:
            # 이미 등장한(중복) 문자
            if lower_char not in repeated_symbols:
                # 이 중복 문자가 처음 등장한 경우
                # 아직 할당되지 않았다면 symbols[symbol_index]를 할당
                repeated_symbols[lower_char] = symbols[symbol_index]
                symbol_index += 1
            # 이미 할당된 기호로 대체
            result.append(repeated_symbols[lower_char])

    return ''.join(result)


while True:
    word = input().rstrip()
    if word == '#':
        break

    print(transform_word(word))
