# 7662: 이중 우선순위 큐
# 특이사항: 다국어(영어)(한국어 번역)
# 출처: ICPC Daejeon Nationalwide Internet Competition 2013 D번
# 알고리즘 분류: 자료 구조/트리를 사용한 집합과 맵/우선순위 큐

# 1. 테스트 데이터의 개수 T 입력
# 2. 각 테스트 데이터의 첫째 줄에 Q에 적용할 연산의 개수 k 입력 (k ≤ 1,000,000)
# 3. 최대 힙 max_Q, 최소 힙 min_Q, 특정 연산에서 삽입한 번호가 삭제되었는지를 체크하는 Boolean 리스트 생성
# 4. k개의 줄 각각에 연산을 나타내는 문자('D' 또는 'I')와 정수 n 입력
# [보충설명] 'I n'은 n을 Q에 삽입, 'D 1'는 Q에서 최대 우선순위 삭제, 'D-1'은 Q에서 최소 우선순위 삭제
# 5. 모든 연산을 처리한 후에 현재까지 삭제된 값이 남아있다면 min_Q와 max_Q에서 제거
# 6-1. 두 힙 중 하나라도 비어있다면 'EMPTY'를 출력
# 6-2. 그렇지 않다면 두 힙에 남아 있는 최대값과 최소값을 한 줄에 공백으로 구분해 출력.

from heapq import heappop, heappush
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k = int(input())
    min_Q = []
    max_Q = []
    is_deleted = [True] * k
    for i in range(k):
        operation = input().rstrip()
        op, num = operation.split()
        num = int(num)
        if operation.startswith('I'):
            # 삽입 연산
            heappush(min_Q, (num, i))
            heappush(max_Q, (-num, i))
            is_deleted[i] = False
        else:
            if num == 1:
                # 최대 힙
                # 삭제되지 않은 값을 찾고, 삭제된 값을 힙에서 제거
                while max_Q and is_deleted[max_Q[0][1]]:
                    heappop(max_Q)
                if max_Q:
                    is_deleted[max_Q[0][1]] = True
                    heappop(max_Q)
            else:
                # 최소 힙
                while min_Q and is_deleted[min_Q[0][1]]:
                    heappop(min_Q)
                if min_Q:
                    is_deleted[min_Q[0][1]] = True
                    heappop(min_Q)

    # 연산이 끝난 후 삭제된 값들을 각각 최소 힙과 최대 힙에서 제거
    while max_Q and is_deleted[max_Q[0][1]]:
        heappop(max_Q)
    while min_Q and is_deleted[min_Q[0][1]]:
        heappop(min_Q)

    # 테스트 케이스에 대한 정답 출력
    if not min_Q:
        print("EMPTY")
    else:
        print(-max_Q[0][0], min_Q[0][0])
