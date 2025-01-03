# 16937: 두 스티커
# 알고리즘 분류: 구현/브루트포스 알고리즘/기하학/많은 조건 분기

# 1. 모눈종이의 크기 H, W 입력
# 2. 스티커의 수 N 입력 (1 ≤ H,W,N ≤ 100)
# 3. N개의 줄에 걸쳐 스티커의 크기 R_i, C_i 입력 (1 ≤ R_i,C_i ≤ 100)
# 4. 스티커를 넓이 순으로 내림차순 정렬
# 5. 어떻게 해도 두 스티커를 붙일 수 없는 경우를 정답의 초기값 0으로 설정
# 6. 투 포인터 적용
# 6-1. 두 스티커에 대하여 R_i, C_i, R_j, C_j 획득
# 6-2. 가로로 나란히 놓는 경우와 세로로 나란히 놓는 경우 스티커를 배치할 수 있는지 판단
# 6-3. 총 네 가지 케이스 중 한 가지라도 만족할 경우 넓이 합산 및 넓이 최대값 갱신
# 7. 넓이의 최대값 출력

import sys
input = sys.stdin.readline

H, W = map(int, input().split())
N = int(input())
stickers = []
for _ in range(N):
    stickers.append(list(map(int, input().split())))

stickers.sort(key=lambda x: x[0] * x[1], reverse=True)
ans = 0


def can_place(r1, c1, r2, c2):
    # 가로로 나란히 배치하는 두 경우의 수
    if r1 + r2 <= H and max(c1, c2) <= W:
        return True
    if c1 + c2 <= W and max(r1, r2) <= H:
        return True

    # 세로로 나란히 배치하는 두 경우의 수
    if r1 + r2 <= W and max(c1, c2) <= H:
        return True
    if c1 + c2 <= W and max(r1, r2) <= H:
        return True

    return False


for i in range(N):
    r1, c1 = stickers[i]
    for j in range(i + 1, N):
        r2, c2 = stickers[j]
        for (nr1, nc1) in [(r1, c1), (c1, r1)]:
            for (nr2, nc2) in [(r2, c2), (c2, r2)]:
                if can_place(nr1, nc1, nr2, nc2):
                    ans = max(ans, nr1 * nc1 + nr2 * nc2)

print(ans)
