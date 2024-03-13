# 1543: 문서 검색

# 1. 문서 입력(길이 최대 2500)
# 2. 문서에서 검색하고 싶은 단어 입력(길이 최대 50)
# 3. [반복문]
# 3-1. 문서에서 검색하고 싶은 단어가 나오면 인덱스 저장
# 3-2. 해당 인덱스 이후를 슬라이스
# 3-3. 원본 문서의 길이가 단어 길이보다 짧아질 때까지 반복
# 4. 단어가 나온 횟수 출력

import sys
input = sys.stdin.readline

d = input().rstrip()
word = input().rstrip()

cnt = 0
if word not in d:
    pass
else:
    while len(d) >= len(word):
        if word not in d:
            break
        d = d[d.index(word) + len(word):]
        cnt += 1

print(cnt)
