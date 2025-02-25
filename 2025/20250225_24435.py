# 24435: 카드 게임
# 특이사항: 다국어(영어)(한국어 번역)
# 알고리즘 분류: 문자열/브루트포스 알고리즘/정렬/백트래킹

# 1. 테스트 케이스의 개수 T 입력 (1 ≤ T ≤ 10)
# 2. 첫 줄에 n 입력 (2 ≤ n ≤ 8)
# 3. 둘째 줄에 밥이 가진 카드에 적힌 숫자를 공백 없이 입력
# 4. 셋재 줄에 앨리스가 가진 카드에 적힌 숫자를 공백 없이 입력
# 5. 밥의 카드를 정배열 및 역배열로 정렬한 뒤 정수로 변환
# 6. 5에서 만든 두 수 중 작은 수를 목표값으로 설정
# 7. 앨리스의 카드를 이용한 순열들을 구성
# 8. 순열의 값들을 join했을 때의 값을 저장
# 9. 순열을 조합한 값이 6의 목표값보다 최초로 커지는 시점에 루프 종료 후 이전 값을 출력

import sys
from itertools import permutations
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    bob = input().rstrip()
    alice = list(input().rstrip())

    target = min(int(bob), int(''.join(list(bob)[::-1])))

    stop_flag = False
    prev_value = None
    for i in range(max(1, n - 2), n + 1):
        perms = sorted(list(permutations(alice, i)))
        # print(f"{perms=}")
        for perm in perms:
            tmp = int(''.join(perm))
            # print(f"{tmp=}")
            if tmp >= target:
                print(prev_value)
                stop_flag = True
                break
            prev_value = tmp

        if stop_flag:
            break
        else:
            prev_value = tmp
    else:
        print(prev_value)
