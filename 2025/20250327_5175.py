# 5175: 문제없는 문제
# 특이사항: 다국어(영어)(한국어 번역)
# 출처: USC Programming Contest Fall 2007 A번
# 알고리즘 분류: 브루트포스 알고리즘/비트마스킹

# 1. 테스트 케이스의 수 K 입력
# 2. 테스트 케이스의 첫 줄에 두 정수 M과 N 입력 (1 ≤ M,N ≤ 20)
# [보충설명] M은 대회에서 사용할 알고리즘의 개수, N은 총 문제의 개수
# 3. N개의 줄에 걸쳐 각 문제가 어떤 알고리즘을 사용하는지 입력
# [보충설명] 한 문제는 한 가지 이상의 알고리즘을 사용. 여러 개를 사용할 경우 공백으로 구분됨.
# 4. 입력받은 순서대로 문제 번호를 뜻하는 알파벳(chr(65 + j)): 알고리즘 리스트의 딕셔너리로 저장
# 5. 딕셔너리의 값을 이용해 1개 ~ M개까지 선택하는 조합으로 구성
# 5-1. 선택한 조합의 원소들을 집합에 넣었을 때 길이를 판별
# 5-2. 길이가 M이 되지 않으면 다음 조합으로 넘어감
# 5-3. 길이가 M이 되면 해당 조합의 키를 정답 리스트로 만들고 반복문 종료
# 6. 정답 리스트를 주어진 양식에 맞게 출력

import sys
from itertools import combinations
input = sys.stdin.readline

K = int(input())

for i in range(1, K + 1):
    M, N = map(int, input().split())

    table = {}
    for j in range(N):
        algorithms = list(map(int, input().split()))
        table[chr(65 + j)] = algorithms

    flag = False
    for j in range(1, M + 1):
        # 전체 원소 중 1개 ~ M개를 선택하는 조합을 시도
        if flag:
            break
        combs = combinations(table.keys(), j)
        for comb in combs:
            temp = set()  # 새 조합을 시도할 때마다 집합을 초기화
            for k in comb:
                if flag:
                    break
                for comp in table[k]:
                    temp.add(comp)
            if len(temp) == M:
                answer = list(comb)
                flag = True
                break

    # 결과 출력 단계
    print(f"Data Set {i}: {' '.join(answer)}")
    if i < K:
        print()  # 각 테스트 케이스의 사이에 빈 줄을 하나 출력
