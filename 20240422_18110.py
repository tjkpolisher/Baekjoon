# 18110: solved.ac
# 출처: 서강대학교 2019 Sogang Programming Contest - Champion A번
# 알고리즘 분류: 수학/구현/정렬

# 1. 난이도 의견의 개수 n 입력 (0 ≤ n ≤ 3 × 10^5)
# 2. n개의 줄에 걸쳐 제출한 난이도 의견 입력 (1 이상 30 이하)
# 3. 전체 난이도의 위아래 15%씩을 제외
# 4. 남겨진 인원들에 대해 평균값 계산 후 반올림
# 5. 최종 난이도 출력

import sys
input = sys.stdin.readline


def new_round(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)


n = int(input().rstrip())
if not n:
    print(0)
else:
    opinion = []
    cut = new_round(n * 0.15)
    for _ in range(n):
        opinion.append(int(input().rstrip()))

    opinion.sort()
    if cut:
        print(new_round(sum(opinion[cut:-cut]) / (n - 2 * cut)))
    else:
        print(new_round(sum(opinion) / (n - 2 * cut)))
