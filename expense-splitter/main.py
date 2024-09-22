def calculate_split(total_amount: float, number_of_people: int, split_array: list, currency: str) -> None:
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

def user_validation(message: str, val_type: str = 'str'):
    while True:
        value = input(message)
        try:
            if (val_type == 'int'):
                value = int(value)
                return value
            elif (val_type == 'float'):
                value = float(value)
                return value
            elif (val_type == 'float_list'):
                user_list: list = value.split()
                split_array: list[float] = [float(item) for item in user_list]
                return split_array
            else:
                return value
        except ValueError as e:
            print(f'"{value}" is not a valid input. Please enter a valid value.')


def main() -> None:
    try:
        total_amount: float = float(user_validation('Enter the total amount of the expense: ', 'float'))
        number_of_people: int = int(user_validation('Enter the number of people sharing the expense: ', 'int'))
        split_array: list = user_validation('Enter the split amount for each person seperated by a space (For even split, leave blank): ','float_list')
        # user_list: list = split_input.split()
        # split_array: list = [int(item) for item in user_list]
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