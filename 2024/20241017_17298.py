# 17298: 오큰수
# 알고리즘 분류: 자료 구조/스택

# 1. 수열 A의 크기 N 입력 (1 ≤ N ≤ 1,000,000)
# 2. A의 원소들을 입력받아 리스트에 저장 (1 ≤ A_i ≤ 1,000,000)
# 3. 오큰수를 저장할 리스트 NGE와 수열의 인덱스를 저장할 스택 선언
# 4. 아래의 단계를 반복하면서 오큰수 판단
# 4-1. 스택이 비어있지 않고 스택의 마지막 원소가 현재 인덱스의 원소보다 작을 경우, NGE에 저장
# 4-2. NGE에 저장했는지의 여부와 관계없이 해당 인덱스를 스택에 저장
# 4-3. 반복문이 종료되면 스택에 남아있는 인덱스에 해당하는 NGE의 원소들을 -1로 변경
# 5. NGE의 원소들을 한 줄에 출력

N = int(input())
A = list(map(int, input().split()))
NGE = [0] * N
stack = []

for i in range(N):
    while stack and A[stack[-1]] < A[i]:
        NGE[stack.pop()] = A[i]
    stack.append(i)

while stack:
    NGE[stack.pop()] = -1

print(*NGE)
