# 1291: 이면수와 임현수
# 알고리즘 분류: 구현/많은 조건 분기

# 1. 분석할 자연수 N 입력 (1 ≤ N ≤ 2,700)
# 2. 이면수 판정 결과를 im 변수에 저장
# 2-1. N이 4보다 작거나 5이면 False를 반환하고 종료
# 2-2. 2-1을 만족한 수 중 각 자릿수의 합이 홀수이면 True 반환, 아니면 False 반환
# 3. 임현수 판정 결과를 ih 변수에 저장
# 3-1. N이 2 또는 4이면 True를 반환하고 종료
# 3-2. N을 소인수분해한 결과 소인수의 개수가 짝수 개면 True를 반환, 아니면 False 반환
# 4. im과 ih 값에 따라 그 결과를 정수 형태로 출력

N = int(input())


def im_yeon_su(N):
    # 이면수 판정 함수
    if N <= 5:
        return False
    N_str = str(N)
    summation = 0
    for i in range(len(N_str)):
        summation += int(N_str[i])
    return True if summation % 2 != 0 else False


def im_hyeon_su(N):
    # 임현수 판정 함수
    if N == 4 or N == 2:
        return True
    if N == 1:
        prime_factors = [1]
    else:
        prime_factors = prime_factorization(N)
    return True if len(prime_factors) % 2 == 0 else False


def prime_factorization(N):
    # 소인수를 리스트 형태로 반환하는 함수
    prime_factors = []
    p = 2
    while p <= N:
        if N % p == 0:
            if p not in prime_factors:
                prime_factors.append(p)
            N //= p
        else:
            p += 1
    return prime_factors


im = im_yeon_su(N)
ih = im_hyeon_su(N)

if im and ih:
    # 이면수이면서 임현수일 경우
    print(4)
elif im and not ih:
    # 이면수이지만 임현수가 아닐 경우
    print(1)
elif not im and ih:
    # 임현수이지만 이면수가 아닐 경우
    print(2)
else:
    # 둘 다 아닌, 즉 성경수일 경우
    print(3)
