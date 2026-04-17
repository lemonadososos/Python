class Zombie():
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def bite(self, damage):
        self.hp -= damage
        return self.hp


zombie = Zombie('Мясник', 100)


hit = int(input('Введите силу укуса: '))
remaining = zombie.bite(hit)

print(f'Остаток здоровья: {remaining}')