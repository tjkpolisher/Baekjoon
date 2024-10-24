# 5426: 비밀 편지
# 특이사항: 다국어(영어)(한국어 번역)
# 출처: ICPC Benelux Algorithm Programming Contest (BAPC) 2012 E번
# 알고리즘 분류: 수학/구현/문자열

# 1. 테스트 케이스의 개수 입력 (100개 이하)
# 2. 암호화된 편지를 나타내는 문자열 입력(알파벳 소문자와 대문자로 구성, 길이는 1 이상 10000 이하의 제곱수)
# 3. 문자열의 길이의 제곱근의 길이를 갖는 정사각형 2차원 배열에 문자열 저장
# 4. 위에서 아래로, 오른쪽 열에서 왼쪽 열로 읽어가며 원래 문장을 복구
# 5. 복구된 원래 문자열을 출력

t = int(input())
for _ in range(t):
    letter = input()
    length = int(len(letter) ** 0.5)
    letter_array = []

    for i in range(length):
        letter_array.append(list(letter[length * i:length * (i + 1)]))

    ans = []
    for i in range(length):
        for j in range(length):
            ans.append(letter_array[j][length - i - 1])

    print(''.join(ans))
