def calculate_finances(monthly_income: float, tax_rate: float, currency: str) -> None:
    monthly_tax: float = monthly_income * (tax_rate / 100)
    monthly_net_income: float = monthly_income - monthly_tax
    yearly_salary: float = monthly_income * 12
    yearly_tax: float = monthly_tax * 12
    yearly_net_income: float = yearly_salary - yearly_tax

    print('-------------------------------')
    print(f'Monthly income: {currency}{monthly_income:,.2f}')
    print(f'Tax rate: {tax_rate:,.0f}%')
    print(f'Monthly tax: {currency}{monthly_tax:,.2f}')
    print(f'Monthly net income: {currency}{monthly_net_income:,.2f}')
    print(f'Yearly salary: {currency}{yearly_salary:,.2f}')
    print(f'Yearly tax paid: {currency}{yearly_tax:,.2f}')
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

def main() -> None:
    
    monthly_income: float = user_validation('Enter your monthly salary: ')
    tax_rate: float = user_validation('Enter your tax rate (%): ', min_limit=0, max_limit=100)
    calculate_finances(monthly_income, tax_rate, currency="$")

if __name__ == "__main__":
    main()