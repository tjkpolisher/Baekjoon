# 14911: 궁합 쌍 찾기
# 출처: 한양대학교 ERICA 캠퍼스 2017 ERICA Programming Contest League B(초보) C번
# 알고리즘 분류: 자료 구조/브루트포스 알고리즘/정렬/해시를 사용한 집합과 맵

# 1. 빈 칸으로 구분된 정수들 입력(2개 이상, 10개 이하)
# 2. 찾고자 하는 정수 하나 입력
# 3. 리스트 내에 있는 정수들을 오름차순으로 정렬
# 4. 맨 앞 원소부터 시작해 자기 자신 및 자기 자신보다 큰 숫자들과 합을 비교
# 5. 합이 찾고자 하는 정수와 같으면 정답 집합에 해당 조합을 추가하고 집합에 없는 경우 개수에 1을 더함
# 6. 정답 내의 순서쌍을 사전 순으로 정렬 후 출력
# 7. 정답 개수를 출력

numbers = list(map(int, input().split()))
integer = int(input())

numbers.sort()
answer = set()

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == integer:
            answer.add((numbers[i], numbers[j]))

answer = list(answer)
answer.sort()
for pair in answer:
    print(pair[0], pair[1])
print(len(answer))
