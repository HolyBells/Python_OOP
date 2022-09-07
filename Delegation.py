class Initialization:
    def __init__(self, capacity, food):
        if isinstance(capacity, int):
            self.capacity = capacity
            self.food = food
        else:
            print('Количество людей должно быть целым числом')


class Vegetarian(Initialization):
    def __str__(self):
        return f'{self.capacity} людей предпочитают не есть мясо! Они предпочитают {self.food}'


class MeatEater(Initialization):
    def __str__(self):
        return f'{self.capacity} мясоедов в Москве! Помимо мяса они едят еще и {self.food}'


class SweetTooth(Initialization):
    def __str__(self):
        return f'Сладкоежек в Москве {self.capacity}. Их самая любимая еда: {self.food}'

    def __eq__(self, other):
        if isinstance(other, int):
            return self.capacity == other
        if isinstance(other, (Vegetarian, MeatEater)):
            return self.capacity == other
        else:
            return f'Невозможно сравнить количество сладкоежек с {other}'

    def __lt__(self, other):
        if isinstance(other, int):
            return self.capacity < other

        if isinstance(other, (Vegetarian, MeatEater)):
            return self.capacity < other.capacity
        else:
            return f'Невозможно сравнить количество сладкоежек с {other}'

    def __gt__(self, other):
        if isinstance(other, int):
            return self.capacity > other
        if isinstance(other, (Vegetarian, MeatEater)):
            return self.capacity > other.capacity
        else:
            return f'Невозможно сравнить количество сладкоежек с {other}'
