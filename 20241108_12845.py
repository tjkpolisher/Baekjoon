# 12845: 모두의 마블
# 출처: 숭실대학교 SCCC 2016 Summer Contest G번
# 알고리즘 분류: 그리디 알고리즘

# 1. 카드의 개수 n 입력 (1 ≤ n ≤ 1,000)
# 2. 카드의 레벨 L_i를 입력 (0 < L_i ≤ 100,000)
# 3. 레벨을 담은 리스트를 내림차순으로 정렬
# 4. 0번부터 시작해 현재 레벨과 그 다음 레벨을 더함
# 5. 이때, 다음 레벨이 현재 레벨보다 클 경우 레벨 변수를 갱신
# 6. 마지막 인덱스까지 4번과 5번을 반복
# 7. 누적된 골드 출력

n = int(input())
levels = list(map(int, input().split()))

levels.sort(reverse=True)
level_0 = levels[0]

golds = 0
for i in range(1, n):
    golds += level_0 + levels[i]
    if level_0 < levels[i]:
        level_0 = levels[i]

print(golds)
