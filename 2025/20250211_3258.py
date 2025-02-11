# 3258: 컴포트
# 특이사항: 다국어(영어)(한국어 번역)
# 출처: Croatian Highschool Competitions in Informatics 2002 National Competition # 1 - Juniors 1번
# 알고리즘 분류: 구현/브루트포스 알고리즘/시뮬레이션

# 1. 필드 개수 N, 도착하고자 하는 필드 번호 Z, 정수의 개수 M 입력
# [보충설명] 2 ≤ N ≤ 1000, 2 ≤ Z, 0 ≤ M ≤ N - 2
# 2. M개의 줄에 걸쳐 장애물이 있는 필드의 번호를 뜻하는 서로 다른 정수 입력
# [보충설명] 1번과 Z번 필드에는 장애물이 놓이지 않음
# 3. K를 1로 초기화
# 4. 1부터 N까지의 수를 시계 방향으로 원형으로 배치했다고 가정하고 K씩 증가하면서 수를 체크
# 4-1. 수를 체크한 후 방문한 적이 없으면 집합에 저장
# 4-2. 해당 필드에 장애물이 있으면 K를 증가시키고 4를 반복
# 4-3. 제대로 Z에 도달했을 경우 K 출력 후 종료

import sys
input = sys.stdin.readline

N, Z, M = map(int, input().split())

obstacles = set(map(int, input().split()))

for K in range(1, N):
    visited = set()
    pos = 1  # 시작 위치

    while pos not in visited:
        visited.add(pos)
        if pos in obstacles:
            break
        pos = (pos + K - 1) % N + 1
        if pos == Z:
            print(K)
            exit()
