# 14717: 앉았다
# 출처: 충남대학교 생각하는 프로그래밍 대회 B번
# 알고리즘 분류: 수학/구현/조합론

# 1. 영학이의 패를 뜻하는 두 개의 정수 A, B 입력 (1 ≤ A, B ≤ 10)
# 2. A와 B가 동일할 경우 10위 이상에서 족보 계산
# 3. A와 B가 동일하지 않을 경우 10위보다 아래에서 족보 계산
# 4. 계산된 족보를 바탕으로 이길 확률을 소수점 아래 셋째 자리까지 반올림해서 출력

A, B = map(int, input().split())
total = 9 * 17  # 총 경우의 수

if A == B:
    num = total - 10 + A
else:
    score = (A + B) % 10
    num = 0
    for i in range(1, 11):
        for j in range(i + 1, 11):
            if score > (i + j) % 10:
                if i == A and j == B:
                    continue
                elif i == A or j == A or i == B or j == B:
                    num += 2
                else:
                    num += 4

print(f"{num / total:.3f}")
