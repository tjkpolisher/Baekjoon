# 25757: 임스와 함께하는 미니게임
# 출처: 제1회 서울과학기술대학교 컴퓨터공학과 알고리즘 대회 C번
# 알고리즘 분류: 자료 구조/문자열/해시를 사용한 집합과 맵

# 1. 플레이 횟수를 나타내는 정수 N과 플레이할 게임의 종류를 나타내는 알파벳 대문자 입력
# [보충설명] 1 ≤ N ≤ 100,000, 게임 종류는 [Y, F, O] 중 한 가지로 각각 2, 3, 4명이서 플레이. 인원이 부족하면 게임 시작 불가.
# 2. N개의 줄에 걸쳐 같이 플레이하고자 하는 사람들의 이름이 문자열로 입력
# [보충설명] 1 ≤ (문자열 길이) ≤ 20, 이름은 숫자 또는 영어 대소문자로 구성
# 3. 이름을 집합에 더하고, 이미 집합에 있는 이름이면 그룹에 포함하지 않음.
# 4. 집합의 길이를 게임 인원 수로 나눈 몫을 출력

import sys
input = sys.stdin.readline

N, game_type = input().rstrip().split()

N = int(N)
game_members = {'Y': 2, 'F': 3, 'O': 4}
n_members = game_members[game_type]
names = set()

for _ in range(N):
    name = input().rstrip()
    names.add(name)

print(len(names) // (n_members - 1))
