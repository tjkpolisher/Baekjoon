# 1343: 폴리오미노
# 알고리즘 분류: 구현/그리디 알고리즘

## 1. 보드판 입력
## 2. 보드판의 영역을 '.'을 기준으로 split
## 3. Split한 영역에 홀수 개의 X를 갖는 타일이 있을 경우 -1 출력 후 종료
## 4. 타일의 개수에 맞게 'AAAA'를 먼저 배치할 수 있는지 확인 후 남는 영역에 'BB' 배치
## 5. 배치 후, 타일과 '.'을 원래 순서에 맞게 배치하여 출력

board = input()
board = board.replace("XXXX", "AAAA")
board = board.replace("XX", "BB")

if 'X' in board:
    print(-1)
else:
    print(board)
