# 3227: MO
# 특이사항: 다국어(영어)
# 출처: Croatian Highschool Competitions in Informatics 2003 Regional Competition Juniors 2번
# 알고리즘 분류: 구현/시뮬레이션

# 1. 테이블의 사각형의 숫자 P, 두 선수의 총 행위 수 N 입력 (1 ≤ P ≤ 100, 1 ≤ N ≤ 1000)
# 2. P개의 Boolean을 저장하는 딕셔너리 생성
# 3. N개의 줄에 걸쳐 Mirko와 Slavko의 행위 입력
# [보충설명] Mirko가 백돌을 놓으며, 항상 선공. 그 뒤로 Mirko와 Slavko가 번갈아가며 돌을 놓음
# 4. 입력받은 사각형 번호의 딕셔너리를 현재 돌을 놓은 선수의 돌 색으로 전환
# 4-1. 이후, 사각형 번호의 특정 범위가 완전히 다른 색으로 둘러싸여 있을 경우 해당 범위의 돌을 전부 제거
# 5. 모든 입력이 끝난 후 백돌의 개수와 흑돌의 개수를 한 줄에 출력

P, N = map(int, input().split())
squares = {i: 0 for i in range(1, P + 1)}
order = True  # 백돌/흑돌 순서(True일 경우 Mirko의 백돌을 놓을 차례)

for i in range(N):
    move = int(input())
    # 현재 플레이어 색 결정
    color = 'w' if order else 'b'
    opponent = 'b' if order else 'w'

    squares[move] = color  # 현재 돌 놓기

    # 왼쪽 방향 검사
    temp_positions = []
    for pos in range(move - 1, 0, -1):
        if squares[pos] == opponent:
            # 상대 돌이 연속되는 중
            temp_positions.append(pos)
        elif squares[pos] == color:
            # 동일 색 돌 발견 -> 사이의 상대 돌 제거
            if temp_positions:
                for p in temp_positions:
                    squares[p] = 0
            break
        else:
            # 빈 칸 혹은 아무것도 아니면(사실 0만 가능) 중단
            break

    # 오른쪽 방향 검사
    temp_positions = []
    for pos in range(move + 1, P + 1):
        if squares[pos] == opponent:
            temp_positions.append(pos)
        elif squares[pos] == color:
            # 동일 색 돌 발견 -> 사이의 상대 돌 제거
            if temp_positions:
                for p in temp_positions:
                    squares[p] = 0
            break
        else:
            # 빈 칸이면 중단
            break

    order = not order

result = list(squares.values())
print(result.count('w'), result.count('b'))
