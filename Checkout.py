class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class User:
    def __init__(self, login, balance=0):
        self.login = login
        self.balance = balance

    def __str__(self):
        return f'Пользователь {self.login}, баланс - {self.balance}'

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, new_balance):
        self.__balance = new_balance

    def deposit(self, value):
        self.__balance += value

    def payment(self, minus_value):
        if self.__balance < minus_value:
            print('Не хватает средств на балансе. Пополните счет')
            return False
        else:
            self.__balance -= minus_value
            return True


class Cart:
    def __init__(self, user):
        self.user = user
        self.goods = {}
        self.__total = 0

    def add(self, product, amount=1):
        if product in self.goods:
            self.goods[product] += amount
        else:
            self.goods[product] = amount
        self.__total += product.price * amount

    def remove(self, product, amount=1):
        if self.__total >= product.price:
            self.__total -= product.price * self.goods[product]
        if self.goods[product] >= amount:
            self.goods[product] -= amount
        else:
            del self.goods[product]

    @property
    def total(self):
        return self.__total

    def order(self):
        if self.user.payment(self.__total):
            print('Заказ оплачен')
        else:
            print('Проблема с оплатой')

    def print_check(self):
        LD = sorted(self.goods, key=lambda x: x.name)
        print("---Your check---")
        for i in LD:
            print(f'{i.name} {i.price} {self.goods[i]} {self.goods[i] * i.price}')
        print(f'---Total: {self.total}---')