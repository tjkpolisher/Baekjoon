# 2149: 암호 해독
# 특이사항: 다국어(영어)
# 출처: 2003 East Central Regional Contest A번
# 알고리즘 분류: 구현/문자열/정렬

# 1. 키 입력 (길이는 10자 이하)
# 2. 암호문 입력 (길이는 100자 이하이며, 항상 키의 길이의 배수)
# 3. 키의 문자들을 알파벳 순서대로 정렬
# 4. 암호문의 문자를 (len(cypher) // len(key_string)) x 키 길이 의 2차원 리스트에 저장
# 5. 키의 원래 문자 순서와 정렬된 순서를 참조해 각각의 열을 정답 테이블(2차원 리스트)에 재배치
# 5-1. 키에 중복된 문자가 있어 이미 해당 인덱스의 열에 문자가 있으면 다음 인덱스를 탐색
# 6. 정답 표의 문자를 행 순서대로 join해서 한 줄에 출력

import sys
from collections import deque
input = sys.stdin.readline

key_string = input().rstrip()
cypher = input().rstrip()

key_list = list(key_string)
key_index_list = deque(list(enumerate(key_list)))
sorted_key_list = sorted(key_list)

n_row = len(cypher) // len(key_string)
cypher_table = [[0 for _ in range(len(key_string))] for i in range(n_row)]
idx = 0
for i in range(len(key_string)):
    for j in range(n_row):
        cypher_table[j][i] = cypher[idx]
        idx += 1

ans_table = [[0 for _ in range(len(key_string))] for i in range(n_row)]
for _ in range(len(key_string)):
    orig_key = key_index_list.popleft()
    orig_idx, orig_char = orig_key
    cypher_idx = sorted_key_list.index(orig_char)
    for j in range(n_row):
        ans_table[j][orig_idx] = cypher_table[j][cypher_idx]
    sorted_key_list[cypher_idx] = 0  # 중복 문자 처리

for i in range(n_row):
    print(''.join(ans_table[i]), end='')
