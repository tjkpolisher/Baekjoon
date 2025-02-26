# 10453: 문자열 변환
# 특이사항: 다국어(영어)(한국어 번역)
# 출처: ICPC Asia Regional - Daejeon 2014 H번
# 알고리즘 분류: 문자열/애드 혹

# 1. 테스트 케이스의 수 T 입력
# 2. 문자열 A, B를 공백으로 분리하여 입력(A와 B는 좋은 문자열, 길이는 2 이상 100,000 이하)
# [보충설명] 좋은 문자열은 다음과 같이 정의됨.
# [보충설명] ab는 좋은 문자열
# [보충설명] 문자열 [S]가 좋은 문자열이라면, 오른쪽과 왼쪽 끝에 a와 b를 추가한 a[S]b도 좋은 문자열
# [보충설명] 문자열 [S]와 [T]가 좋은 문자열이라면 이를 붙여 쓴 [S][T]도 좋은 문자열.
# 3. A와 B에서 모든 'a'가 등장하는 위치를 리스트에 저장
# 4. 3에서 얻은 두 리스트의 같은 순서의 인덱스 차이의 절대값을 모두 합하기
# 5. 4의 계산 결과 출력

import sys
from collections import Counter
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    A, B = input().rstrip().split()

    # a와 b의 개수가 서로 다르면 -1을 출력 후 다음 케이스로 진행
    counter_A = Counter(A)
    counter_B = Counter(B)
    if counter_A['a'] != counter_B['a'] and counter_A['b'] != counter_B['b']:
        print(-1)
        continue

    pos_A = [i for i, ch in enumerate(A) if ch == 'a']
    pos_B = [i for i, ch in enumerate(B) if ch == 'a']

    ans = 0
    for a_idx, b_idx in zip(pos_A, pos_B):
        ans += abs(a_idx - b_idx)
    print(ans)
