# 18406: 럭키 스트레이트
# 알고리즘 분류: 구현/문자열

# 1. 점수 N 입력 (10 ≤ N ≤ 99,999,999, N의 자릿수는 짝수)
# 2. N의 자릿수 측정 후 변수 length에 저장
# 3. [:length // 2]와 [length // 2:]의 슬라이스를 취해 각 슬라이스의 자릿수의 합을 구함
# 4. 두 합이 동일하면 "LUCKY", 다르면 "READY" 출력

N = input()
length = len(N)
slice1, slice2 = N[:length // 2], N[length // 2:]

sum1, sum2 = 0, 0
for i in range(length // 2):
    sum1 += int(slice1[i])
    sum2 += int(slice2[i])

if sum1 == sum2:
    print("LUCKY")
else:
    print("READY")
