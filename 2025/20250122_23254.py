# 23254: 나는 기말고사형 인간이야
# 출처: 선린 가을맞이 알고리즘 챌린지 Beginner Division D번
# 알고리즘 분류: 자료 구조/그리디 알고리즘/우선순위 큐

# 1. 정수 N, M 입력 (1 ≤ N,M ≤ 200,000)
# [보충설명] 시험까지 남은 시간은 (24 × N)시간
# 2. 공부를 하지 않아도 받을 수 있는 점수의 목록 a_i M개 입력
# 3. 한 시간 공부할 때마다 올릴 수 있는 점수의 목록 b_i M개 입력
# [보충설명] 1 ≤ a_i,b_i ≤ 100, 반드시 한 시간을 다 채워서 공부해야 b_i만큼 성적이 오름
# [보충설명] 아무리 공부하더라도 최고점인 100점이 넘는 점수를 받을 수는 없음
# 4. b_i 리스트로 최대 힙을 구성한 뒤, 공부할 수 있는 남은 시간과, 최대 점수로 만드는 데 필요한 시간 계산
# 5-1. 남은 시간 동안 공부해서 최대점을 맞을 수 있으면 정답에 더함
# 5-2. 100점이 안 된다면 b_i를 100 - 최대 점수로 변경해 최대 힙에 다시 삽입
# 5-3. 남은 시간 동안 공부해도 최대점을 못 받으면 남은 시간에 b_i를 곱해 a에 더하고 정답에 값을 더함
# 6. 큐에 남아있는 모든 a_i 값을 정답에 더함
# 7. 정답 출력

from heapq import heappush, heappop

N, M = map(int, input().split())  # 시험까지 남은 일수, 시험 볼 과목의 개수
a_list = list(map(int, input().split()))  # 기본 점수
b_list = list(map(int, input().split()))  # 공부할 때마다 오르는 점수

time = 0  # 총 공부 시간
heap = []  # 최대 힙
ans = 0  # 정답

for i in range(M):
    heappush(heap, (-b_list[i], a_list[i]))

while N * 24 > time and heap:
    b, a = heappop(heap)
    if (100 - a) // (-b) < 24 * N - time:
        tmp = a + (-b * ((100 - a) // (-b)))
        if tmp == 100:
            ans += 100
        else:
            heappush(heap, (-(100 - tmp), tmp))
        time += (100 - a) // (-b)
    else:
        ans += a + (N * 24 - time) * (-b)
        time += (N * 24 - time)

for b, a in heap:
    ans += a

print(ans)
