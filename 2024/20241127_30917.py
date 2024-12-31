# 30917: A + B - 10 (제1편)
# 특이사항: 인터랙티브
# 출처: BOJ Bundle in Math. Vol 1 H번
# 알고리즘 분류: 수학/구현/브루트포스 알고리즘/사칙연산

# 1. 1 이상 9 이하의 범위에서 A의 값을 문제의 양식에 맞게 질문하여 알아냄
# 2. A의 값을 맞춰서 1을 입력받았을 경우, 같은 방식으로 1 이상 9 이하에서 B를 알아냄
# 3. B에 대하여 1을 입력받았을 경우, 즉 정답을 만족할 경우 A + B를 계산하여 '! x'라는 형식으로 출력


def solution():
    for a in range(1, 10):
        # A가 a인지 물어보고 flush를 한다.
        # print에 flush 파라미터를 넣으면 된다.
        print("? A", a, flush=True)

        resp = int(input())

        if resp == 1:
            for b in range(1, 10):
                print("? B", b, flush=True)
                resp2 = int(input())
                if resp2 == 1:
                    return f"! {a + b}"
    return f"! {a + b}"


print(solution())
