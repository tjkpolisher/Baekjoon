# 5104: NoMoPhobia
# 특이사항: 다국어(영어)
# 출처: NZPC 2010 E번
# 알고리즘 분류: 구현/자료 구조/문자열/정렬/해시를 사용한 집합과 맵/트리를 사용한 집합과 맵

# 1. 매 시나리오마다 첫 줄에 주 번호 W, 디메리트의 수 N 입력 (0 < W, N <= 50)
# 1-1. 입력값이 0, 0인 경우 종료
# 2. N개의 줄에 걸쳐 학생 이름과 디메리트 코드 입력
# 3-1. 학생이 처음 추가되었을 경우 딕셔너리에 이름과 디메리트 코드에 해당하는 점수 더하기
# 3-2. 학생이 이미 있는 경우 기존 점수에 더하기
# 4. 모든 입력이 끝난 후 100점 미만인 학생을 딕셔너리에서 제거
# 5. 표시된 형식에 맞게 압수 명단 출력
# 5-1. 압수된 사람이 없을 경우에는 명단 대신 “No phones confiscated”를 출력.

import sys
input = sys.stdin.readline

demerit_dict = {'TT': 75, 'TX': 50, 'PR': 80,
                'RT': 30, 'AP': 25, 'PX': 60}
while True:
    W, N = map(int, input().split())
    if W == 0 and N == 0:
        break

    students_dict = {}
    for _ in range(N):
        student, demerit = input().rstrip().split()
        if student not in students_dict:
            students_dict[student] = demerit_dict[demerit]
        else:
            students_dict[student] += demerit_dict[demerit]

    name_list = list(students_dict.keys())
    for name in students_dict.keys():
        if students_dict[name] < 100:
            name_list.remove(name)

    if not name_list:
        print(f"Week {W} No phones confiscated")
    else:
        print(f"Week {W} {','.join(name_list)}")
