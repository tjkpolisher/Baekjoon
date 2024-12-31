# 20546: 기적의 매매법
# 출처: 2020 인하대학교 프로그래밍 경진대회(IUPC) H번
# 알고리즘 분류: 구현/시뮬레이션

# 1. 준현이와 성민이에게 주어진 현금 입력
# 2. 14일간의 주가가 공백을 두고 입력 (입력은 1000 이하의 양의 정수)
# 3. 준현이와 성민이의 전략에 따라 시뮬레이션 실행
# 3-1. 준현: BNP 전략 - 주식을 최대한 많이 매수 후 팔지 않음
# 3-2. 성민: 33 매매법 - 3일 연속 순상승하면 전량 매도, 3일 연속 순하락하면 전량 매수
# 4. 1월 14일이 되었을 때 자산 계산 (현금 + 1월 14일의 주가 * 주식 수)
# 5. 준현이의 자산이 더 크면 "BNP", 성민이의 자산이 더 크면 "TIMING", 같으면 "SAMESAME" 출력

cash_now = int(input())
stocks = list(map(int, input().split()))


def bnp(start, stocks):
    for i in range(14):
        if stocks[i] <= start or i == 13:
            number, cash = divmod(start, stocks[i])
            break
    return cash + stocks[-1] * number


def timing(start, stocks):
    number, cash = 0, start
    for i in range(10):
        if stocks[i] < stocks[i + 1] < stocks[i + 2]:
            # 전량 매도 조건
            cash += number * stocks[i + 3]
            number = 0
        elif stocks[i] > stocks[i + 1] > stocks[i + 2]:
            # 전량 매수 조건
            number_new, cash = divmod(cash, stocks[i + 3])
            number += number_new
    return cash + stocks[-1] * number


asset_bnp = bnp(cash_now, stocks)
asset_timing = timing(cash_now, stocks)
# print(f"{asset_bnp=}, {asset_timing=}")
if asset_bnp == asset_timing:
    print("SAMESAME")
elif asset_bnp > asset_timing:
    print("BNP")
else:
    print("TIMING")
