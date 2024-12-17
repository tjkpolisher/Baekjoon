# 32345: 혼긱대학교
# 출처: 2024 HICON 홍익대학교 프로그래밍 경진대회 D번
# 알고리즘 분류: 수학/문자열/조합론

# 1. 테스트 케이스의 개수 T 입력 (1 ≤ T ≤ 100,000)
# 2. T개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어 S 입력 (1 ≤ |S| ≤ 300,000)
# 3. 단어를 순회하면서 모음이 나타나면 그룹으로 분할
# 4-1. 모음이 없을 경우 -1을 출력
# 4-2. 모음의 위치 인덱스를 서로 빼면서 정답에 더한 뒤 10^9 + 7을 나눠서 출력

import sys
input = sys.stdin.readline

T = int(input())
vowels = {'a', 'e', 'i', 'o', 'u'}  # 'y'는 이 문제에서 모음으로 취급하지 않음
MOD = 10 ** 9 + 7

for _ in range(T):
    word = list(input().rstrip())
    ans = 1
    vowel_position = []

    for i, ch in enumerate(word):
        if ch in vowels:
            vowel_position.append(i)

    if not vowel_position:
        print(-1)
        continue

    for i in range(len(vowel_position) - 1):
        ans *= vowel_position[i + 1] - vowel_position[i]
    print(ans % MOD)
