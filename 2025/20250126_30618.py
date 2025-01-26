# 30618: donstructive
# 특이사항: 스페셜 저지
# 출처: 서강대학교 2023 Sogang Programming Contest Master B번
# 알고리즘 분류: 해 구성하기

# 1. 구하고자 하는 순열의 길이 N 입력 (1 ≤ N ≤ 200,000)
# 2. 높은 수를 덱의 가운데에 배치(append)
# 3. 다음 수를 번갈아가면서 appendleft, append를 실행
# 4. 완성된 덱을 한 줄에 출력

from collections import deque

N = int(input())
result = deque()

right = True

for i in range(N, 0, -1):
    if right:
        result.append(i)
    else:
        result.appendleft(i)
    right = not right

print(*result)
