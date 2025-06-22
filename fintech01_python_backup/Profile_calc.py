# 거래 이익 계산기 프로그램
# 사용자가 매출(sales)과 비용(cost)을 입력하면 이익(profit)을 계산하고,
# 그 결과에 따라 흑자인지 적자인지를 판별해주는 프로그램입니다.

# 함수 정의: 이익 계산기
def calculate_profit(sales, cost):
    return sales - cost

# 사용자로부터 매출과 비용을 입력받기
# input()은 문자열을 반환하므로 int()로 숫자로 변환
sales = int(input('매출을 입력하세요 (숫자만): '))
cost = int(input('비용을 입력하세요 (숫자만): '))

# 함수 호출하여 이익 계산
profit = calculate_profit(sales, cost)

# 결과 출력
print(f'\n[결과] 이익은 {profit:,}원입니다.')

# 조건문으로 흑자/적자 판단
if profit > 0:
    print('이익 상태입니다. (흑자)')
elif profit < 0:
    print('손실 상태입니다. (적자)')
else:
    print('본전입니다. (0원)')
