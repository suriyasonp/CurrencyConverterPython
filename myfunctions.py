import currency


def print_menu():
    print("*" * 50)
    print("*" + " " * 48 + "*")
    print("*" + " " * 48 + "*")

    print("*" + "Welcome to Currency Exchange Rate Program".center(48) + "*")
    # Menu 1
    print("*" + "1. Get available currencies".center(48) + "*")
    print("*" + "2. Convert currency rate (Today)".center(48) + "*")
    print("*" + "3. 7 days trend".center(48) + "*")
    print("*" + "Press Q or q to exit".center(48) + "*")

    print("*" + " " * 48 + "*")
    print("*" * 50)

    try:
        input_menu = input("Select menu: >> ")
        return input_menu
    except:
        print("\n>> Entered menu could not be found. Please enter menu again <<")
        return 'q'


def access_menu(user_selected_menu):
    if user_selected_menu == '1':
        print("\n\n" + "<" * 10 + "Available Currencies".center(30) + ">" * 10)
        try:
            result = currency.get_available_currencies()
            print(result)
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

            if currency.is_currency_available(source_currency_unit) and currency.is_currency_available(
                    des_currency_unit):
                converted_result = currency.convert_currency_rate(source_amount, source_currency_unit,
                                                                  des_currency_unit)
                print("v" * 50)
                print(source_currency_unit + format(source_amount, ".2f") + " = " + des_currency_unit + format(
                    converted_result, '.2f'))
                print("^" * 50)
            else:
                message_something_went_wrong("[ERR] Currency is not correct.")
        except ValueError:
            message_something_went_wrong("[ERR] That was no valid number. Try again...")
        except:
            message_something_went_wrong()
        finally:
            return question_continue()
    elif user_selected_menu == '3':
        print("\n\n" + "<" * 10 + "7 days trend".center(30) + ">" * 10)

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


def message_something_went_wrong(message=""):
    print("Something went wrong! Please try again.\n" + message)
