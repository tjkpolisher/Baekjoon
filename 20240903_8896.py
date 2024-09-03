# 8896: 가위 바위 보
# 출처: ICPC Asia Regional - Daejeon 2012 I번
# 특이사항: 다국어(영어)(한국어 번역)
# 알고리즘 분류: 구현/시뮬레이션

# 1. 테스트 케이스의 개수 T 입력
# 2. 테스트 케이스의 첫째 줄에 참여하는 로봇의 수 N 입력 (2 ≤ N ≤ 10)
# 3. N개의 줄에 걸쳐 각 로봇에 저장되어 있는 문자열 입력
# [보충설명] 모든 로봇의 문자열의 길이는 k (3 ≤ k ≤ 30), S/R/P가 각각 가위/바위/보를 나타냄.
# 4. 문자열의 길이 k만큼 각 문자열의 맨 앞에서부터 문자를 pop
# 4-1. 한 라운드에 세 종류의 문자가 다 나온다면 비긴 것이므로 다음 라운드로 진행
# 4-2. 한 라운드에 같은 문자만 나온 경우에도 비긴 것이므로 다음 라운드 진행
# 4-3. 두 종류의 문자만 나왔다면 가위바위보 규칙에 따라 진 문자열은 제거
# 5. 마지막 라운드에 승리한 로봇의 번호를 출력하되, 한 명의 승자가 나오지 않으면 0을 출력

from collections import defaultdict, deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())  # 참여하는 로봇의 수
    robots = defaultdict(deque)
    for i in range(N):
        rsp = deque(input().rstrip())
        robots[i] = rsp

    k = len(rsp)  # 문자열의 길이
    for i in range(k):
        # 로봇이 한 개만 남았으면 더 이상 게임을 하지 않아도 되므로 정지
        if len(robots) <= 1:
            break

        popped = defaultdict(str)
        # 생존한 로봇의 수만큼 가위바위보 문자열을 추출
        for j in robots.keys():
            popped[j] = robots[j].popleft()

        # 전부 똑같은 걸 내거나 다 다른 걸 냈으면 비김
        if len(set(popped.values())) == 3 or len(set(popped.values())) == 1:
            continue

        # 패배한 로봇들의 번호를 저장
        losers = set()
        if 'R' in popped.values() and 'S' in popped.values():
            for key, value in popped.items():
                if value == 'S':
                    losers.add(key)
        elif 'S' in popped.values() and 'P' in popped.values():
            for key, value in popped.items():
                if value == 'P':
                    losers.add(key)
        elif 'P' in popped.values() and 'R' in popped.values():
            for key, value in popped.items():
                if value == 'R':
                    losers.add(key)

        # 패배한 로봇 삭제
        for loser in losers:
            del robots[loser]

    if len(robots) > 1:
        print(0)
    else:
        print(list(robots.keys())[0] + 1)
