# 2755: 이번학기 평점은 몇점?

# 1. 이번 학기에 들은 과목 수 n 입력
# 2. n줄에 걸쳐 각 과목의 과목명, 학점, 성적 입력
# 3. A+부터 F까지 성적을 평점으로 변환
# 4. 학점 * 성적을 모두 더한 뒤 총 학점으로 나누어 출력
n = int(input())

answer = 0
scores = 0
gpa_table = {'A+': 4.3, 'A0': 4.0, 'A-': 3.7,
             'B+': 3.3, 'B0': 3.0, 'B-': 2.7,
             'C+': 2.3, 'C0': 2.0, 'C-': 1.7,
             'D+': 1.3, 'D0': 1.0, 'D-': 0.7,
             'F': 0.0}

for _ in range(n):
    subject, score, gpa = input().split()
    score = int(score)
    scores += score
    gpa_score = gpa_table[gpa]
    answer += score * gpa_score

answer /= scores

print(f"{round(answer + 0.0001, 2):.2f}")
