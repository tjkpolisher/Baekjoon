# 8975: PJESMA
# 특이사항: 다국어(영어)
# 출처: Croatian Highschool Competitions in Informatics 2008 Regional Competition - Juniors 2번
# 알고리즘 분류: 자료 구조/문자열/해시를 사용한 집합과 맵/트리를 사용한 집합과 맵

# 1. 노래 제목의 단어 개수 N 입력 (1 ≤ N ≤ 50)
# 2. N줄에 걸쳐 노래 제목에 들어가는 단어를 1개씩 입력
# 3. 가사에 들어가는 단어의 개수 M 입력 (1 ≤ M ≤ 10,000)
# 4. M줄에 걸쳐 가사에 들어가는 단어를 1개씩 입력
# [보충설명] 가사에 들어가는 모든 단어는 1 ~ 15개의 영어 소문자로 구성됨.
# 5-1. 가사에 들어가는 단어들을 순회하면서 노래 제목에 들어가는 단어인지를 체크
# 5-2. 만약 현재까지 체크한 단어의 개수가 N // 2 이상일 경우 현재 가사 속 단어 목록의 인덱스를 출력 후 종료

from math import ceil
import sys
input = sys.stdin.readline

N = int(input())
titles = {}
for _ in range(N):
    titles[input().rstrip()] = False

M = int(input())
lyrics = []
for _ in range(M):
    lyrics.append(input().rstrip())

cnt = 0
for i in range(M):
    word = lyrics[i]
    if word in titles and not titles[word]:
        cnt += 1
        titles[word] = True
    if cnt >= ceil(N / 2):
        print(i + 1)
        break
