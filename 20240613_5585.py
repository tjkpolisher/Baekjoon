# 5585: 거스름돈
# 특이사항: 다국어(일본어)(한국어 번역)
# 출처: Japanese Olympiad in Informatics Qualification Round 2007/2008
# 알고리즘 분류: 그리디 알고리즘

# 1. 타로가 지불할 돈의 액수 입력
# 2. 1000엔에서 액수를 빼기
# 3. 500엔부터 시작해 1엔까지 값을 나눠가면서 몫을 취하고, 나머지를 더 낮은 액수로 나눠가며 반복
# 4. 총 몫의 개수를 더해 출력

price = int(input())
change = 1000 - price
change_list = [500, 100, 50, 10, 5, 1]
answer = 0
for c in change_list:
    n1, n2 = divmod(change, c)
    answer += n1
    change = n2
print(answer)
