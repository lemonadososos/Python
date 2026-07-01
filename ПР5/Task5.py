CUPURA_5K = 5000
CUPURA_2K = 2000
CUPURA_1K = 1000
CUPURA_5H = 500
CUPURA_2H = 200
CUPURA_1H = 100

def bankomat(dengi):
    """
    Высчитывает количесвто количество выдаваемых купюр

    Arguments:
        dengi(int): количество запрашиваемых денег, кратных 100

    Returns:
        int: количество купюр каждого номинала, которые выдадутся
    """
    dengi_5k = dengi // CUPURA_5K
    dengi -= dengi_5k * CUPURA_5K
    dengi_2k = dengi // CUPURA_2K
    dengi -= dengi_2k * CUPURA_2K
    dengi_1k = dengi // CUPURA_1K
    dengi -= dengi_1k * CUPURA_1K
    dengi_5h = dengi // CUPURA_5H
    dengi -= dengi_5h * CUPURA_5H
    dengi_2h = dengi // CUPURA_2H
    dengi -= dengi_2h * CUPURA_2H
    dengi_1h = dengi // CUPURA_1H
    return dengi_5k, dengi_2k, dengi_1k, dengi_5h, dengi_2h, dengi_1h

d = int(input("Введите количество денег(кратно 100):"))
print(f"""
        Вам выдастя:
        {bankomat(d)[0]} - пятитысячных купюр
        {bankomat(d)[1]} - двухтысячных купюр
        {bankomat(d)[2]} - тысячных купюр
        {bankomat(d)[3]} - пятисотых купюр
        {bankomat(d)[4]} - двухсотых купюр
        {bankomat(d)[5]} - сотых купюр
""")
