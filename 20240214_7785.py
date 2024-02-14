# 7785: 회사에 있는 사람
# 특이사항: 다국어(영어)(한국어 번역)
# 알고리즘 분류: 자료구조/해시를 사용한 집합과 맵

## 1. 출입 기록의 수 n 입력
## 2. n개의 줄에 걸쳐 출입 기록 입력 - "enter" 또는 "leave"가 함께 표시됨. - 딕셔너리에 입력
## 3. 입력이 끝난 후 딕셔너리의 값이 enter로 남아있는 사람의 이름 추출
## 4. 이름을 역순으로 한 줄에 한 명씩 출력

n = int(input())
table = {}

for _ in range(n):
    name, is_in = input().split()
    table[name] = is_in

names = [n for n in table.keys() if table[n] == 'enter']
names.sort(reverse=True)
for n in names:
    print(n)
