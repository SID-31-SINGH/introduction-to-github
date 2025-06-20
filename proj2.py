import requests
import json

# --- Simulated Exchange Rates ---
# In a real application, you would fetch these from a live API.
# Example APIs: Open Exchange Rates (https://openexchangerates.org/), Fixer.io (https://fixer.io/)
# For this demonstration, we'll use a static set of rates against USD.
# All rates are relative to 1 USD.
EXCHANGE_RATES = {
    "USD": 1.0,
    "EUR": 0.92, # 1 USD = 0.92 EUR
    "GBP": 0.79, # 1 USD = 0.79 GBP
    "JPY": 156.91, # 1 USD = 156.91 JPY
    "CAD": 1.37, # 1 USD = 1.37 CAD
    "AUD": 1.50, # 1 USD = 1.50 AUD
    "CHF": 0.89, # 1 USD = 0.89 CHF
    "CNY": 7.26, # 1 USD = 7.26 CNY
    "INR": 83.47, # 1 USD = 83.47 INR
    "BRL": 5.43, # 1 USD = 5.43 BRL
}

# --- API Integration Placeholder (Conceptual) ---
# To use a real API, you would typically do something like this:
# API_KEY = "YOUR_OPENEXCHANGERATES_API_KEY" # Get your API key
# BASE_CURRENCY = "USD" # Or any base currency your API supports
# API_URL = f"https://openexchangerates.org/api/latest.json?app_id={API_KEY}&base={BASE_CURRENCY}"

# def fetch_live_exchange_rates(api_url):
#     try:
#         response = requests.get(api_url)
#         response.raise_for_status() # Raise an HTTPError for bad responses (4xx or 5xx)
#         data = response.json()
#         return data['rates'] # This would be your updated EXCHANGE_RATES dictionary
#     except requests.exceptions.RequestException as e:
#         print(f"Error fetching live exchange rates: {e}")
#         return None

# # You would call this at the start of your application or periodically:
# # live_rates = fetch_live_exchange_rates(API_URL)
# # if live_rates:
# #     EXCHANGE_RATES.update(live_rates) # Update your global rates


def display_available_currencies(rates: dict):
    """
    Prints a list of available currency codes to the user.
    """
    print("\n--- Available Currencies ---")
    # Sort currency codes alphabetically for better readability
    sorted_currencies = sorted(rates.keys())
    for currency_code in sorted_currencies:
        print(f"- {currency_code}")
    print("----------------------------")

def get_user_input():
    """
    Gets amount, source currency, and target currency from the user.
    """
    while True:
        try:
            amount = float(input("\nEnter the amount to convert: "))
            if amount <= 0:
                print("Amount must be a positive number. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid amount. Please enter a numerical value.")

    while True:
        from_currency = input("Convert from currency (e.g., USD, EUR): ").strip().upper()
        if from_currency not in EXCHANGE_RATES:
            print(f"Currency '{from_currency}' not supported. Please choose from the list above.")
            display_available_currencies(EXCHANGE_RATES)
        else:
            break

    while True:
        to_currency = input("Convert to currency (e.g., JPY, GBP): ").strip().upper()
        if to_currency not in EXCHANGE_RATES:
            print(f"Currency '{to_currency}' not supported. Please choose from the list above.")
            display_available_currencies(EXCHANGE_RATES)
        elif to_currency == from_currency:
            print("Source and target currencies cannot be the same. Please choose a different target currency.")
        else:
            break
            
    return amount, from_currency, to_currency

def convert_currency(amount: float, from_currency: str, to_currency: str, rates: dict) -> float | None:
    """
    Converts an amount from one currency to another using the provided exchange rates.
    All rates are assumed to be relative to a common base (e.g., USD in EXCHANGE_RATES).

    Args:
        amount (float): The amount to convert.
        from_currency (str): The source currency code.
        to_currency (str): The target currency code.
        rates (dict): A dictionary of exchange rates relative to a common base currency.

    Returns:
        float | None: The converted amount, or None if conversion is not possible.
    """
    if from_currency not in rates or to_currency not in rates:
        print("One or both currencies are not available for conversion.")
        return None

    try:
        # Convert the 'from_currency' amount to the base currency (USD in our example)
        amount_in_base = amount / rates[from_currency]
        
        # Convert the base currency amount to the 'to_currency'
        converted_amount = amount_in_base * rates[to_currency]
        
        return converted_amount
    except ZeroDivisionError:
        print("Error: Exchange rate for source currency is zero, which is not possible.")
        return None
    except Exception as e:
        print(f"An error occurred during conversion: {e}")
        return None

def main():
    """
    Main function to run the currency converter application.
    """
    print("Welcome to the Simple Currency Converter!")
    
    while True:
        display_available_currencies(EXCHANGE_RATES)
        amount, from_cur, to_cur = get_user_input()

        converted_value = convert_currency(amount, from_cur, to_cur, EXCHANGE_RATES)

        if converted_value is not None:
            print(f"\n{amount:,.2f} {from_cur} is equal to {converted_value:,.2f} {to_cur}")
        
        another_conversion = input("\nDo you want to perform another conversion? (yes/no): ").strip().lower()
        if another_conversion != 'yes':
            print("Thank you for using the Currency Converter. Goodbye!")
            break

if __name__ == "__main__":
    main()