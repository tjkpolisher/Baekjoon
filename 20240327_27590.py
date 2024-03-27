# 27590: Sun and Moon
# 특이사항: 다국어(영어)
# 알고리즘 분류: 구현/브루트포스 알고리즘/시뮬레이션

# 1. 첫 번째 줄에 d_s, y_s 입력
# (각각 몇 년 전에 태양이 일식/월식 위치에 있었는지, 다시 그 위치에 돌아가려면 몇 년이 걸리는지를 나타냄)
# 2. 두 번째 줄에 d_m, y_m 입력
# (각각 몇 년 전에 달이 일식/월식 위치에 있었는지, 다시 그 위치에 돌아가려면 몇 년이 걸리는지를 나타냄)
# (0 ≤ d_s < y_s ≤ 50, 0 ≤ d_m < y_m ≤ 50)
# 3. 두 천체에 대하여 y - d를 계산
# 4. [반복문]공전 주기를 1씩 더해주면서 두 연도가 일치하는 시점까지 계산
# 5. 정답 출력

d_s, y_s = map(int, input().split())
d_m, y_m = map(int, input().split())

sun_year = y_s - d_s
moon_year = y_m - d_m

while sun_year != moon_year:
    if sun_year < moon_year:
        sun_year += y_s
    else:
        moon_year += y_m
print(sun_year)
