# 9536: 여우는 어떻게 울지?
# 특이사항: 다국어(영어)(한국어 번역)
# 출처: CERC 2013 B번
# 알고리즘 분류: 자료 구조/문자열/해시를 사용한 집합과 맵/파싱

# 1. 테스트 케이스의 개수 T 입력
# 2. 첫 줄에 단어들로 구성된 문장 입력(단어는 최대 100개, 단어의 길이는 최대 100글자)
# 2-1. 여우를 제외한 동물들의 울음소리 입력 후 별도의 집합에 저장
# 2-2. what does the fox say?가 입력되면 입력 종료
# 3. 전체 소리 중 집합에 없는 원소들만 결과 리스트에 저장
# 4. 결과 리스트를 공백을 기준으로 join하여 출력

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    recorded_sound = input().rstrip().split()
    unique_sounds = set()

    while True:
        line = input().rstrip()
        if line == "what does the fox say?":
            break
        _, _, sound = line.split()
        unique_sounds.add(sound)

    result = [sound for sound in recorded_sound if sound not in unique_sounds]
    print(' '.join(result))
