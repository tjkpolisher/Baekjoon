# 30866: NOT a SAT problem
# 특이사항: 스페셜 저지, 다국어(영어)(한국어 번역)
# 출처: 제10회 한양대학교 프로그래밍 경시대회(HCPC) 예비소집 B번
# 알고리즘 분류: 구현/해 구성하기

# 1. 논리 변수의 개수 N, CNF에 있는 절의 개수 M 입력
# 2. M개의 줄에 걸쳐 절의 정보 입력 후 리스트에 저장
# 3. 각 절의 변수 할당 상태 배열 초기화 (0: 미정, 1: 참, -1: 거짓)
# 4. 각 절을 하나씩 확인하여 거짓으로 만들 수 있는지 검사
# 5. 절의 모든 리터럴을 거짓으로 만들기 위한 변수 할당 시도
# 6. 이 절을 거짓으로 만들 수 있다면 YES 출력 후 중료
# 6-1. 이 절로는 불가능하다면 설정한 변수들을 초기화하고 다음 절 시도
# 8. 모든 절을 확인했지만 거짓으로 만들 수 없는 경우 NO 출력


N, M = map(int, input().split())
clauses = []
for _ in range(M):
    line = list(map(int, input().split()))
    clauses.append(line[1:])

assignment = [0] * (N + 1)

for clause in clauses:
    used_vars = []
    can_make_false = True

    for literal in clause:
        var = abs(literal)
        needed_value = -1 if literal > 0 else 1

        if assignment[var] == 0:
            assignment[var] = needed_value
            used_vars.append(var)
        elif assignment[var] != needed_value:
            can_make_false = False
            break

    if can_make_false:
        for i in range(1, N + 1):
            if assignment[i] == 0:
                assignment[i] = 1

        print("YES")
        print(*[1 if assignment[i] == 1 else 0 for i in range(1, N + 1)])
        exit()

    for var in used_vars:
        assignment[var] = 0

print("NO")
