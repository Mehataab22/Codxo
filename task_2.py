"""This Python code implements a basic currency converter that allows users to convert amounts between different currencies using predefined exchange rates. 
The `get_exchange_rate` function retrieves the exchange rate for a specified currency pair from a hardcoded dictionary. 
The `currency_converter` function interacts with the user to input the source currency, target currency, and the amount to convert. 
It then calculates the converted amount by multiplying the input amount by the retrieved exchange rate and displays the result. 
If the currency pair is not supported, it provides an error message. 
The code effectively facilitates simple currency conversions between USD, EUR, JPY, and INR."""


def get_exchange_rate(from_currency, to_currency, rates):
    return rates.get((from_currency, to_currency))


def currency_converter():
    print("Currency Converter")

    # Define the exchange rates
    rates = {
        ("USD", "EUR"): 0.92,
        ("USD", "JPY"): 110.50,
        ("USD", "INR"): 83.50,
        ("EUR", "USD"): 1.09,
        ("EUR", "JPY"): 120.45,
        ("EUR", "INR"): 91.65,
        ("JPY", "USD"): 0.0090,
        ("JPY", "EUR"): 0.0083,
        ("JPY", "INR"): 0.75,
        ("INR", "USD"): 0.012,
        ("INR", "EUR"): 0.011,
        ("INR", "JPY"): 1.33
    }

    # Get the user input
    from_currency = input("Enter the currency to convert from (e.g., USD, EUR, JPY, INR): ").upper()
    to_currency = input("Enter the currency to convert to (e.g., USD, EUR, JPY, INR): ").upper()
    amount = float(input("Enter the amount to convert: "))

    # Validate the user input
    if from_currency not in [currency[0] for currency in rates.keys()]:
        print("Invalid from currency. Please try again.")
        return
    if to_currency not in [currency[1] for currency in rates.keys()]:
        print("Invalid to currency. Please try again.")
        return

    # Get the exchange rate
    exchange_rate = get_exchange_rate(from_currency, to_currency, rates)

    if exchange_rate is not None:
        # Convert the amount
        converted_amount = amount * exchange_rate
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
    else:
        print("Invalid currency pair or rate not available.")


if __name__ == "__main__":
    currency_converter()

