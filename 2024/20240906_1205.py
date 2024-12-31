# 1205: 등수 구하기
# 알고리즘 분류: 구현

# 1. 점수의 개수 N, 태수의 새로운 점수, 랭킹 리스트에 올라갈 수 있는 점수의 개수 P 입력
# [보충설명] 10 ≤ P ≤ 50, 0 ≤ N ≤ P, 모든 점수는 2,000,000,000 이하의 자연수 또는 0.
# 2. 현재 랭킹 리스트에 있는 점수가 비오름차순으로 입력
# [보충설명] 비오름차순: 단조 감소가 아닌 내림차순, 즉 같은 숫자가 포함될 수 있음.
# [보충설명] 둘째 줄은 N이 0보다 큰 경우에만 주어짐. 이 경우 예외 처리 후 1을 출력.
# 3-1. 태수의 점수가 리스트의 i번째 수보다 작으면 순위에 1을 더하고 다음 인덱스와 비교
# 3-2. i번째 수와 같으면 continue
# 4. 랭킹 리스트의 개수 P를 넘어서면 순위를 -1로 설정
# 5. 순위 출력

N, score_new, P = map(int, input().split())
try:
    score_list = list(map(int, input().split()))

    # 새 점수가 리스트에서 몇 번째에 위치할 지를 계산
    ans = 1
    for score in score_list:
        if score > score_new:
            ans += 1
        elif score == score_new:
            continue
        else:
            break

    # 랭킹 리스트에 들어갈 수 있는 지 확인
    if N < P or (N == P and score_new > score_list[-1]):
        print(ans)
    else:
        print(-1)
except:
    print(1)
