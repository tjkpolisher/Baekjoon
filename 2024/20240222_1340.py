# 1340: 연도 진행바
# 알고리즘 분류: 구현/문자열/파싱

## 1. 날짜 및 시간 입력
## 2. 올해 1월 1일 00:00로부터 지난 시간 계산
## 3. 지난 시간을 퍼센테이지로 계산해 출력

from datetime import datetime
time_and_date = datetime.strptime(input(),
                                  "%B %d, %Y %H:%M")
year_start = datetime.strptime(f"{time_and_date.year} 01 01 00:00",
                               "%Y %m %d %H:%M")
diff = time_and_date - year_start
diff = diff.days * 24 * 3600 + diff.seconds
if time_and_date.year % 400 == 0 or (time_and_date.year % 4 == 0 and time_and_date.year % 100 != 0):
    answer = diff / 366 / 24 / 3600 * 100
else:
    answer = diff / 365 / 24 / 3600 * 100
print(answer)
