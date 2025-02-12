# 2961: 도영이가 만든 맛있는 음식
# 특이사항: 다국어(영어)(한국어 번역)
# 출처: COCI 2008/2009 Contest #2 3번
# 알고리즘 분류: 브루트포스 알고리즘/비트마스킹/백트래킹

# 1. 재료의 개수 N 입력 (1 ≤ N ≤ 10)
# 2. N개의 줄에 걸쳐 신맛과 쓴맛의 정도 S, B 입력 (두 맛은 모두 1,000,000,000보다 작은 양의 정수)
# 3. 재귀 함수 호출
# 3-1. N-1번 인덱스의 재료까지 사용했을 경우 신맛의 총합과 쓴맛의 총 곱의 차이를 반환
# 3-2. 재료를 아직 덜 사용했을 경우, 다음 재료 호출 후 합/곱 연산 진행
# 3-3. 해당 인덱스에서 모두 호출이 끝났으면 합/곱 연산 없이 다음 인덱스로 넘어가 재귀 호출
# 4. 정답 출력

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input())
sour = []
bitter = []

for _ in range(N):
    s, b = map(int, input().split())
    sour.append(s)
    bitter.append(b)


def recur(idx, s, b, use):
    global answer

    if idx == N:
        if not use:  # 아무 재료도 사용하지 않았다면 문제의 조건에 위배되므로 함수 종료
            return
        result = abs(s - b)
        answer = min(answer, result)
        return

    recur(idx + 1, s * sour[idx], b + bitter[idx], use + 1)
    recur(idx + 1, s, b, use)


answer = 10 ** 9
recur(0, 1, 0, 0)
print(answer)
