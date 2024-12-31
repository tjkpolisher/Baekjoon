# 30804: 과일 탕후루
# 특이사항: 다국어(영어)(한국어 번역)
# 출처: solved.ac Grand Arena #3 Division 2 C번/Division 1 A번
# 알고리즘 분류: 구현/브루트포스 알고리즘/두 포인터

# 1. 과일의 개수 N 입력 (1 ≤ N ≤ 200,000)
# 2. 탕후루에 꽂힌 과일을 의미하는 정수 S_i N개 입력 (1 ≤ S_i ≤ 200,000)
# 3. 1부터 9까지의 정수의 개수를 담은 리스트 생성
# 4. 범위를 표현하는 start, end를 입력한 후 투 포인터 알고리즘 적용
# 4-1. 최대 길이를 찾은 경우 최대 길이 반환
# 4-2. 끝 범위의 숫자에 1을 더하고, 그 숫자가 1이면 과일 종류에 1을 더하기
# 4-3. 과일 종류가 2보다 클 경우에는 역연산 진행 후 시작 범위에 1을 더함
# 4-4. 최대 길이를 찾을 때까지 재귀적으로 함수 실행
# 5. 함수 호출 후 결과 출력


import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input())
S = list(map(int, input().split()))
num = [0] * 10


def number(start, end, N, max_num, fruit):
    if end >= N:
        return max_num

    num[S[end]] += 1
    if num[S[end]] == 1:
        fruit += 1

    if fruit > 2:
        num[S[start]] -= 1
        if num[S[start]] == 0:
            fruit -= 1
        start += 1

    max_num = max(max_num, end - start + 1)
    return number(start, end + 1, N, max_num, fruit)


print(number(0, 0, N, 0, 0))
