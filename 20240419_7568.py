# 7568: 덩치
# 알고리즘 분류: 구현/브루트포스 알고리즘

# 1. 전체 사람의 수 N 입력 (2 ≤ N ≤ 50)
# 2. N개의 줄에 걸쳐 몸무게와 키를 나타내는 x, y 입력(10 ≤ x, y ≤ 200)
# 3. 덩치를 저장한 리스트를 순회하며 키와 몸무게가 모두 클 경우 등수에 1을 더함
# 4. 더 이상 순위가 작아지지 않으면 순위 출력

N = int(input())
size = []  # 덩치를 판단하는 두 수치를 저장할 리스트
for _ in range(N):
    x, y = map(int, input().split())
    size.append([x, y])

for i in size:
    rank = 1
    for j in size:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=' ')
