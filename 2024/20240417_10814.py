# 10814: 나이순 정렬
# 알고리즘 분류: 정렬

# 1. 회원 수 N 입력
# 2. N개의 줄에 걸쳐 각 회원의 나이와 이름 입력
# 3. 나이 순으로 오름차순, 나이가 같으면 가입한 순서대로 나이와 이름을 공백으로 구분해 출력

N = int(input())
clients = []
for i in range(N):
    age, name = input().split()
    clients.append([i, int(age), name])

clients.sort(key=lambda x: (x[1], x[0]))
for i in range(N):
    print(clients[i][1], clients[i][2])
