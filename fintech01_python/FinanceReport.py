# 재무제표를 객체로 다루기 위한 클래스 정의
class FinanceReport:
    def __init__(self, quarter, revenue, net_income):
        # 생성자: 분기, 매출, 순이익 값을 받아 객체 속성에 저장
        self.quarter = quarter          # 분기 정보
        self.revenue = revenue          # 매출 정보
        self.net_income = net_income    # 순이익

    def show_summary(self):
        # 분기별 매출과 순이익 정보를 출력
        print(f'[{self.quarter}] 매출: {self.revenue:,}원 / 순이익: {self.net_income:,}원')

    def profit_rate(self):
        # 이익률 계산: 순이익 ÷ 매출 × 100 (% 단위)
        if self.revenue == 0:
            return 0
        return round((self.net_income / self.revenue) * 100, 2)


# 객체 생성
q1 = FinanceReport('2024 Q1', 500000000, 120000000)
q2 = FinanceReport('2024 Q2', 620000000, 150000000)
q3 = FinanceReport('2024 Q3', 580000000, 80000000)
q4 = FinanceReport('2024 Q4', 640000000, 180000000)

# 객체 리스트로 저장
reports = [q1, q2, q3, q4]

# ✅전체 분기 요약 출력
for report in reports:
    report.show_summary()       # 각 분기별 요약 정보 출력
    print(f'    이익률: {report.profit_rate()}%')
