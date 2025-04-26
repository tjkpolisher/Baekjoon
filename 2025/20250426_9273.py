# 9273: 정제헌을 팔자!
# 특이사항: 다국어(영어)(한국어 번역)
# 출처: CTU Open Contest 2013 L번
# 알고리즘 분류: 수학/브루트포스 알고리즘/정수론

# 1. 각 줄마다 테스트 케이스 입력 ("1/n" 형태로 입력, 1 ≤ n ≤ 10,000)
# 2. 1/x + 1/y = 1/n을 만족하는 조합을 찾기 위해 반복문 실행
# 2-1. n^2의 약수의 개수 D에 대해 그 약수를 찾으면 2 * e + 1을 곱하기
# 3. 이중 반복문이 모두 종료되면 카운터 출력

import sys
input = sys.stdin.readline

while True:
    try:
        capacity = input().rstrip()
        n = int(capacity[2:])  # 분수 1/n의 분모
    except ValueError:
        break

    cnt = 1
    tmp = n

    # 2의 지수 처리
    e = 0
    while tmp % 2 == 0:
        tmp //= 2
        e += 1
    if e:
        cnt *= (2 * e + 1)

    # 홀수인 소인수 처리
    p = 3
    while p ** 2 <= tmp:
        if tmp % p == 0:
            e = 0
            while tmp % p == 0:
                tmp //= p
                e += 1
            cnt *= (2 * e + 1)
        p += 2

    # 남은 소인수가 있을 경우 추가 처리
    if tmp > 1:
        cnt *= 3  # 2 * 1 + 1

    print((cnt + 1) // 2)
