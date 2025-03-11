# 9953: Paula's search
# 특이사항: 다국어(영어)
# 출처: NZPC 2007 G번
# 알고리즘 분류: 이분 탐색

# 1. 매 입력마다 방문하고자 하는 가게 번호 입력(가게 번호는 1 이상 100 이하)
# 1-1. 0이 입력되면 프로그램 종료
# 2. 50번부터 시작해 이진 탐색 시작(50번 가게는 짝수 측 길가의 정중앙에 위치)
# 2-1. 반대쪽 길로 건너가야 할 경우
# 2-1-1. 짝수에서 홀수로 넘어갈 때 현재 위치를 홀수 쪽 길의 중점으로 세팅 후 1을 빼기
# 2-1-2. 홀수에서 짝수로 넘어갈 때 현재 위치를 짝수 쪽 길의 중점으로 세팅 후 1을 빼기
# 2-2. 같은 길에서 이동할 경우 일반적인 이진 탐색 알고리즘을 따르기
# 3. 마지막 가게에 방문했다는 것을 고려하기 위해 횟수에 1을 더하고 출력

import sys
input = sys.stdin.readline

while True:
    N = int(input())
    if N == 0:
        break

    current = 50  # 시작 위치는 항상 50번 가게
    cnt = 0  # 파울라가 맞는 옷을 찾을 때까지 방문한 가게의 수
    odd_start, odd_end = 1, 99
    even_start, even_end = 2, 100

    while current != N:
        cnt += 1

        # 길 반대편으로 이동해야 할 경우
        if N % 2 != current % 2:
            if current % 2 == 0:  # 짝수에서 홀수로
                current = (odd_start + odd_end) // 2
                if current % 2 == 0:
                    current -= 1
            else:  # 홀수에서 짝수로
                current = (even_start + even_end) // 2
                if current % 2 == 1:
                    current -= 1
            continue

        # 같은 쪽에서의 이동
        if current % 2 == 0:  # 짝수 쪽 길
            if N < current:
                even_end = current - 2
            else:
                even_start = current + 2
            current = (even_start + even_end) // 2
            if current % 2 == 1:
                current -= 1
        else:  # 홀수 쪽 길
            if N < current:
                odd_end = current - 2
            else:
                odd_start = current + 2
            current = (odd_start + odd_end) // 2
            if current % 2 == 0:
                current -= 1

    print(cnt + 1)
