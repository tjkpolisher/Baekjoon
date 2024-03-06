# 5576: 콘테스트
# 특이사항: 다국어(일본어)(한국어 번역)
# 알고리즘 분류: 구현/정렬

# 1. [반복문]1~10번째 줄에 걸쳐 W 대학의 각 참가자의 점수 입력
# 2. [반복문]11~20번째 줄에 걸쳐 K 대학의 각 참가자의 점수 입력
# 3. 각 대학에 대하여, 득점이 높은 순으로 3명의 점수를 합산하여 출력

w = []
k = []
for _ in range(10):
    w.append(int(input()))

for _ in range(10):
    k.append(int(input()))

w.sort(reverse=True)
k.sort(reverse=True)

print(sum(w[:3]), sum(k[:3]))
