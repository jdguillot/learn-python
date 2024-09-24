def calculate_split(total_amount: float, number_of_people: int, split_array: list[float], currency: str) -> None:
    if number_of_people < 1:
        raise ValueError('Number of people must be greater than one.')
    if (sum(split_array) > 100):
        raise ValueError('Individual splits must add up to less than 100.')
    if (len(split_array) > number_of_people):
        raise ValueError('You\'ve entered more splits than the number of people.')
    
    print(f'Total expense: {currency}{total_amount:,.2f}')
    print(f'Number of people: {number_of_people}')

    for x in range(number_of_people):
        share_per_person: float = total_amount *  (split_array[x] / 100)
        print(f' Person {x + 1} should pay: {currency}{share_per_person:,.2f}')

def user_validation(message: str, expected_type: type):
    while True:
        value = input(message)
        try:
            if (expected_type == list):
                user_list: list[str] = value.split()
                value = [float(item) for item in user_list] if user_list else []
            else:
                value = expected_type(value)
            return value
        except (ValueError, TypeError):
            print(f'"{value}" is not a valid {expected_type.__name__}. Please try again.')


def main() -> None:
    try:
        total_amount: float = float(user_validation('Enter the total amount of the expense: ', float)) # type: ignore
        number_of_people: int = int(user_validation('Enter the number of people sharing the expense: ', int)) # type: ignore
        split_array: list = user_validation('Enter the split amount for each person seperated by a space (For even split, leave blank): ', list)
        split_sum: float = sum(split_array)
        split_num: float = len(split_array)

        if (split_num < number_of_people ):
            for x in range( number_of_people - split_num ):
             split_array.append(( 100 - split_sum ) / 
                                ( number_of_people - split_num ) )

        calculate_split(total_amount, number_of_people, split_array, currency='$')
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()