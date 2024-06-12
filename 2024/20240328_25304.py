# 25304: 영수증
# 알고리즘 분류: 수학/구현/사칙연산

# 1. 총 금액 X 입력
# 2. 구매한 물건의 종류의 수 N 입력
# 3. N개의 줄에 걸쳐 가격 a와 개수 b 입력
# 4. 입력받는 족족 정답에 a * b를 더하기
# 5. 총합이 X와 동일하면 "Yes", 아니면 "No" 출력

X = int(input())
N = int(input())
ans = 0
for _ in range(N):
    a, b = map(int, input().split())
    ans += a * b
if X == ans:
    print("Yes")
else:
    print("No")
