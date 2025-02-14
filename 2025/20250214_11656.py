# 11656: 접미사 배열
# 알고리즘 분류: 문자열/정렬

# 1. 문자열 S 입력 (S는 영어 소문자로만 구성된 길이 1000 이하의 문자열)
# 2. S의 모든 문자를 큐에 넣고 하나씩 pop (단, 원본 S를 먼저 리스트에 저장한 뒤 pop 수행)
# 3. pop한 뒤 남은 문자들은 join해 생성된 문자열을 리스트에 저장
# 4. 접미사 리스트를 사전 순으로 정렬
# 5. 정렬된 리스트의 원소를 한 줄에 하나씩 출력

from collections import deque

S = deque(input())
S_list = []
while S:
    S_list.append(''.join(S))
    S.popleft()

S_list.sort()
for word in S_list:
    print(word)
