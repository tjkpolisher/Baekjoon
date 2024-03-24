# 1049: 기타줄
# 알고리즘 분류: 수학/그리디 알고리즘

# 1. 끊어진 기타줄의 개수 N, 기타줄 브랜드의 개수 M 입력
# 2. M개의 줄에 걸쳐 각 브랜드의 패키지 가격과 낱개 가격 입력
# 3. 패키지 당 기타 줄 6개가 들어있으므로 N을 6으로 나눈 몫과 나머지 입력
# 4. 몫 * 패키지 가격 + 나머지 * 낱개 가격 계산
# 5. (몫 + 1) * 패키지 가격 계산
# 6. N * 낱개 가격 계산
# 7. 4, 5, 6에서 구한 값들 중 최소값을 출력

N, M = map(int, input().split())
price_package = []  # 패키지 가격
price_single = []  # 낱개 가격
for _ in range(M):
    p, s = map(int, input().split())
    price_package.append(p)
    price_single.append(s)

price_package.sort()
price_single.sort()
package, single = divmod(N, 6)  # N을 6으로 나눴을 때의 몫과 나머지

p1 = package * price_package[0] + single * price_single[0]
p2 = (package + 1) * price_package[0]
p3 = N * price_single[0]

print(min(min(p1, p2), p3))
