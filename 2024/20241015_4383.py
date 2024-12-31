# 4383: 점프는 즐거워
# 특이사항: 다국어(영어)(한국어 번역)
# 출처: Waterloo's local Programming Contests 30 September, 2000 C번
# 알고리즘 분류: 구현

# 1. 각 줄의 첫 수 n이 주어지고, n개의 수가 주어짐
# 1-1. 입력이 없으면 프로그램을 종료
# 2. n을 리스트에서 제외한 후, 리스트의 길이를 비교
# 2-1. 리스트의 길이가 1이면 Jolly를 출력 후 다음 입력을 받아 위의 연산 진행
# 2-2. 2 이상일 경우 아래 단계 진행
# 3. 연속된 두 수의 차의 절대값이 저장된(1 ~ n - 1) 집합 생성
# 4. 앞뒤 원소의 차의 절대값을 비교하고 집합에 있으면 제거
# 4-1. 집합에 없을 경우 Not jolly 출력 후 종료
# 5-1. 연산이 모두 끝난 후 집합의 길이가 n - 1이 아니면 Not jolly 출력
# 5-2. n - 1이면 Jolly 출력

import sys
input = sys.stdin.readline

while True:
    sequence = list(map(int, input().split()))
    if not sequence:
        break
    n = sequence[0]
    sequence.remove(n)

    if len(sequence) == 1:
        print("Jolly")
    else:
        differences = set(range(1, n))  # 연속된 두 수의 차의 절대값을 비교
        for i in range(n - 1):
            diff = abs(sequence[i] - sequence[i + 1])
            if diff not in differences:
                print("Not jolly")
                break
            differences.remove(diff)
        else:
            if not differences:
                print("Jolly")
            else:
                print("Not jolly")
