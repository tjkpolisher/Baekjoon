# 23253: 자료구조는 정말 최고야
# 특이사항: 자료구조라는 분류와 제목에 속지 맙시다. 사실상 정렬 문제입니다.

## 1. 교과서의 수 N, 교과서 더미의 수 M 입력
## 2. [반복문] 2xM 줄에 걸쳐 각 더미의 정보 입력
## 2-1. i번째 더미를 나타내는 첫 번째 줄에 교과서의 수 k_i 입력
## 2-2. 두 번째 줄에서 k_i개의 정수를 입력받아 스택화
## 2-3-1. 더미가 내림차순으로 정렬되어 있지 않으면 "No" 출력 후 종료
## 2-3-2. "Yes" 출력

import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
# stacks = []
# tops = {}

for i in range(M):
    k_i = int(input())
    stack = list(map(int, input().rstrip().split()))
    if sorted(stack, reverse=True) != stack:
        print("No")
        break
else:
    print("Yes")
    # tops[i] = stack.pop() # i번 스택의 맨 위에 있는 교과서의 번호
    # stacks.append(stack)

# indexes = {m + 1:list(tops.values()).index(m + 1) for m in range(M)} # m번 교과서가 존재하는 스택의 인덱스

# for i in range(1, N + 1):
#     print(f"i = {i},", indexes)
#     print("stacks =", stacks)
#     print("tops =", tops)
#     print("=" * 30)
#     if i in tops.values(): # 다음 번호가 어떤 스택의 맨 위에 있을 경우
#         idx = indexes[i] # 다음 번호가 존재하는 스택의 인덱스
#         if stacks[idx]:
#             tops[idx] = stacks[idx].pop() # 해당 스택의 다음 번호를 스택 맨 위로 올림
#             indexes[tops[idx]] = idx # 해당 번호가 존재하는 인덱스를 딕셔너리에 저장
#     else:
#         print("No")
#         break
# else:
#     print("Yes")
