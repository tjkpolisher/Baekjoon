# 15577: Prosjek
# 특이사항: 다국어(영어), 스페셜 저지
# 출처: COCI (Croatian Open Competition in Informatics) 2017/2018 Contest #7 1번
# 알고리즘 분류: 수학/자료 구조/그리디 알고리즘/정렬/우선순위 큐

# 1. 과제의 개수를 뜻하는 정수 N 입력 (1 ≤ N ≤ 20)
# 2. N개의 줄에 걸쳐 수학 성적의 등급 X_i 리스트에 입력 후 리스트를 내림차순으로 정렬 (1 ≤ X_i ≤ 5)
# 3. 리스트의 가장 작은 두 원소를 리스트에서 pop하고 그 평균을 리스트에 저장 (리스트를 스택처럼 취급)
# 4. 3번 과정을 스택의 리스트의 길이가 1이 될 때까지 반복
# 5. 리스트에 남은 원소를 소수점 6자리까지 출력

N = int(input())
grades = []
for _ in range(N):
    grades.append(int(input()))

grades.sort(reverse=True)

while len(grades) > 1:
    a = grades.pop()
    b = grades.pop()
    grades.append((a + b) / 2)

print(f"{grades[0]:.6f}")
