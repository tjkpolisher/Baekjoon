# 1874: 스택 수열

# 1. n 입력 (1 ≤ n ≤ 100,000)
# 2. n개의 줄에 걸쳐 수열을 이룰 정수 입력(중복 없음)
# [보충설명] 나중에 들어올 수록 초항에 가까운 항인 것으로 보임
# 3. [반복문] 1부터 n까지의 수를 오름차순으로 스택에 넣고 뽑으면서 판단
# [보충설명] stack1에서의 push 및 pop 연산만을 operators 리스트에 순서대로 저장
# 3-1. 다음 원소가 수열에 해당하는 수가 될 때까지 push 후 해당 수가 되면 그 전의 수를 pop
# 3-2. 스택을 생성할 수 없을 경우 NO 출력
# 4. 연산자들을 순서대로 출력

count = 1
temp = True
stack = []
op = []

n = int(input())
for i in range(n):
    num = int(input())
    # num이하 숫자까지 스택에 넣기
    while count <= num:
        stack.append(count)
        op.append('+')
        count += 1

    # num이랑 스택 맨 위 숫자가 동일하다면 제거
    if stack[-1] == num:
        stack.pop()
        op.append('-')
    # 스택 수열을 만들 수 없으므로 NO
    else:
        temp = False
        break

# 스택 수열을 만들수 있는지 여부에 따라 출력
if not temp:
    print("NO")
else:
    for i in op:
        print(i)
