# Currency Converter - Frankfurter API

import requests

try:
    # User Input
    amount = float(input("Enter amount: "))
    from_currency = input("Enter from currency (USD, EUR, INR): ").upper()
    to_currency = input("Enter to currency (USD, EUR, INR): ").upper()

    # API URL
    url = f"https://api.frankfurter.dev/v2/rate/{from_currency}/{to_currency}"

    # API Request
    response = requests.get(url)
    response.raise_for_status()

    # Convert response to JSON
    data = response.json()

    # Get exchange rate
    exchange_rate = data["rate"]

    # Mathematical Operation
    converted_amount = amount * exchange_rate

    # Display Result
    print("\n========== CURRENCY CONVERTER ==========")
    print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")

except ValueError:
    print("Error: Please enter a valid amount.")

except requests.exceptions.RequestException:
    print("Error: Unable to connect to the API.")

except KeyError:
    print("Error: Invalid currency code.")

except Exception as e:
    print("Error:", e) 