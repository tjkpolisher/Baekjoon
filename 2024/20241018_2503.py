# 2503: 숫자 야구
# 출처: 한국정보올림피아드시.도지역본선 2008 초등부 3번
# 알고리즘 분류: 구현/브루트포스 알고리즘

# 1. 질문의 개수 N 입력 (1 ≤ N ≤ 20)
# 2. N개의 줄에 걸쳐 민혁이가 질문한 세 자리 수와 스트라이크, 볼의 개수 입력
# 3. 세 자리 숫자를 만들기
# 3-1. 단, 만든 숫자의 세 자리 수가 모두 동일할 경우 continue
# 3-2. 각 자리의 숫자가 세 자리 수의 숫자와 동일하면 스트라이크 카운터에 1을 더함
# 3-3. 숫자는 맞지만 그 숫자가 위치한 자리가 다를 경우 볼 카운터에 1을 더함
# 4. 리스트에 들어있는 조건을 넣고 스트라이크/볼 판정
# 4-1. 스트라이크와 볼 모두 매칭이 될 때만 카운터에 1을 더함
# 5. 현재 만들어진 수에 대해 N회 검증한 후 스트라이크와 볼의 개수가 N가 동일하면 정답에 1 추가
# 6. 정답 출력

N = int(input())
numbers = [list(map(int, input().split())) for _ in range(N)]
answer = 0

# 정답에 맞는 세 자리 수의 자릿수 별로 탐색
for a in range(1, 10):  # 백의 자리
    for b in range(1, 10):  # 십의 자리
        for c in range(1, 10):  # 일의 자리
            cnt = 0

            # 세 자리 수를 정확하게 맞추어 3 스트라이크가 되면 게임 종료
            if a == b or b == c or c == a:
                continue
            for array in numbers:
                check = list(str(array[0]))  # 민혁이가 질문한 세 자리 수
                strike = int(array[1])  # 스트라이크 개수
                ball = int(array[2])  # 볼 개수

                strike_count = 0
                ball_count = 0

                if a == int(check[0]):
                    strike_count += 1
                if b == int(check[1]):
                    strike_count += 1
                if c == int(check[2]):
                    strike_count += 1

                if a == int(check[1]) or a == int(check[2]):
                    ball_count += 1
                if b == int(check[0]) or b == int(check[2]):
                    ball_count += 1
                if c == int(check[0]) or c == int(check[1]):
                    ball_count += 1

                # 스트라이크/볼 매칭 여부 확인
                if strike != strike_count:
                    break
                if ball != ball_count:
                    break

                cnt += 1

            if cnt == N:
                answer += 1

print(answer)
