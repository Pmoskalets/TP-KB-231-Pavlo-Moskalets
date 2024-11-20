import requests

AVAILABLE_CURRENCIES = ['EUR', 'USD', 'PLN']

def get_user_input():
    """Отримати вибір валюти та кількість від користувача."""
    while True:
        currency = input("Виберіть валюту (EUR, USD, PLN) або вихід (EX): ").upper()
        if currency == "EX":
            print("Програма завершена.")
            exit(0)
        if currency in AVAILABLE_CURRENCIES:
            try:
                amount = float(input("Введіть суму для конвертації: "))
                return currency, amount
            except ValueError:
                print("Помилка: введено некоректне число.\n")
        else:
            print("Помилка: обрана невідома валюта.\n")

def fetch_exchange_rates():
    """Отримати курси валют із API НБУ."""
    try:
        response = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")
        response.raise_for_status()  # Перевірка статусу запиту
        data = response.json()
        rates = {item['cc']: item['rate'] for item in data if item['cc'] in AVAILABLE_CURRENCIES}
        return rates
    except requests.exceptions.RequestException as e:
        print(f"Не вдалося отримати курси валют: {e}")
        exit(1)

def convert_currency(rates, currency, amount):
    """Виконати конвертацію валюти в гривні."""
    if currency in rates:
        result = rates[currency] * amount
        print(f"{amount} {currency} = {result:.2f} UAH")
    else:
        print("Помилка: відсутній курс для обраної валюти.")

def main():
    """Основна логіка програми."""
    print("Конвертація валют в гривні (UAH)")
    print(f"Доступні валюти: {', '.join(AVAILABLE_CURRENCIES)}")
    
    exchange_rates = fetch_exchange_rates()

    while True:
        selected_currency, amount = get_user_input()
        convert_currency(exchange_rates, selected_currency, amount)

if __name__ == "__main__":
    main()
