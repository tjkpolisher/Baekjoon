# 31846: 문자열 접기
# 출처: 2024 인하대학교 프로그래밍 경진대회(IUPC) Contest C번
# 알고리즘 분류: 구현/브루트포스 알고리즘즘

# 1. 문자열의 길이 N 입력 (2 ≤ N ≤ 50)
# 2. 알파벳 대문자로 구성된 문자열 S 입력
# 3. 정수 Q 입력 (1 ≤ Q ≤ 100)
# 4. Q개의 줄에 걸쳐 질문을 나타내는 정수 l, r 입력 (1 ≤ l < r ≤ N)
# 5. l과 r에서 1씩 빼기
# 6. 왼쪽 절반 길이와 오른쪽 절반 길이 중 작은 값을 겹치는 쪽으로 설정
# 7. 겹친 길이만큼 위아래 문자열을 비교해 서로 같은 문자면 스코어에 1 추가
# 8. 최대 점수 갱신
# 9. 최대 점수 출력

import sys
input = sys.stdin.readline

N = int(input())
S = input().rstrip()
Q = int(input())

for _ in range(Q):
    l, r = map(int, input().split())

    l -= 1
    r -= 1
    max_score = 0

    # 접는 위치 i는 l과 r 사이, i와 i+1 사이에서 접음
    for i in range(l, r):
        # 왼쪽 절반 길이 = i-l+1, 오른쪽 절반 길이 = r-i
        overlap = min(i - l + 1, r - i)
        score = 0
        # k번째째 매칭: S[i-k] vs S[i+1+k]
        for k in range(overlap):
            if S[i - k] == S[i + 1 + k]:
                score += 1
        if score > max_score:
            max_score = score

    print(max_score)
