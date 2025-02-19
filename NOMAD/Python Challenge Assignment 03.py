# Python Challenge Assignment 03

# 👇🏻 YOUR CODE 👇🏻:

# /YOUR CODE

# BLUEPRINT | DONT EDIT


monthly_revenue = 5500000 # 월간매출
monthly_expenses = 2700000 #월간비용
tax_credits = 0.01 #세액 공제율


# 함수
## 연간 매출 계산
def get_yearly_revenue(monthly_revenue):
    year_rev = 12 * monthly_revenue
    return year_rev

## 연간 비용 계산
def get_yearly_expenses(monthly_expenses):
    year_expens = 12 * monthly_expenses
    return year_expens

## 세금 계산
def get_tax_amount(profit):
    if profit > 1000000: 
        tax_amount = 0.25 # 1. tax_credits * 2500 에서 변경 2.profit * tax_credits 
    else:
        tax_amount = 0.15
    
    return tax_amount * profit # 1. return = tax_amount 

## 세액 공제 적용
def apply_tax_credits(tax_amount, tax_credits):
    tax_discount = tax_amount * tax_credits # 1. amount_dicount = tax_amount - (tax_amount * tax_credits) 
    return tax_discount



yearly_revenue = get_yearly_revenue(monthly_revenue)
yearly_expenses = get_yearly_expenses(monthly_expenses)

profit = yearly_revenue - yearly_expenses

tax_amount = get_tax_amount(profit)

final_tax_amount = tax_amount - apply_tax_credits(tax_amount, tax_credits)

print(f"Your tax bill is: ${final_tax_amount}")

# /BLUEPRINT