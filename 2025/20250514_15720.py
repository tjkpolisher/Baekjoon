# 15720: 카우버거
# 출처: 중앙대학교 CodeRace 2018 2번
# 알고리즘 분류: 수학/구현/그리디 알고리즘/정렬/사칙연산

# 1. 주문한 버거의 개수 B, 사이드 메뉴의 개수 C, 음료의 개수 D 입력
# [보충설명] 1 ≤ B, C, D ≤ 1,000
# 2. 각 버거의 가격 입력
# 3. 각 사이드 메뉴의 가격 입력
# 4. 각 음료의 가격 입력
# [보충설명] 각 메뉴의 가격은 10,000 이하의 100의 배수
# 5. 세트 할인이 되기 전 가격을 구하기 위해 모든 리스트의 합을 더해서 출력
# 6. B, C, D 중 최대값을 n에 저장
# 7. 버거, 사이드메뉴, 음료의 가격을 순서대로 2차원 리스트에 저장.
# 8. 각 행에서 모자란 원소의 개수만큼 0을 저장
# 9. 각 열에 대하여 0이 나오지 않으면 10% 할인 적용 후 정답에 누적
# 10. 계산된 총합 출력

import sys
input = sys.stdin.readline

B, C, D = map(int, input().split())
burgers = list(map(int, input().split()))
sides = list(map(int, input().split()))
beverages = list(map(int, input().split()))

print(sum(burgers) + sum(sides) + sum(beverages))

ans = 0
n = max((B, C, D))
burgers.sort(reverse=True)
sides.sort(reverse=True)
beverages.sort(reverse=True)


def append_none(list_element, n):
    if len(list_element) == n:
        return
    for _ in range(n - len(list_element)):
        list_element.append(0)


append_none(burgers, n)
append_none(sides, n)
append_none(beverages, n)

table = [burgers, sides, beverages]
none_flag = False
for i in range(n):
    tmp = 0
    for j in range(3):
        tmp2 = table[j][i]
        if tmp2 == 0 and not none_flag:
            none_flag = True
        tmp += tmp2
    if none_flag:
        ans += tmp
    else:
        ans += int(tmp * 0.9)

print(ans)
