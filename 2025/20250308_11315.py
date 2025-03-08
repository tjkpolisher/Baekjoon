# 11315: Serves Me Right
# 특이사항: 다국어(영어)
# 출처: CCPC 2015 Division 1 D번/CCPC 2015 Division 2 G번
# 알고리즘 분류: 구현/시뮬레이션

# 1. 처리할 웹 로그의 개수 T 입력 (1 ≤ T ≤ 100)
# 2. 로그의 첫 번째 줄에 E와 TO 입력 (1 ≤ E,TO ≤ 1440)
# [보충설명] E는 로그의 개수, TO는 로그인한 사용자의 세션 만료 시간(자동 로그아웃까지의 시간)
# 3. E개의 줄에 걸쳐 로그 항목 입력
# 4. 사용자 로그인 시간을 저장할 딕셔너리 user_table 생성
# 4. 로그 내용에 따라 다음 작업 실행
# 4-1. RESTART로 로그가 끝날 경우 서버 재시작으로 user_table 초기화
# 4-2-1. 그렇지 않을 경우 로그를 TIME, USER, hUSER_NAMEi, hUSER_ACTIONi로 split
# 4-2-2. hUSER_ACTIONi가 LOG_IN일 경우 user_table에 USER:TIME 저장
# 4-2-3. LOG_OUT일 경우 user_table에서 USER 삭제
# 4-3. 위의 과정을 실행하기 전 TIME이 기존 로그인 시간 + TO를 초과하면 해당 키 삭제
# 4-4. 로그에서 지시한 과정이 끝나면 최대 로그인 사용자 갱신
# 5. 최대 로그인 사용자의 수 출력

import sys
input = sys.stdin.readline

T = int(input())


def session_logout(t1, t2, TO):
    h1, m1 = map(int, t1.split(":"))
    h2, m2 = map(int, t2.split(":"))

    return True if h1 * 60 + m1 + TO <= h2 * 60 + m2 else False


for _ in range(T):
    E, TO = map(int, input().split())
    user_table = {}
    max_users = 0
    unique_users = set()

    for i in range(E):
        log = input().rstrip()
        if log.endswith("RESTART"):
            user_table = {}
        else:
            TIME, _, USER, hUSER_ACTIONi = log.split()
            unique_users.add(USER)
            if user_table:
                names = list(user_table.keys())
                for name in names:
                    if session_logout(user_table[name], TIME, TO):
                        user_table.pop(name, None)

            if hUSER_ACTIONi == "LOG_IN":
                user_table[USER] = TIME
            elif hUSER_ACTIONi == "LOG_OUT":
                user_table.pop(USER, None)
            max_users = max(max_users, len(user_table))

    print(len(unique_users), max_users)
