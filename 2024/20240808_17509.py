# 17509: And the Winner Is... Ourselves!
# 특이사항: 다국어(영어)
# 출처: 2019 KAIST 9th ICPC Mock Competition B번
# 알고리즘 분류: 그리디 알고리즘/정렬

# 1. 11개의 줄에 걸쳐 문제 해결에 필요한 시간 D_i, 오답의 개수 V_i 입력
# [보충설명] D_i ≥ 1, 0 ≤ V_i ≤ 1000, D_i의 총합은 300 이하.
# 2. D_i와 V_i를 원소로 갖는 리스트를 전체 리스트에 추가
# 3. D_i를 기준으로 오름차순으로 전체 리스트 정렬
# 4. D의 누적합을 구하여 T 리스트를 구함
# 5. T 리스트와 정렬된 V를 이용해 T + 20V를 누적합으로 계산하여 출력

D_and_V = []
for _ in range(11):
    D, V = map(int, input().split())
    D_and_V.append((D, V))

D_and_V.sort(key=lambda x: x[0])
print(f"{D_and_V=}")
T = [D_and_V[0][0]]
for i in range(1, 11):
    T.append(T[-1] + D_and_V[i][0])

ans = 0
for i in range(11):
    ans += (T[i] + 20 * D_and_V[i][1])
print(ans)
