USD_TO_RUB = 95.50

def convert_usd_to_rub(amount_usd):
    """
    Перводит доллары в рубли по заданному курсу

    Args:
        amount_usd(int): количество долларов

    Returns:
        float: Количсетво рублей
    """
    return amount_usd * USD_TO_RUB
kolvo_usd = int(input("Введите количество долларов: "))
print(f"{kolvo_usd} долларов = {convert_usd_to_rub(kolvo_usd)} рублей")