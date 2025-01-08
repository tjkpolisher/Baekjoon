# 20915: 숫자 카드 놀이
# 특이사항: 다국어(영어)(한국어 번역)
# 알고리즘 분류: 그리디 알고리즘/브루트포스 알고리즘

# 1. 테스트 케이스의 수 T 입력 (1 ≤ T ≤ 10)
# 2. Albert가 가진 숫자 카드를 표현하는 문자열 입력(각 문자는 '0'~'9' 중 하나)
# [보충설명] 문자열의 길이 n은 2 ≤ n ≤ 18
# 3. 문자열 중 6을 9로 변경
# 4. 문자열을 내림차순으로 정렬
# 5. 0의 개수를 확인하고 문자열을 리스트로 변환한 뒤 0을 전부 pop
# 6. 리스트에 남은 수를 num1, 0을 num2에 더한 뒤 수를 연산
# 6-1. num1 > num2 이면 num2 = num2 * 10 + 다음 카드의 수
# 6-2. 그 외에는 num1 = num1 * 10 + 다음 카드의 수
# 7. 두 변수를 정수형으로 변환한 뒤 곱에 0의 개수만큼 10을 곱하고 출력

T = int(input())
for _ in range(T):
    cards = input().replace('6', '9')
    cards = sorted(list(cards), reverse=True)

    zeros = cards.count('0')
    for i in range(zeros):
        cards.pop()
    if not cards:
        print(0)
        continue

    num1 = int(cards[0])
    num2 = 0
    for i in range(1, len(cards)):
        if num1 > num2:
            num2 = num2 * 10 + int(cards[i])
        else:
            num1 = num1 * 10 + int(cards[i])
    for i in range(zeros):
        num1 *= 10
    print(num1 * num2)
