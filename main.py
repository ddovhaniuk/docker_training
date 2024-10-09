import requests

def get_crypto_price(crypto="bitcoin", currency="usd"):
    """
    Функція для отримання поточної ціни криптовалюти.
    Використовує публічне API CoinGecko.

    :param crypto: Назва криптовалюти (за замовчуванням 'bitcoin').
    :param currency: Валюта для відображення ціни (за замовчуванням 'usd').
    :return: Поточна ціна криптовалюти.
    """
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies={currency}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        price = data[crypto][currency]
        return price
    else:
        return None

def main():
    crypto = input("Введіть назву криптовалюти (наприклад, 'bitcoin', 'ethereum'): ").lower()
    currency = input("Введіть валюту для відображення ціни (наприклад, 'usd', 'eur'): ").lower()

    price = get_crypto_price(crypto, currency)

    if price:
        print(f"Поточна ціна {crypto.capitalize()} в {currency.upper()}: {price}")
    else:
        print("Не вдалося отримати ціну криптовалюти. Перевірте введені дані.")

if __name__ == "__main__":
    main()
