# 10546: 배부른 마라토너
# 특이사항: 다국어(영어)(한국어 번역)
# 출처: COCI 2014/2015 Contest #2 2번
# 알고리즘 분류: 자료 구조/해시를 사용한 집합과 맵

# 1. 참가자의 수 N 입력 (1 ≤ N ≤ 10^5)
# 2. N개의 줄에 걸쳐 참가자의 이름을 딕셔너리에 추가 및 수에 1을 더함
# 3. N - 1개의 줄에 걸쳐 완주한 참가자의 이름 입력받고 해당 이름을 집합에서 제거
# 4. 마지막으로 남은 참가자의 이름 출력

from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
runners = defaultdict(int)
for _ in range(N):
    runners[input().rstrip()] += 1

for _ in range(N - 1):
    name = input().rstrip()
    runners[name] -= 1
    if not runners[name]:
        del runners[name]

ans = list(runners.keys())
print(*ans)
