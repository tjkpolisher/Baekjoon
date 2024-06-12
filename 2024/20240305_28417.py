# 28417: 스케이트보드
# 알고리즘 분류: 정렬

# 1. 사람의 수 N 입력
# 2. [반복문] 2개의 런, 5개의 트릭 점수를 나타내는 정수 입력
# 3. 2개의 런 최고 점수와, 5개의 트릭 점수 중 상위 2개 점수를 더함
# 4. 세 점수의 합이 현재까지의 최고 점수보다 높을 경우 최고 점수 변수를 갱신
# 5. 최종 점수 출력

import sys
input = sys.stdin.readline

N = int(input())
max_score = 0

for _ in range(N):
    scores = list(map(int, input().split()))
    run = max(scores[:2])
    trick = sorted(scores[2:], reverse=True)[:2]
    total_score = run + sum(trick)
    if total_score > max_score:
        max_score = total_score

    if total_score == 300:
        break

print(max_score)
