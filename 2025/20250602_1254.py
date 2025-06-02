# 1254: 팰린드롬 만들기
# 알고리즘 분류: 문자열/브루트포스 알고리즘

# 1. 문자열 S 입력(길이는 최대 50, 알파벳 소문자로만 구성됨)
# 2. i번째 이후의 문자열과 그것을 뒤집었을 때가 같은 지 확인
# 2-1. 같을 경우 S의 길이에 i를 더해서 출력

S = input()
length = len(S)

for i in range(length):
    if S[i:] == S[i:][::-1]:
        print(length + i)
        break
