# 16502: 그녀를 찾아서
# 특이사항: 스페셜 저지 (오차는 10^(-2)까지 허용)
# 출처: 한양대학교 ERICA 캠퍼스 2018 ERICA Software-Up Programming Contest League B G번
# 알고리즘 분류: 그래프 이론

# 1. 쇼핑 시간 입력(단위는 10분, 10보다 작거나 같은 자연수로 주어짐)
# 2. 간선의 개수 입력 (1 ≤ M ≤ 10)
# 3. M개의 줄에 걸쳐 간선의 정보(시작 매장, 도착 매장, 확률) 입력
# 4. 간선의 정보를 바탕으로 노드(매장)별 연결 그래프 생성
# 5. 각 노드별로 주어진 시간만큼 행렬 곱셈을 수행해 확률을 계산
# 6. 계산된 확률을 퍼센트 단위로 환산해 출력

t = int(input())
M = int(input())

# 각 노드 별 이동 확률을 저장할 인접행렬 생성
matrix = [[0.0 for _ in range(4)] for _ in range(4)]
for _ in range(M):
    start, end, prob = input().split()
    i, j = ord(start) - ord('A'), ord(end) - ord('A')
    matrix[i][j] = float(prob)

current_prob = [0.25] * 4


def update_prob(matrix, current_prob):
    new_prob = [0.0] * 4
    for i in range(4):
        for j in range(4):
            new_prob[j] += current_prob[i] * matrix[i][j]
    return new_prob


for _ in range(t):
    current_prob = update_prob(matrix, current_prob)

for prob in current_prob:
    print(f"{prob * 100:.2f}")
