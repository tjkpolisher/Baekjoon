# 2057: 팩토리얼 분해
# 알고리즘 분류: 수학/그리디 알고리즘/브루트포스 알고리즘

# 1. 정수 N 입력 (0 ≤ N ≤ 1,000,000,000,000,000,000)
# 2. 0부터 20까지의 팩토리얼을 계산 후 리스트에 저장
# 3. 리스트를 역순으로 순회해 현재까지의 누적합이 N보다 큰지, 작은지, 같은지 판단
# 3-1. 작으면 누적합에 더하기
# 3-2. 같으면 YES 출력 후 종료
# 3-3. 크면 pass
# 4. for 문을 모두 거치고 난 후에도 YES가 출력되지 않으면 NO 출력

N = int(input())
factorial = [1, 1]
for i in range(2, 21):
    factorial.append(factorial[-1] * i)

result = 0
for i in range(20, -1, -1):
    if result + factorial[i] < N:
        result += factorial[i]
    elif result + factorial[i] == N:
        print("YES")
        break
else:
    print("NO")
