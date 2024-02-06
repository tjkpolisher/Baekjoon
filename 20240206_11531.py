# 11531: ACM 대회 채점
# 특이사항: 다국어(영어)(한국어 번역)

## 1. 문제 이름, 제출 시각을 저장할 딕셔너리 생성
## 2. [반복문] -1이 입력될 때까지 입력을 받고 아래 절차 수행
## 2-1. 제출 시각, 문제 이름, 결과 순으로 입력 후 딕셔너리에 입력
## 2-2. 문제 별 제출 시각을 입력받을 때마다 값에 해당하는 리스트에 입력
## 2-3-1. 결과가 맞았을 경우, 그 전까지의 시간을 더해서 패널티 계산
## 2-3-2. 결과가 틀렸을 경우, 제출 시각을 리스트에 입력
## 3. 푼 문제 수와 총 걸린 시간(페널티 포함)을 출력

problem_table = {}
penalty = 0
correct = 0

while True:
    log = input()
    if log == "-1":
        break
    m, name, result = log.split()
    m = int(m)
    if name not in problem_table:
        problem_table[name] = [m]
    else:
        problem_table[name].append(m)
    
    if result == 'right':
        penalty += (m + 20 * len(problem_table[name][:-1]))
        correct += 1

print(correct, penalty)
