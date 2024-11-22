# 20365: 블로그2
# 출처: 인천대학교 INU 코드페스티벌 2020 E번
# 알고리즘 분류: 그리디 알고리즘/문자열

# 1. 색을 칠해야 하는 문제의 수 N 입력 (1 ≤ N ≤ 500,000)
# 2. N개의 문자를 공백없이 입력(R과 B로만 구성됨)
# 3. B와 R의 개수를 저장할 딕셔너리 생성
# 4. 문자열을 처음부터 순회하면서 문자가 바뀔 때마다 현재 문자의 딕셔너리 값에 1을 더함
# 4. 문자열에서 B와 R의 값 중 더 적은 것을 취해 1을 더해 출력

N = int(input())
strings = input()

cnt = {'B': 0, 'R': 0}
cnt[strings[0]] += 1
for i in range(1, N):
    if strings[i] != strings[i - 1]:
        cnt[strings[i]] += 1

print(min(cnt['B'], cnt['R']) + 1)
