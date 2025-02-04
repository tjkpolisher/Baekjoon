# 25908: 수열의 합
# 출처: 2022 성균관대학교(SKKU) 프로그래밍 대회 in 소프트의 밤 E번
# 알고리즘 분류: 수학/정수론

# 1. 양의 정수 S, T 입력 (1 ≤ S ≤ T ≤ 10^7)
# 2. 1부터 n까지의 약수 등장 횟수를 계산하는 함수 정의
# 3. 함수를 이용해 T까지의 합과 S-1까지의 합을 계산 후 빼서 출력

S, T = map(int, input().split())


def summation(n):
    ans = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            ans += n // i
        else:
            ans -= n // i
    return ans


print(summation(T) - summation(S - 1))
