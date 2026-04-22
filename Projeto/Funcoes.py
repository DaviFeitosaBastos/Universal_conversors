from time import sleep
import locale
import requests


def get_dollar_rate():
    """
    Fetches the current USD to BRL exchange rate using AwesomeAPI.

    Returns:
        float: Current dollar value in BRL.
    """
    try:
        url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return float(data['USDBRL']['bid'])
    except Exception:
        print("Error fetching exchange rate. Using fallback value.")
        return 5.47


def retry_or_return():
    """
    Asks the user if they want to perform another conversion.

    Returns:
        bool: True to continue, False to exit.
    """
    while True:
        yes_options = ['yes', 'y']
        no_options = ['no', 'n']

        try:
            option = input("\nDo you want to convert another value? (y/n): ").lower().strip()

            if option in yes_options:
                return True
            elif option in no_options:
                print("\nReturning...\n")
                return False
            else:
                print("Invalid option. Please type 'y' or 'n'.")
        except ValueError:
            print("Invalid input.")
            sleep(1)


def celsius_to_fahrenheit():
    """
    Converts temperature from Celsius to Fahrenheit.
    """
    while True:
        try:
            celsius = float(input("\nEnter temperature in Celsius: "))
            fahrenheit = (celsius * 9/5) + 32
            sleep(0.5)
            print(f"\n{celsius}°C = {fahrenheit:.2f}°F")
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if not retry_or_return():
            break


def km_to_miles():
    """
    Converts kilometers to miles.
    """
    while True:
        try:
            km = float(input("\nEnter distance in kilometers: "))
            miles = round(km * 0.621371, 2)
            sleep(0.5)
            print(f"\n{km} km = {miles} miles")
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if not retry_or_return():
            break


def brl_to_usd():
    """
    Converts Brazilian Real (BRL) to US Dollar (USD).
    """
    while True:
        try:
            value = input("\nEnter value in BRL: ").replace(',', '.')
            rate = get_dollar_rate()
            brl = float(value)
            usd = brl / rate
            formatted_value = locale.currency(brl, grouping=True)

            sleep(0.5)
            print(f"\n{formatted_value} = ${usd:,.2f} USD (Rate: R$ {rate:.2f})")
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if not retry_or_return():
            break


def minutes_to_hours():
    """
    Converts minutes to hours.
    """
    while True:
        try:
            minutes = float(input("\nEnter minutes: "))
            hours = minutes / 60
            sleep(0.5)
            print(f"\n{minutes} minutes = {hours:.2f} hours")
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if not retry_or_return():
            break
