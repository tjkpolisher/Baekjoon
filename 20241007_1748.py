# 1748: 수 이어 쓰기 1
# 특이사항: 다국어(영어)(한국어 번역), 시간 제한(Python 3, Pypy3: 0.5초)
# 출처: 2004 Croatian Highschool Competitions in Informatics Regional Competition - Juniors 4번
# 알고리즘 분류: 수학/구현

# 1. 정수 N 입력 (1 ≤ N ≤ 100,000,000)
# 2. N의 자릿수를 변수로 저장
# 3. 점화식 계산: ans = func(length - 1) + length * (N - int('9' * (length - 1)))
# [보충설명] func은 length를 변수로 삼는 함수로, 해당 자릿수에서 가장 큰 수에 대한 점화식의 값을 의미
# 예를 들어, length = 2일 때는 N = 99, length = 3일 때는 N = 999일 때의 수의 자릿수

N = input()
length = len(N)
N = int(N)


def first_term(length):
    ans = [0, 0, 9]
    for i in range(2, length + 1):
        term = ans[-1] + i * (10 ** i - 1 - (10 ** (i - 1) - 1))
        ans.append(term)
    return ans[-1]


if length > 1:
    ans = first_term(length - 1) + length * (N - (10 ** (length - 1) - 1))
else:
    ans = N
print(ans)
