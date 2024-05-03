# 1065: 한수
# 알고리즘 분류: 수학/브루트포스 알고리즘

# 1. 1,000 이하의 자연수 N 입력
# 2. 각 자리수 별로 순회하며 등차수열을 이루는지 체크
# 3. 1 이상 N 이하의 한수의 개수 출력

N = int(input())
if N < 100:
    cnt = N  # 한 자릿수와 두 자리 수는 반드시 등차수열을 이룸
else:
    cnt = 99
    for i in range(100, N + 1):
        num = str(i)
        d = int(num[1]) - int(num[0])  # 공차
        for j in range(1, len(num) - 1):
            if d != int(num[j + 1]) - int(num[j]):
                break
        # 모든 자릿수에서 공차가 동일하면 한수이므로 cnt에 1을 더함
        else:
            cnt += 1

print(cnt)
