# 9342: 염색체
# 특이사항: 다국어(영어)(한국어 번역)
# 출처: 2013 ACM-ICPC Thailand National Programming Contest D번
# 알고리즘 분류: 문자열/정규 표현식

# 1. 테스트 케이스의 개수 T 입력 (T ≤ 20)
# 2. 테스트 케이스에 해당하는 문자열 입력
# 3. 문자열이 염색체인지 아닌지를 정규 표현식을 이용해 판별
# 3-1. A~F 중 0개 또는 1개로 시작
# 3-2. 그 다음에 A가 하나 이상
# 3-3. 그 다음에 F가 하나 이상
# 3-4. 그 다음에 C가 하나 이상
# 3-5. 그 다음에 A~F 중 0개 또는 1개로 문자열 끝
# 4. 조건을 모두 만족하면 "Infected!"를, 아니면 "Good"을 출력

import re

T = int(input())
for _ in range(T):
    s = input()
    if re.match(r'^[A-F]?A+F+C+[A-F]?$', s):
        print("Infected!")
    else:
        print("Good")
