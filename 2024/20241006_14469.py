# 14469: 소가 길을 건너간 이유 3
# 특이사항: 다국어(영어)(한국어 번역)
# 출처: USA Computing Olympiad 2017 February Contest Bronze 3번
# 알고리즘 분류: 그리디 알고리즘/정렬

# 1. N 입력 (N ≤ 100인 양의 정수)
# 2. N줄에 걸쳐 소의 도착 시간과 검문 시간 입력(두 종류의 시간은 1,000,000 이하의 양의 정수)
# 2-1. 입력받은 시간들을 소의 도착 시간을 기준으로 정렬
# 3. 현재까지의 시간 + 도착 시간 + 검문 시간을 다음 소의 도착 시간과 비교
# 3-1. 같거나 크면 현재까지의 시간을 다음 소의 도착 시간으로 바꾸고 검문 시간을 더함
# 3-2. 작으면 현재까지의 시간 + 도착 시간 + 검문 시간 이후에 다음 소의 검문 시간을 더함
# 4. 경과 시간 출력

N = int(input())
t = 0
times = []
for _ in range(N):
    times.append(list(map(int, input().split())))

times.sort(key=lambda x: x[0])
for i in range(N):
    t_arrive, t_test = times[i]
    if t <= t_arrive:
        t = t_arrive + t_test
    else:
        t += t_test

print(t)
