# 26576: Date
# 특이사항: 다국어(영어)
# 출처: PLU High School Programming Contest PLU 2020 Novice 4번
# 알고리즘 분류

# 1. 입력받을 줄의 개수 n 입력
# 2. n줄에 걸쳐 월 일, 년 순서로 문자열 입력(년도는 1에서 300,000,000 사이의 정수)
# 3. 문자열을 각각 스페이스바 그리고 쉼표에 대해 split
# 4. 월을 뜻하는 단어에 대한 딕셔너리에서 숫자 호출
# 5. 일을 뜻하는 숫자가 두 자리가 되도록 왼쪽에 0을 붙임
# 6. 년을 뜻하는 숫자의 맨 끝 두자리만 추출(단, 길이가 1이면 왼쪽에 0을 붙임)
# [보충설명] 4, 5, 6 중 어느 한 단계에서라도 올바른 날짜가 입력되지 않은 경우 Invalid 출력 후 종료
# 7. 4, 5, 6에서 추출 및 변환된 숫자를 정해진 포맷에 맞게 출력

import sys
input = sys.stdin.readline

n = int(input())
month_dict = {"January": 1, "February": 2, "March": 3, "April": 4,
              "May": 5, "June": 6, "July": 7, "August": 8,
              "September": 9, "October": 10, "November": 11, "December": 12}


def transform(string):
    month, day, year = string.split()
    ans = []
    day = day[:-1]  # 쉼표 제거

    # 월 처리
    if month not in month_dict:
        return "Invalid"
    else:
        month = month_dict[month]
        ans.append(str(month).zfill(2))

    # 일 처리
    if int(day) < 1 or int(day) > 31:
        return "Invalid"
    else:
        day = day.zfill(2)
        ans.append(day)

    # 연도 처리
    if len(year) >= 2:
        ans.append(year[-2:])
    else:
        ans.append(year.zfill(2))
    return '/'.join(ans)


for _ in range(n):
    string = input().rstrip()
    print(transform(string))
