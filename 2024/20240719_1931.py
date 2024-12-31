# 1931: 회의실 배정
# 알고리즘 분류: 그리디 알고리즘/정렬

# 1. 회의의 수 N 입력 (1 ≤ N ≤ 100,000)
# 2. N줄에 걸쳐 회의의 시작시간과 끝나는 시간 입력 (0 이상 2^31 - 1 이하)
# 3. 시작 시간과 끝 시간을 입력한 배열을 끝 시간/시작 시간을 기준으로 오름차순 정렬
# 4. 배열을 순회하면서 해당 원소의 시작 시간이 현재 끝 시간보다 크거나 같으면 정답에 1 추가
# 5. 정답 출력

import sys
input = sys.stdin.readline

N = int(input().rstrip())
time_table = []
for i in range(N):
    t1, t2 = map(int, input().rstrip().split())
    time_table.append([t1, t2])

time_table.sort(key=lambda x: (x[1], x[0]))

ans = 0
end_time = 0
for i, j in time_table:
    if end_time <= i:
        ans += 1
        end_time = j
print(ans)
