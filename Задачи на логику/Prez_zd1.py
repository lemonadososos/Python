SUTKI = 24                                          #Количество часов в дне
OSTAVSHIESYA_CHASTI = 5                             #Количество оставшихся частей дня, т.к прошла 1/5 времени, которая ещё осталась

Vsego_chastey = OSTAVSHIESYA_CHASTI + 1             #Полное количество частей дня, включая оставшееся время
Tekushee_wrema = int(SUTKI / Vsego_chastey)         #Деление часов в сутках на части, чтобы узнать длительность одной части

print(f"Текущее время: {Tekushee_wrema}")