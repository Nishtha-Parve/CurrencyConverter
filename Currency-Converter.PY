# A large set of predefined exchange rates (example rates)
exchange_rates = {
    'USD': {'EUR': 0.93, 'GBP': 0.82, 'INR': 83.09, 'JPY': 150.32, 'AUD': 1.56, 'CAD': 1.36, 'CHF': 0.89, 'CNY': 7.32, 'MXN': 18.08, 'BRL': 5.19},
    'EUR': {'USD': 1.08, 'GBP': 0.88, 'INR': 89.35, 'JPY': 161.64, 'AUD': 1.67, 'CAD': 1.47, 'CHF': 0.96, 'CNY': 7.88, 'MXN': 19.43, 'BRL': 5.58},
    'GBP': {'USD': 1.22, 'EUR': 1.14, 'INR': 101.9, 'JPY': 183.52, 'AUD': 1.89, 'CAD': 1.67, 'CHF': 1.09, 'CNY': 8.97, 'MXN': 22.06, 'BRL': 6.35},
    'INR': {'USD': 0.012, 'EUR': 0.011, 'GBP': 0.0098, 'JPY': 1.8, 'AUD': 0.016, 'CAD': 0.014, 'CHF': 0.011, 'CNY': 0.085, 'MXN': 0.19, 'BRL': 0.051},
    'JPY': {'USD': 0.0067, 'EUR': 0.0062, 'GBP': 0.0055, 'INR': 0.56, 'AUD': 0.0092, 'CAD': 0.0078, 'CHF': 0.0059, 'CNY': 0.049, 'MXN': 0.12, 'BRL': 0.034},
    'AUD': {'USD': 0.64, 'EUR': 0.59, 'GBP': 0.53, 'INR': 53.07, 'JPY': 108.7, 'CAD': 0.89, 'CHF': 0.53, 'CNY': 4.72, 'MXN': 11.74, 'BRL': 3.36},
    'CAD': {'USD': 0.74, 'EUR': 0.68, 'GBP': 0.60, 'INR': 64.85, 'JPY': 128.1, 'AUD': 1.13, 'CHF': 0.60, 'CNY': 5.32, 'MXN': 13.17, 'BRL': 3.77},
    'CHF': {'USD': 1.12, 'EUR': 1.04, 'GBP': 0.92, 'INR': 92.77, 'JPY': 170.4, 'AUD': 1.89, 'CAD': 1.66, 'CNY': 8.83, 'MXN': 22.11, 'BRL': 6.25},
    'CNY': {'USD': 0.14, 'EUR': 0.13, 'GBP': 0.11, 'INR': 11.73, 'JPY': 20.43, 'AUD': 0.21, 'CAD': 0.19, 'CHF': 0.11, 'MXN': 2.59, 'BRL': 0.71},
    'MXN': {'USD': 0.055, 'EUR': 0.051, 'GBP': 0.045, 'INR': 5.8, 'JPY': 8.4, 'AUD': 0.085, 'CAD': 0.076, 'CHF': 0.045, 'CNY': 0.39, 'BRL': 0.27},
    'BRL': {'USD': 0.19, 'EUR': 0.18, 'GBP': 0.16, 'INR': 19.63, 'JPY': 29.4, 'AUD': 0.30, 'CAD': 0.27, 'CHF': 0.16, 'CNY': 1.41, 'MXN': 3.7}
}

def convert_currency(amount, from_currency, to_currency):
    """
    Convert an amount from one currency to another using predefined exchange rates.
    
    :param amount: Amount in the base currency
    :param from_currency: The base currency (e.g., USD)
    :param to_currency: The target currency (e.g., EUR)
    :return: Converted amount in target currency
    """
    
    # Ensure the base currency and target currency are available
    if from_currency not in exchange_rates:
        print(f"Error: {from_currency} is not a valid currency.")
        return None
    if to_currency not in exchange_rates[from_currency]:
        print(f"Error: Conversion rate from {from_currency} to {to_currency} is not available.")
        return None
    
    # Get the exchange rate
    rate = exchange_rates[from_currency][to_currency]
    
    # Convert the amount
    converted_amount = amount * rate
    return converted_amount

def display_supported_currencies():
    """
    Display all the currencies available in the predefined exchange rates dictionary.
    """
    print("Supported Currencies:")
    for currency in exchange_rates:
        print(currency, end=' ')
    print("\n")

def currency_converter():
    """
    Interactive function to prompt the user for the conversion details.
    """
    # Display supported currencies
    display_supported_currencies()
    
    # Get user input
    from_currency = input("Enter the base currency (e.g., USD, EUR, GBP, INR, JPY, AUD, CAD, CNY, MXN, BRL): ").upper()
    to_currency = input("Enter the target currency (e.g., USD, EUR, GBP, INR, JPY, AUD, CAD, CNY, MXN, BRL): ").upper()
    
    # Ensure valid currencies are entered
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        print("Invalid currency entered. Please choose valid currencies from the supported list.")
        return
    
    amount = float(input(f"Enter the amount in {from_currency}: "))
    
    # Convert the currency
    converted_amount = convert_currency(amount, from_currency, to_currency)
    
    if converted_amount is not None:
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
    else:
        print("Conversion could not be completed.")

if __name__ == "__main__":
    # Run the currency converter
    currency_converter()
