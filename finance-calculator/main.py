def calculate_finances(monthly_income: float, tax_rate: float, all_expenses: float, currency: str) -> None:
    monthly_tax: float = monthly_income * (tax_rate / 100)
    monthly_net_income: float = monthly_income - monthly_tax
    yearly_salary: float = monthly_income * 12
    yearly_tax: float = monthly_tax * 12
    yearly_expenses: float = all_expenses * 12
    yearly_net_income: float = yearly_salary - yearly_tax - yearly_expenses

    print('-------------------------------')
    print(f'Monthly income: {currency}{monthly_income:,.2f}')
    print(f'Tax rate: {tax_rate:,.0f}%')
    print(f'Monthly tax: {currency}{monthly_tax:,.2f}')
    print(f'Monthly expenses: {currency}{all_expenses:,.2f}')
    print(f'Monthly net income: {currency}{monthly_net_income:,.2f}')
    print(f'Yearly salary: {currency}{yearly_salary:,.2f}')
    print(f'Yearly tax paid: {currency}{yearly_tax:,.2f}')
    print(f'Yearly expenses paid: {currency}{yearly_expenses:,.2f}')
    print(f'Yearly net income: {currency}{yearly_net_income:,.2f}')
    print('-------------------------------')

def user_validation(message:str, min_limit = float('-inf'), max_limit = float('inf')) -> float:
    while True:
        try:
            user_input: str = input(message)
            float_input: float = float(user_input)
            if (check_limits(float_input, min_limit, max_limit)):
                return float_input
            else:
                continue
        except Exception:
            print(f'"{user_input}" is not a valid number. Please enter a valid number.')

def check_limits(input:float, min_limit = float('-inf'), max_limit = float('inf')) -> bool:
    if (input >= min_limit and input <= max_limit):
        return True
    else:
        print(f'"{input}" is not between {min_limit} and {max_limit}. Please enter a valid number.')
        return False

def main() -> None:
    
    monthly_income: float = user_validation('Enter your monthly salary: ', min_limit=0)
    tax_rate: float = user_validation('Enter your tax rate (%): ', min_limit=0, max_limit=100)
    mortgage_expens: float = user_validation('Enter your monthly mortgage expense: ', min_limit=0)
    food_expense: float = user_validation('Enter your monthly food expense: ', min_limit=0)
    additional_expense: float = user_validation('Enter any additional expenses: ')

    all_expenses: float = mortgage_expens + food_expense + additional_expense

    calculate_finances(monthly_income, tax_rate, all_expenses, currency="$")

if __name__ == "__main__":
    main()