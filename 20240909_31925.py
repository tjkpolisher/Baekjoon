# 31925: APC2shake!
# 출처: 2024 아주대학교 프로그래밍 경시대회 APC Div.1 C번, Div.2 D번, Open Contest D번
# 알고리즘 분류: 구현/문자열/정렬

# 1. 참가자의 수 N 입력 (1 ≤ N ≤ 10^4)
# 2. N개의 줄에 걸쳐 이름, 재학 여부, 수상 여부, shake 최고 성적 S, 2024 APC 성적(등수) A 입력
# [보충설명] 이름의 길이는 10을 넘지 않음, 재학 여부는 jaehak/hewahk으로 구분
# [보충설명] ICPC 수상 여부는 winner/notyet으로 구분, 1 ≤ S ≤ 10^4(-1이면 아직 진출 못함), 1 ≤ A ≤ N
# 3. 입력받은 정보 중 다음과 같은 조건을 통해 진출자를 선정하고 모든 조건을 충족하면 이름과 A를 리스트에 저장
# 3-1. 휴학 중인 학생(hewhak)은 제외
# 3-2. ICPC 수상자(winner)는 제외
# 3-3. shake! 순위가 3위 이내, 즉 S가 3 이하이면 제외
# 4. 리스트에 저장된 이름을 A 기준 내림차순으로 정렬
# 5. 진출자의 수 M과 상위 10명의 이름을 사전 순으로 정렬 후 출력

import sys
input = sys.stdin.readline

N = int(input())
name_and_A = []
for _ in range(N):
    name, jaehak, icpc, S, A = input().rstrip().split()
    S, A = int(S), int(A)
    if jaehak == 'hewhak':
        continue
    if icpc == 'winner':
        continue
    if S <= 3 and S != -1:
        continue
    name_and_A.append([name, A])

name_and_A.sort(key=lambda x: x[1])
answer = name_and_A[:10]
print(len(answer))
answer.sort(key=lambda x: x[0])
for ans in answer:
    print(ans[0])
