# 1384: 메시지
# 특이사항: 다국어(영어)(한국어 번역)
# 유의사항: n줄의 순서는 아이들이 앉아있고 종이를 넘기던 순서에 해당
# 알고리즘 분류: 구현

# 1. 각 그룹에 참여한 아이들의 수 n 입력
# 2. n줄에 걸쳐 활동을 끝마친 종이 n장 입력
# 3. 이름을 담은 큐 생성
# 4. 각 이름 중 N이 있을 때마다 큐를 오른쪽으로 회전시킴
# 5-1. 아무도 나쁜 말을 하지 않았으면 "Nobody was nasty" 출력
# 5-2. 나쁜 말을 한 사람은 첫 번째 종이부터, 왼쪽에서 오른쪽으로 출력

from collections import deque
import sys
input = sys.stdin.readline
group_num = 1

while True:
    n = int(input())

    if n == 0:
        break

    print(f"Group {group_num}")

    names_paper = dict()
    for _ in range(n):
        name_paper = list(input().split())
        name, paper_list = name_paper[0], name_paper[1:]
        names_paper[name] = paper_list

    names = names_paper.keys()
    q = deque(names)
    papers = []
    for name in names:
        if 'N' not in names_paper[name]:
            pass
        else:
            idx = []
            for i, p in enumerate(names_paper[name]):
                if p == 'N':
                    idx.append(i)
            for i in idx:
                blamer = q[-(i + 1)]
                print(f"{blamer} was nasty about {name}")
        papers += names_paper[name]
        last = q.popleft()
        q.append(last)
    if 'N' not in papers:
        print("Nobody was nasty")
    print('\n', end='')
    group_num += 1
