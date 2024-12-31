# 9631: The Alphabet Sticker
# 특이사항: 다국어(영어)
# 출처: 2013 Arab Collegiate Programming Contest A번
# 알고리즘 분류: 수학/문자열/조합론

# 1. 테스트 케이스의 개수 T 입력 (1 ≤ T ≤ 100)
# 2. 길이가 10,000 이하인 문자열 입력 후 sticker 변수에 저장(알파벳 소문자 또는 ? 문자 중 하나로 구성)
# 3. 물음표 구간의 양 옆 문자를 확인하고, 두 문자가 서로 다를 경우 구간의 길이를 결과에 곱합
# 4. 연산 후 100000007로 나눈 나머지를 취함
# 5. 결과값 출력

import sys
input = sys.stdin.readline

MOD = 10 ** 9 + 7

T = int(input())
for _ in range(T):
    sticker = input().rstrip()
    result = 1
    n = len(sticker)
    i = 0

    while i < n:
        if sticker[i] == '?':
            j = i
            while j < n and sticker[j] == '?':
                j += 1

            # j는 이제 물음표가 아닌 위치 또는 문자열 끝을 가리킴
            left = sticker[i - 1] if i > 0 else None
            right = sticker[j] if j < n else None

            if left and right:
                if left != right:
                    result *= (j - i + 1)
                    result %= MOD

            i = j
        else:
            i += 1

    print(result % MOD)
