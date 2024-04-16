# 28078: 중력 큐
# 알고리즘 분류: 구현/자료 구조/많은 조건 분기/덱

# 1. 쿼리의 개수 Q 입력 (1 ≤ Q ≤ 500,000)
# 2. Q개의 줄에 걸쳐 첫 번째 쿼리부터 순서대로 각 쿼리의 정보 입력
# 3. 쿼리의 종류에 따라 아래 연산 진행
# 3-1. push: b일 경우 맨 뒤에 공 삽입, w일 경우 가림막 삽입
# 3-2. pop: 가장 앞에 있는 공이나 가림막 하나 꺼내기. 단, 큐가 비어있으면 pass
# 3-3. rotate: l일 경우 반시계 방향, r일 경우 시계 방향으로 90도 회전 후 중력에 의해 공을 떨굼(가림막 이상은 제외)
# 3-4. count: b일 경우 공의 개수를, w일 경우 가림막의 개수 출력
# [참고사항] 마지막 쿼리는 항상 count b

"""from collections import deque

Q = int(input())
queue = deque()
degree = 0  # 회전각 0, 90, 180, 270
n_balls = 0  # 공의 개수
n_walls = 0  # 가림막의 개수


def falling_balls():
    global n_balls
    if degree in [90, 270]:  # 수직일 때만 공이 떨어짐 처리
        new_queue = deque()
        ball_falling = True
        for item in reversed(queue):
            if item == 'w':
                ball_falling = False
            if item == 'b' and ball_falling:
                n_balls -= 1  # 공이 떨어지면 공 개수 감소
            else:
                new_queue.appendleft(item)
        queue.clear()
        queue.extend(new_queue)


for _ in range(Q):
    query = input().split()
    if query[0] == "pop":
        if queue:
            item = queue.popleft()
            if item == 'b':
                n_balls -= 1
            elif item == 'w':
                n_walls -= 1
    elif query[0] == "push":
        item = query[1]
        if degree in [90, 270] and item == 'b':
            # 수직 위치에 공을 추가하는 경우, 가림막이 없다면 공은 즉시 떨어짐
            if not queue or queue[-1] != 'w':
                continue
        queue.append(item)
        if item == 'b':
            n_balls += 1
        elif item == 'w':
            n_walls += 1
    elif query[0] == "rotate":
        if query[1] == 'l':
            degree = (degree - 90) % 360
        else:
            degree = (degree + 90) % 360
        falling_balls()
    elif query[0] == "count":
        if query[1] == 'b':
            print(n_balls)
        elif query[1] == 'w':
            print(n_walls)"""

import sys
from collections import deque
input = sys.stdin.readline


def solution():
    q = deque()  # 큐를 deque로 구현
    balls = 0  # 큐 내부의 공 개수
    walls = 0  # 큐 내부의 가림막 개수
    direction = 0  # 큐의 방향 (0: 가로, 1: 세로(위에서 아래로), 2: 가로(반대), 3: 세로(아래에서 위로))

    for _ in range(Q):
        query = input().split()

        if query[0] == 'push':
            item = query[1]
            # 큐의 방향이 가로(0 또는 2)일 때
            if (direction == 0 or direction == 2):
                q.appendleft(item)  # 큐의 앞에 원소 추가
                if item == 'b':
                    balls += 1
                else:
                    walls += 1
            # 큐의 방향이 세로(위에서 아래로, 1)일 때
            elif direction == 1:
                if item == 'b':
                    if q and q[-1] == 'w':  # 큐의 마지막이 가림막이면 공을 추가
                        balls += 1
                        q.appendleft(item)
                else:  # 가림막은 무조건 추가
                    walls += 1
                    q.appendleft(item)
            # 큐의 방향이 세로(아래에서 위로, 3)일 때
            elif direction == 3:
                if item == 'w':  # 가림막만 추가
                    walls += 1
                    q.appendleft(item)
        elif query[0] == 'pop':
            if q:  # 큐가 비어있지 않을 때
                if direction == 1:  # 큐의 방향이 세로(위에서 아래로, 1)일 때
                    if q[-1] == 'w':  # 큐의 마지막이 가림막이면
                        q.pop()  # 가림막 제거
                        walls -= 1
                        while q and q[-1] == 'b':  # 그 아래에 있는 공들도 제거
                            q.pop()
                            balls -= 1
                else:  # 다른 방향일 때는 단순히 큐의 마지막 원소 제거
                    item = q.pop()
                    if item == 'b':
                        balls -= 1
                    else:
                        walls -= 1
        elif query[0] == 'rotate':
            if query[1] == 'l':  # 반시계 방향으로 90도 회전
                direction = (direction - 1) % 4
            else:  # 시계 방향으로 90도 회전
                direction = (direction + 1) % 4
            # 큐의 방향이 세로(위에서 아래로, 1)이 되었을 때, 큐의 맨 아래에 있는 공들 제거
            if direction == 1:
                while q and q[-1] == 'b':
                    q.pop()
                    balls -= 1
            # 큐의 방향이 세로(아래에서 위로, 3)이 되었을 때, 큐의 맨 위에 있는 공들 제거
            elif direction == 3:
                while q and q[0] == 'b':
                    q.popleft()
                    balls -= 1
        elif query[0] == 'count':
            if query[1] == 'b':
                print(balls)  # 공의 개수 출력
            else:
                print(walls)  # 가림막의 개수 출력


if __name__ == '__main__':
    Q = int(input())
    solution()
