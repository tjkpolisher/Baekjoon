# 1769: 3의 배수
# 알고리즘 분류: 수학/구현/문자열

# 1. 자연수 X 입력
# 2. 한 자리 숫자가 될 때까지 각 자릿수를 더하고, 더할 때마다 횟수에 1을 더함
# 3. 더한 횟수와 3의 배수인지의 여부 출력

X = input()
cnt = 0
while int(X) >= 10:
    X = sum([int(i) for i in X])
    X = str(X)
    cnt += 1

if int(X) % 3 == 0:
    answer = "YES"
else:
    answer = "NO"

print(cnt)
print(answer)
