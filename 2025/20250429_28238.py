# 28238: 정보 선생님의 야망
# 특이사항: 스페셜 저지
# 출처: 송도고등학교 코드마스터 2023 C번
# 알고리즘 분류: 구현/브루트포스 알고리즘

# 1. 알고리즘 특강을 듣고자 하는 학생 수 n 입력 (1 ≤ n ≤ 10^6)
# 2. n개의 줄에 걸쳐 i번째 학생의 요일별 참가 가능 여부를 의미하는 다섯 개의 정수 입력
# [보충설명] 월요일부터 금요일까지의 순서대로 1이면 참여 가능, 0이면 참여 불가를 의미.
# 3. 입력받은 줄의 어떤 학생 칸이 1이면 아래 과정 실행
# 3-1. 그 다음 칸들을 순회하면서 해당 칸도 1이면 2차원 최적 날짜 테이블의 해당 행과 열의 원소를 1로 변경
# 4. 2차원 최적 날짜 테이블을 순회하면서 임시값이 해당 칸보다 작으면 최대 학생 수 임시값 갱신
# 4-1. 임시값을 갱신하면서 특강 일정에 해당하는 날짜의 인덱스 기록
# 5. 최대 학생 수 출력
# 6. 특강 일정 날짜를 길이 5의 리스트에 입력하여 출력

import sys
input = sys.stdin.readline

n = int(input())

max_cnt = -1
best_days = [[0] * 5 for _ in range(5)]

for _ in range(n):
    student = list(map(int, input().split()))
    for i in range(5):
        if student[i] == 1:
            for j in range(i + 1, 5):
                if student[j] == 1:
                    best_days[i][j] += 1

best_1, best_2 = 0, 1
for i in range(5):
    for j in range(i + 1, 5):
        if best_days[i][j] > max_cnt:
            max_cnt = best_days[i][j]
            best_1, best_2 = i, j

days = [0] * 5
days[best_1], days[best_2] = 1, 1

print(max_cnt)
print(*days)
