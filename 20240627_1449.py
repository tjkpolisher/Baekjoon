# 1449: 수리공 항승
# 알고리즘 분류: 그리디 알고리즘/정렬

# 1. 물이 새는 곳의 개수 N과 테이프의 길이 L 입력
# 2. 물이 새는 곳의 위치 입력
# [보충설명] N과 L은 1000 이하의 자연수, 물이 새는 곳의 위치는 1000 이하의 자연수
# 3. 물이 새는 곳 리스트의 최소값부터 최대값까지의 자연수의 개수만큼의 불리언 리스트 생성
# 4. 물이 새는 곳이 리스트에 있으면 해당 인덱스부터 L - 1까지의 지점을 True로 변환
# 5. 4와 동시에 테이프 개수에 1을 더함
# 6. 다음 물이 새는 곳이 True로 처리되어 있으면 패스, False일 경우 4와 5번 과정 반복
# 7. 필요한 테이프의 개수 출력

import sys
input = sys.stdin.readline

N, L = map(int, input().split())
leaks = list(map(int, input().split()))
leaks.sort()

cnt = 0
is_tape = [False] * (leaks[-1] + 1)  # 테이프를 붙였는지 여부를 판단
for pos in leaks:
    # print(f"{pos=}")
    # print(f"{is_tape[pos]=}")
    if not is_tape[pos]:
        for i in range(pos, min(leaks[-1] + 1, pos + L)):
            is_tape[i] = True
        cnt += 1
        # print(f"{cnt=}")
        # print(f"{is_tape=}")
print(cnt)
