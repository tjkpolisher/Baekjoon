# 20548: 칠리소스
# 출처: 2020 인하대학교 프로그래밍 경진대회(IUPC) J번
# 알고리즘 분류: 수학/브루트포스 알고리즘

# 1. 캡사이신 함유량 c 입력 (캡사이신 단계는 727,272를 초과하지 않도록 c가 주어짐)
# 2. c보다 작은 7의 거듭제곱들을 계산해 리스트에 저장
# 3. 리스트의 길이만큼 2, 1, 0으로 구성된 계수의 중복순열을 조합(각각 7의 거듭제곱의 계수를 뜻함)
# 4. 7의 거듭제곱과 계수의 곱의 합으로 구성되는 합을 구해 c와 같은지 비교
# 5. c와 같은 경우 리스트의 길이 - 인덱스 - 1을 정답으로 출력

from itertools import product

c = int(input())

sevens = [1]
e = 1
while 7 ** e <= c:
    sevens.append(7 ** e)
    e += 1
sevens = sevens[::-1]

exponents = [2, 1, 0]
combs = list(product(exponents, repeat=len(sevens)))

ans = 0
for idx, comb in enumerate(combs):
    summation = 0
    c_list = list(comb)
    for i in range(len(c_list)):
        summation += sevens[i] * c_list[i]

    if summation == c:
        ans = len(combs) - idx - 1
        break

print(ans)
