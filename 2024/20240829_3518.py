# 3518: 공백왕 빈-칸
# 특이사항: 다국어(영어)(한국어 번역)
# 출처: ICPC Northern Eurasia Finals NEERC 2010 A번
# 알고리즘 분류: 구현/문자열/파싱

# 1. 여러 줄에 걸쳐 문서 입력 (한 단어는 최대 80자, 한 줄에 최대 180자, 한 문서는 최대 1000줄)
# 2. 입력받은 문서 한 줄을 공백을 기준으로 split
# 3. Split한 단어를 단어 리스트에 저장
# 4. 한 줄의 단어들을 순회하며 해당 순서의 단어들 중 최대 길이 저장
# 5. 모든 줄의 입력이 끝났다면 각 인덱스의 단어에 대해 m[j] - len(w)만큼의 공백을 추가
# 6. 형식에 맞게 한 줄씩 출력

li, m = [], []

while True:
    try:
        line = input().rstrip().split()
        li.append(line)
        for i, l in enumerate(line):
            if i < len(m):
                m[i] = max(m[i], len(l))
            else:
                m.append(len(l))
    except EOFError:
        break

for i, l in enumerate(li):
    for j, w in enumerate(l):
        li[i][j] = w + (m[j] - len(w)) * ' '

for l in li:
    print(' '.join(l).rstrip())
