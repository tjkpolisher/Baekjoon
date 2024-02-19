# 1308: D-Day
# 특이사항: 연도가 서기 1년부터 시작하므로 strptime을 사용하면 ValueError가 발생할 수 있습니다. 전처리를 미리 하도록 합시다.
# 알고리즘 분류: 구현

## 1. 오늘 날짜 입력
## 2. D-Day 날짜 입력(연도, 월, 일 순서)
## 3-1. 캠프가 천 년 이상 지속된다면 "gg" 출력
## 3-2. 그 외의 경우, x일이 남았다면 "D-"를 출력 후 공백 없이 x 출력

from datetime import datetime
a, b, c = map(int, input().split())
a = f"{a:04d}"
today = datetime.strptime(f"{a} {b} {c}", "%Y %m %d")
a, b, c = map(int, input().split())
a = f"{a:4d}"
dday = datetime.strptime(f"{a} {b} {c}", "%Y %m %d")

if dday.year - today.year > 1000:
    print("gg")
elif dday.year - today.year == 1000 and (dday.month, dday.day) >= (today.month, today.day):
    print("gg")
else:
    x = dday - today
    print(f"D-{x.days}")
