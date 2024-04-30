# 1003: 피보나치 함수

# 1. 테스트 케이스의 개수 T 입력
# 2. 피보나치 함수 생성(단, 0과 1이 호출될 때마다 0의 개수와 1의 개수에 각각 1씩을 더함)
# 3. 메모이제이션 리스트 dp 생성
# 4. 테스트 케이스에 대하여 피보나치 함수 실행
# 5. 0의 횟수와 1의 횟수 출력

T = int(input())
for _ in range(T):
    n = int(input())
    cnt0, cnt1 = 1, 0
    for i in range(n):
        cnt0, cnt1 = cnt1, cnt0 + cnt1
    print(cnt0, cnt1)
