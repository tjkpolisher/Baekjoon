# 3054: 피터팬 프레임
# 특이사항: 다국어(영어)(한국어 번역)
# 출처: COCI 2006/2007 Contest #1 3번
# 알고리즘 분류: 구현

# 1. 알파벳 대문자로 이루어진 최대 15글자의 단어 입력
# 2. 3의 배수 위치는 웬디 프레임, 나머지 위치는 피터팬 프레임으로 장식
# 2-1. 한 행마다 출력 열의 개수 c_i = 5 + 4 * (i - 1)
# 2-2. 5행 c_i열의 2차원 리스트의 모든 원소를 '.'으로 초기화
# 2-3. 3행의 2 + 4 * i번째 원소를 단어의 i번째 글자로 치환
# 2-4. 1행과 5행의 2 + 4 * i번째 원소를 '#'으로 치환(단, idx + 1이 3의 배수이면 '*'으로 치환)
# 2-5. 2행과 4행의 홀수 인덱스의 원소를 '#'으로 치환
# 2-6. 3행의 글자 주변 1, 2, 3행 중 문자가 들어가야 하는 부분을 '#' 또는 '*'로 치환
# 3. 리스트의 각 행을 join하여 출력

word = input()
i = len(word)

frame = [['.' for _ in range(5 + 4 * (i - 1))] for j in range(5)]
for idx in range(i):
    frame[0][2 + 4 * idx] = '#' if (idx + 1) % 3 != 0 else '*'
    frame[2][2 + 4 * idx] = word[idx]
    frame[4][2 + 4 * idx] = '#' if (idx + 1) % 3 != 0 else '*'

for idx in range(1, len(frame[0]), 2):
    frame[1][idx] = '#'
    frame[3][idx] = '#'

idx = 0
for j in range(2, len(frame[0]) - 2):
    if frame[2][j] == word[idx]:
        if (idx + 1) % 3 == 0:
            frame[1][j - 1] = '*'
            frame[1][j + 1] = '*'
            frame[2][j - 2] = '*'
            frame[2][j + 2] = '*'
            frame[3][j - 1] = '*'
            frame[3][j + 1] = '*'
        else:
            if frame[2][j - 2] == '.':
                frame[2][j - 2] = '#'
            frame[2][j + 2] = '#'
        idx += 1

for i in range(5):
    print(''.join(frame[i]))
