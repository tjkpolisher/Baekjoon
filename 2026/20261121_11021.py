# 11021: A + B - 7
# 알고리즘 분류:

# 1. 테스트 케이스의 개수 T 입력
# 2. 각 줄에 A, B 입력 (0 < A,B < 10)
# 3. 각 테스트 케이스마다 "Case #x: "를 출력한 다음, A+B를 출력
# (테스트 케이스 번호는 1부터 시작)

T = int(input())
for i in range(1, T + 1):
    A, B = map(int, input().split())
    print(f"Case #{i}: {A + B}")
