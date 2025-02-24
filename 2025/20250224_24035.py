# 24035: Impartial Offerings
# 특이사항: 서브태스크, 다국어(영어)
# 출처: Code Jam to I/O for Women 2021 A번
# 알고리즘 분류: 그리디 알고리즘/정렬

# 1. 테스트 케이스의 개수 T 입력 (1 ≤ T ≤ 100)
# 2. 첫 번째 줄에 다음 애완동물의 날에 데리고 있을 동물의 수 N 입력
# 3. 동물의 크기를 나타내는 S_1, S_2, ..., S_N 입력
# 4. 동물 크기를 오름차순으로 정렬
# 5. 동물 크기 리스트를 순회하면서 사료비 계산
# 5-1. 각 동물에게 쓸 사료비를 1부터 시작하고 총합에 더하기
# 5-2. 사료비가 더 커지면 사료비를 1 증가시키고 총합에 더하기
# 6. 주어진 양식에 맞춰 사료비 총합 출력

import sys
input = sys.stdin.readline

T = int(input())
for idx in range(T):
    N = int(input())
    sizes = list(map(int, input().split()))

    sizes.sort()
    ans = 1
    treat = 1
    for i in range(1, N):
        if sizes[i] > sizes[i - 1]:
            treat += 1
        ans += treat
    print(f"Case #{idx + 1}: {ans}")
