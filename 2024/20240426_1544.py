# 1544: 사이클 단어
# 알고리즘 분류: 구현/자료 구조/문자열/브루트포스 알고리즘/해시를 사용한 집합과 맵

# 1. 단어의 개수 N 입력
# 2. 단어가 한 줄에 하나씩 주어짐.
# 3. 길이가 다른 단어와 다르면 서로 다른 단어의 개수에 1을 더함.
# 4. 길이가 같을 경우 단어의 문자를 큐로 만들어 돌리면서 같은 단어가 나오는지 체크.
# 4-1. 순회 중에 같은 단어의 배치가 나오지 않을 경우 서로 다른 단어 개수에 1을 더함.
# 5. 서로 다른 단어 개수 출력

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
words = dict()
cnt = 0
for i in range(N):
    word = input().rstrip()

    if i == 0 or len(word) not in words:
        cnt += 1
        words[len(word)] = [word]
        continue
    else:
        q = deque(word)
        is_same = False
        words_to_compare = words[len(word)]
        for w in words_to_compare:
            for _ in range(len(word)):
                p = q.popleft()
                q.append(p)
                is_same = (w == ''.join(q))
                # 어느 한 단어와도 동일했을 경우 정지
                if is_same:
                    break
            if is_same:
                break
        # 길이가 같은 모든 단어와 비교해도 다른 단어일 때
        # 비교할 단어 리스트를 전부 순회했을 때만 기능하는 절입니다.
        else:
            cnt += 1
            words[len(word)].append(word)

print(cnt)
