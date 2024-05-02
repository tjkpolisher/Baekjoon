# 26043: 식당 메뉴
# 알고리즘 분류: 자료 구조/정렬/큐

# 1. 식당 정보의 개수 n 입력 (1 ≤ n ≤ 500,000)
# 2. n개의 줄에 걸쳐 한 줄에 하나의 정보 입력
# 2-1. "1 a b" 유형일 경우 학생 번호와 좋아하는 메뉴 번호 입력
# 2-2. "2 b" 유형일 경우 메뉴 번호 b가 준비되어 맨 앞 학생 pop
# [보충설명] 1 ≤ a ≤ n (a의 값은 중복 없음), b는 1 또는 2
# 3-1. 본인이 원하는 메뉴를 먹었을 경우 학생 목록 A에 번호 저장
# 3-2. 본인이 좋아하지 않는 메뉴를 먹었을 경우 학생 목록 B에 번호 저장
# 3-3. 학교 식당에 도착했으나 식사를 하지 못한 학생은 학생 목록 C에 저장
# 4. A, B, C를 한 줄에 한 목록씩 오름차순으로 출력
# 4-1. 단, 학생 목록에 학생이 없는 경우 None을 출력

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
A, B, C = [], [], []  # 세 종류의 학생 목록
q = deque()
for _ in range(n):
    s = input().rstrip()
    # 유형 1의 정보가 들어올 때
    if s.startswith("1"):
        i, a, b = s.split()
        a = int(a)
        b = int(b)
        q.append([a, b])
    # 유형 2의 정보가 들어올 때
    else:
        i, b = s.split()
        b = int(b)
        student_info = q.popleft()  # 줄 맨 앞에 있는 학생 정보 pop
        if student_info[1] == b:
            A.append(student_info[0])
        else:
            B.append(student_info[0])

# 모든 s가 입력되었다면 q에 남은 인원은 모두 식사를 하지 못하므로 C에 번호 입력
while q:
    student_info = q.popleft()
    C.append(student_info[0])

A.sort()
B.sort()
C.sort()

for name_list in [A, B, C]:
    if not name_list:
        print("None")
    else:
        print(*name_list)
