# 1620: 나는야 포켓몬 마스터 이다솜
# 알고리즘 분류: 자료 구조/해시를 사용한 집합과 맵

# 1. 도감의 수록된 포켓몬의 수 N, 맞춰야 하는 문제의 개수 M 입력
# 1-1. 포켓몬의 번호와 이름을 수록한 해시 테이블 생성
# [보충설명] 1 ≤ N, M ≤ 100,000
# 2. N개의 줄에 걸쳐 1번부터 N번에 해당하는 포켓몬의 이름 입력(첫 글자만 영어 대문자, 나머지는 영어 소문자)
# [보충설명] 일부 포켓몬은 마지막 문자만 대문자일 수 있음. 길이는 2 이상 20 이하.
# 3. M개의 줄에 걸쳐 맞춰야 하는 문제 입력
# 4. 문제가 알파벳이면 포켓몬 번호를, 숫자면 포켓몬 번호 출력
# 5. M개의 줄에 각 문제에 대한 답 출력

import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
p_n = dict()
n_p = dict()

for i in range(N):
    p = input().rstrip()
    n = i + 1
    p_n[p] = n
    n_p[n] = p

for _ in range(M):
    prob = input().rstrip()
    # 문제가 숫자일 경우
    try:
        prob = int(prob)
        print(n_p[prob])
    except ValueError:
        print(p_n[prob])
