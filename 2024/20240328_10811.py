# 10811: 바구니 뒤집기
# 알고리즘 분류: 구현/시뮬레이션

# 1. 바구니 번호의 개수 N, 역순으로 만드는 방법의 수 M 입력
# 2. [반복문] M개의 줄에 걸쳐 i와 j 입력
# 2-1. i번째 바구니부터 j번째 바구니까지의 순서를 역순으로 바꾸기
# 3. 가장 왼쪽에 있는 바구니부터 바구니에 적혀있는 순서를 출력

N, M = map(int, input().split())
array = list(range(1, N + 1))
for _ in range(M):
    i, j = map(int, input().split())
    i -= 1
    j -= 1
    if i != 0 and j != N - 1:
        array = array[:i] + array[i:j + 1][::-1] + array[j + 1:]
    elif i == 0:
        array = array[:j + 1][::-1] + array[j + 1:]
    elif j == N - 1:
        array = array[:i] + array[i:][::-1]
print(*array, end=' ')
