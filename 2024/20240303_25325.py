# 25325: 학생 인기도 측정
# 알고리즘 분류: 자료 구조/문자열/정렬/해시를 사용한 집합과 맵/트리를 사용한 집합과 맵

# 1. 학생 수 n 입력
# 2. n명의 학생 이름 문자열 A 입력
# 3. [반복문] n개의 줄에 걸쳐 한 줄에 한 학생의 정보 입력
# 3-1. 문자열이 두 단어로 쪼개질 경우 두 번째 단어를 키로 갖는 딕셔너리의 값을 1 올림
# 3-2. 문자열이 한 단어로만 구성될 경우 패스
# 4. 입력이 끝나면 인기도가 높은 학생부터 출력(인기도 같을 경우 학생 이름 기준 오름차순으로)

n = int(input())
names = list(input().split())
d = {name: 0 for name in names}

for _ in range(n):
    like_name = list(input().split())
    for n in like_name:
        d[n] += 1

for name, value in sorted(d.items(), key=lambda item: item[1], reverse=True):
    print(name, value)
