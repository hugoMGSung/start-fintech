# 거래 이익 계산기 프로그램 (반복 처리 버전)

# 이익을 계산하는 함수 정의
def calculate_profit(sales, cost):
    return sales - cost

print('거래 이익 계산기 프로그램입니다.')
print('종료하려면 q를 입력하세요.\n')

while True:
    # 사용자 입력 받기
    sales_input = input('매출을 입력하세요 (숫자 또는 q): ').strip()
    if sales_input.lower() in ['q']:
        print('프로그램을 종료합니다.')
        break

    cost_input = input('비용을 입력하세요 (숫자 또는 q): ').strip()
    if cost_input.lower() in ['q']:
        print('프로그램을 종료합니다.')
        break

    # 숫자 여부 확인
    if not sales_input.isdigit() or not cost_input.isdigit():
        print('⚠️ 숫자만 입력해주세요.\n')
        continue

    # 정수형으로 변환
    sales = int(sales_input)
    cost = int(cost_input)

    # 이익 계산
    profit = calculate_profit(sales, cost)

    # 결과 출력
    print(f'\n[결과] 이익은 {profit:,}원입니다.')
    if profit > 0:
        print('이익 상태입니다. (흑자)\n')
    elif profit < 0:
        print('손실 상태입니다. (적자)\n')
    else:
        print('본전입니다. (0원)\n')