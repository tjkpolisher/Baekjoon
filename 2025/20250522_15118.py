# 15118: Halfway
# 출처: 2017 Southeast USA Reginoal Programming Contest Division 2 C번
# 알고리즘 분류: 수학/이분 탐색/매개 변수 탐색

# 1. 정수 n 입력 (2 ≤ n ≤ 10^9)
# 2. 중간값을 1부터 n까지의 총합으로 우선 설정
# 3. 왼쪽과 오른쪽 값을 각각 1, n-1로 설정
# 4. 매개변수 탐색을 실시해 mid * n - (mid * (mid + 1)) // 2를 계산해 비교
# 5. 비교값이 목표값 이상이면 오른쪽으로 중간값 - 1로, 그렇지 않으면 왼쪽으로 중간값 + 1로 설정
# 6. 정답 출력

n = int(input())


def solve(n):
    total = (n * (n - 1)) // 2
    target = (total + 1) // 2

    left, right = 1, n - 1
    ans = n - 1

    while left <= right:
        mid = (left + right) // 2
        comparisons = mid * n - (mid * (mid + 1)) // 2

        if comparisons >= target:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    return ans


print(solve(n))
