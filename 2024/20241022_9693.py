# 9693: 시파르 (원제: Sifar, 말레이시아어로 0을 뜻함.)
# 특이사항: 다국어(영어)(한국어 번역)
# 출처: ICPC Malaysia Al-Khawarizmi National Programming Contest 2013 A번
# 알고리즘 분류: 수학/정수론

# 0. 출력 양식에 들어갈 카운터를 1로 초기화
# 1. N 입력(5 ≤ N ≤ 10^6) (마지막 입력에는 0이 주어짐)
# 2. N을 5로 나눈 몫이 M의 최대값
# 3. 5의 거듭제곱으로 나누었을 때의 몫을 더해줌
# 4. 주어진 양식에 맞게 정답 출력 후 카운터에 1을 더함

cnt = 1
while True:
    N = int(input())
    if not N:
        break
    M = 0
    i = 1
    while 5 ** i <= N:
        M += N // (5 ** i)
        i += 1

    print(f"Case #{cnt}: {M}")
    cnt += 1
