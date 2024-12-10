# 16521: A Symmetrical Pizza
# 특이사항: 다국어(영어)
# 출처: ICPC Latin America Regional Contests 2018 A번
# 알고리즘 분류: 수학/정수론/유클리드 호제법

# 1. 회전대칭의 회전각을 의미하는 유리수 R 입력 (0 < R < 360, 소수점 두 자리까지 입력으로 주어짐)
# 2. (1000 * R + 5) // 10을 계산하여 R을 정수 자료형으로 변환
# 3. R에 1부터 차례대로 곱하면서 36000으로 나누어 떨어지면 cnt를 출력
# 3-1. 그렇지 않을 경우 cnt에 1을 더한 후 2를 반복

R = float(input())
R = (1000 * R + 5) // 10
cnt = 1
while True:
    if R * cnt % 36000 == 0:
        print(cnt)
        break
    cnt += 1
