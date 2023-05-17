from forex_python.converter import CurrencyRates
from forex_python.converter import CurrencyCodes


def print_menu():
    print("*" * 50)
    print("*" + " " * 48 + "*")
    print("*" + " " * 48 + "*")

    print("*" + "Welcome to Currency Exchange Rate Program".center(48) + "*")
    # Menu 1
    print("*" + "1. Get currency rates".center(48) + "*")
    print("*" + "2. Convert currency rate".center(48) + "*")
    print("*" + "Press Q or q to exit".center(48) + "*")

    print("*" + " " * 48 + "*")
    print("*" * 50)

    try:
        input_menu = input("Select menu: >> ")
        return input_menu
    except:
        print(">> Entered menu could not be found. Please enter menu again <<")
        return 'q'


def get_currency_rate(source_currency):
    c = CurrencyRates()
    rate_result = c.get_rates(source_currency)
    return rate_result


def convert_currency_rate(source_currency, dest_currency, amount):
    c = CurrencyRates()
    rate_result = c.convert(source_currency, dest_currency, amount)
    return rate_result


def access_menu(user_selected_menu):
    if user_selected_menu == '1':
        print("\n\n" + "<" * 10 + "Currency Rate".center(30) + ">" * 10)
        try:
            currency_unit = input(">" * 5 + " Please enter currency unit: >> ").upper()
            currency_list = get_currency_rate(currency_unit)
            c = CurrencyCodes()
            for key, value in currency_list.items():
                print(">>>  " + key + " (" + c.get_symbol(key) + ")" + (format(value, '.4f')))
        except:
            message_something_went_wrong()
        finally:
            return question_continue()
    elif user_selected_menu == '2':
        print("\n\n" + "<" * 10 + "Currency Rate Converter".center(30) + ">" * 10)
        try:
            source_currency_unit: str = input(">" * 5 + " Enter source currency unit: >> ").upper()
            des_currency_unit: str = input(">" * 5 + " Enter destination currency unit: >> ").upper()
            source_amount = float(input(">" * 5 + "Enter source currency amount : >> "))
            converted_result = convert_currency_rate(source_currency_unit, des_currency_unit, source_amount)
            print("v" * 50)
            c = CurrencyCodes()
            print(c.get_symbol(source_currency_unit) + format(source_amount, ".2f") + " = " + c.get_symbol(
                des_currency_unit) + format(converted_result, '.2f'))
            print("^" * 50)
        except:
            message_something_went_wrong()
        finally:
            return question_continue()
    elif user_selected_menu == 'q' or user_selected_menu == 'Q':
        print('Quit found.')
    else:
        print(">> Entered menu could not be found. Please enter menu again <<")
        return question_continue()


def question_continue():
    answer = input("\n\nWould you like to continue? Y=Yes, N=No: >> ")
    return answer == 'Y' or answer == 'y'


def goodbye():
    print("\n")
    print("Thank you. See you again.".center(50))
    print("\n")


def message_something_went_wrong():
    print("Something went wrong! Please try again")


# Core Program
running = True

while running:
    selected_menu = print_menu()

    if selected_menu == 'q' or selected_menu == 'Q':
        running = False

    running = access_menu(selected_menu)

goodbye()
