# 2018: 수들의 합 5
# 특이사항: 다국어(영어)(한국어 번역)
# 출처: USACO March 2023 Contest Orange 2번
# 알고리즘 분류: 수학/두 포인터

# 1. 정수 N 입력 (1 ≤ N ≤ 10,000,000)
# 2. 1이나 2일 경우 예외적으로 1 출력 후 종료
# 3. 총합을 변수 total = 1로 초기화
# 4. start부터 end까지의 합을 저장 후 N과 비교
# 4-1. N보다 작으면 end에서 1을 뺌
# 4-2. N보다 크면 start에 1을 더함
# 4-3. N과 같으면 cnt에 1을 더하고 end에 1을 더함
# 5. end가 N의 절반을 초과할 때까지 위 과정을 반복
# 6. cnt 출력

N = int(input())

if N == 1 or N == 2:
    print(1)
else:
    start = 1
    end = 1
    total = 1
    cnt = 1

    while end < N // 2 + 2:
        if total == N:
            cnt += 1
            end += 1
            total += end
        elif total < N:
            end += 1
            total += end
        else:
            total -= start
            start += 1

    print(cnt)
