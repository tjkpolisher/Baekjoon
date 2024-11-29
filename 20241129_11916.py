# 11916: 볼질
# 출처: GENIUSainta.com - oj.uz Contest OJUZ10 1번
# 알고리즘 분류: 구현/시뮬레이션

# 1. 창석이가 던진 공의 수 N 입력 (1 ≤ N ≤ 50,000)
# 2. 창석이가 던진 공의 종류 입력 (볼, 몸에 맞는 공, 폭투는 각각 1, 2, 3으로 주어짐)
# 3. 루상의 주자 여부를 확인하는 딕셔너리 생성 후, 다음 규칙에 따라 진루를 하되, 3루에 있는 주자가 진루할 경우 실점에 1을 추가
# 3-1. 볼이 4번 나오거나 몸에 맞는 공이 나올 경우
# 3-1-1. 1루에 주자가 없으면 타자 주자만 1루로 이동
# 3-1-2. 1루 또는 그 이후에 연속으로 베이스에 주자가 있을 경우 한 베이스씩 밀어내기
# 3-2. 폭투가 나올 경우 루상의 모든 주자 한 베이스씩 진출
# 3-2-1. 폭투도 볼에 해당하므로 볼 카운트를 1 올리되, 3볼에서 폭투가 나오면 타자도 그대로 출루
# 4. 총 실점 출력

N = int(input())
balls = list(map(int, input().split()))

bases = {1: False, 2: False, 3: False}  # 시작할 때는 모든 베이스가 비어있음
score = 0  # 총 실점
ball_count = 0  # 볼의 개수, 4개가 되면 볼넷으로 타자가 출루 및 주자가 조건을 충족하면 한 베이스 진루


def forward():
    global bases, score
    if bases[3]:
        if bases[1] and bases[2]:
            bases[3] = False
            score += 1
    if bases[2]:
        if bases[1]:
            bases[2] = False
            bases[3] = True
    if bases[1]:
        bases[1] = False
        bases[2] = True
    bases[1] = True


def wild_pitch():
    global bases, score
    if bases[3]:
        bases[3] = False
        score += 1
    if bases[2]:
        bases[2] = False
        bases[3] = True
    if bases[1]:
        bases[1] = False
        bases[2] = True


for ball in balls:
    if ball == 1:
        # 볼 - 타자는 4볼일 경우 출루
        ball_count += 1
        if ball_count == 4:
            forward()
            ball_count = 0
    elif ball == 2:
        # 몸에 맞는 공 (데드볼, hit-by-pitch) - 타자 출루 및 볼 카운트 즉시 초기화
        forward()
        ball_count = 0
    elif ball == 3:
        # 폭투 - 주자 한 베이스씩 진루, 타자는 4볼이 될 때만 출루 가능
        wild_pitch()
        ball_count += 1
        if ball_count == 4:
            forward()
            ball_count = 0

print(score)
