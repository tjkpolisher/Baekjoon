# 30803: 수도꼭지
# 특이사항: 다국어(영어)(한국어 번역)
# 출처: solved.ac Grand Arena #3 Division 2 B번
# 알고리즘 분류: 구현/시뮬레이션

# 1. 수도꼭지의 수 N 입력 (1 ≤ N ≤ 200,000)
# 2. 수도꼭지에서 나오는 물의 양 A_1, A_2, ..., A_N 입력 (1 ≤ A_i ≤ 10^9)
# 3. 조작 횟수 Q 입력 (1 ≤ Q ≤ 200,000)
# 4. Q개의 줄에 걸쳐 조작이 한 줄에 하나씩 입력
# 4-1. 1, i, x가 입력될 경우 i번째 수도꼭지의 나사를 돌려 1분에 x리터의 물을 내보냄
# 4-2. 2, i가 입력될 경우 i번째 수도꼭지의 버튼을 눌러 열린 수도꼭지는 잠그고, 잠겨있으면 열기.
# 5. 아무 조작도 하지 않았을 때 1분 동안 탱크에 담기는 물의 양 출력
# 6. i개의 줄에 걸쳐 i번째 조작까지 끝낸 이후에 1분 동안 탱크에 담기는 물의 양 출력

import sys
input = sys.stdin.readline

N = int(input())
A_list = list(map(int, input().split()))
A = {i + 1: A_list[i] for i in range(N)}  # 수도꼭지 번호는 1부터 시작
toggled = {i + 1: 0 for i in range(N)}  # 토글 시 원래 유량을 저장할 딕셔너리
Q = int(input())

ans = sum(A_list)   # 아무 조작도 하지 않았을 때 분당 탱크에 담기는 물의 양
print(ans)
for _ in range(Q):
    control = input().rstrip()
    if control.startswith('1'):
        n, i, x = control.split()
        i, x = int(i), int(x)
        if A[i]:
            # 수도꼭지가 열려 있는 경우
            ans += (x - A[i])
            A[i] = x
        else:
            # 수도꼭지가 잠겨 있는 경우
            toggled[i] = x
    else:
        n, i = control.split()
        i = int(i)
        if A[i]:
            # 수도꼭지가 열려 있는 경우
            toggled[i] = A[i]
            ans -= A[i]
            A[i] = 0
        else:
            # 수도꼭지가 잠겨 있는 경우
            A[i] = toggled[i]
            ans += A[i]
            toggled[i] = 0
    print(ans)
