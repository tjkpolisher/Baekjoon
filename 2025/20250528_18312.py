# 18312: 시각
# 알고리즘 분류: 구현/문자열/브루트포스 알고리즘즘

# 1. 정수 N, K 입력 (0 ≤ N ≤ 23, 0 ≤ K ≤ 9)
# 2. 00시 00분 00초부터 시작해 N시 59분 59초까지 문자열을 구성
# 3. 구성된 문자열에 K가 포함될 경우 카운트에 1을 더함
# 4. 개수 출력

N, K = map(int, input().split())

cnt = 0
for i in range(N + 1):
    for j in range(60):
        for k in range(60):
            ts = [str(i).zfill(2), str(j).zfill(2), str(k).zfill(2)]
            string = ''.join(ts)
            if str(K) in string:
                cnt += 1
print(cnt)
