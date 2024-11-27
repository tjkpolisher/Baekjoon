# 30924: A + B - 10 (제2편)
# 특이사항: 인터랙티브
# 출처: BOJ Bundle in Math. Vol 1 O번
# 알고리즘 분류: 수학/사칙연산/무작위화

# 1. 1 이상 10000 이하의 범위를 셔플한 후, A의 값을 문제의 양식에 맞게 질문하여 알아냄
# 2. A의 값을 맞춰서 1을 입력받았을 경우, 같은 방식으로 1 이상 9 이하에서 B를 알아냄
# 3. B에 대하여 1을 입력받았을 경우, 즉 정답을 만족할 경우 A + B를 계산하여 '! x'라는 형식으로 출력

from random import shuffle


def solution():
    num_li = list(range(1, 10001))
    shuffle(num_li)
    for a in num_li:
        print("? A", a, flush=True)
        resp = int(input())
        if resp:
            break

    for b in num_li:
        print("? B", b, flush=True)
        resp2 = int(input())
        if resp2:
            return f"! {a + b}"
    return f"! {a + b}"


print(solution())
