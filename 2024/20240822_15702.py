# 15702: 중간고사 채점
# 알고리즘 분류: 구현/정렬

# 1. 문제의 개수 N, 응시자의 수 M 입력 (1 ≤ N ≤ 100, 1 ≤ M ≤ 100)
# 2. N개의 문제의 배점 입력 후 문제 번호와 배점을 키-값으로 삼는 딕셔너리로 변환
# 3. M개의 줄에 걸쳐 응시자의 정보(수험 번호, 문제 채점 결과) 입력
# [보충설명] 수험 번호는 100,000 이하의 자연수, 문제 채점 결과는 o 또는 x로 주어짐
# 4. 수험생 별로 문제 번호에 맞게 배점을 산정 후, 수험 번호와 점수를 입력한 리스트에 입력
# 5. 가장 높은 점수를 얻은 학생의 번호와 점수를 공백으로 구분해 출력

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
scores = list(map(int, input().split()))
score_table = {i + 1: scores[i] for i in range(N)}

result_table = []
for _ in range(M):
    student_score = list(input().split())
    student_num = int(student_score[0])
    net_score = 0
    for i in range(1, N + 1):
        result = student_score[i]
        if result == 'O':
            net_score += score_table[i]
    result_table.append([student_num, net_score])

result_table.sort(key=lambda x: (-x[1], x[0]))
print(result_table[0][0], result_table[0][1])
