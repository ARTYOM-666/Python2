# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
from typing import Union

class House:
    def __init__(self, amount_of_residents: int, amount_of_elevators: int):
        '''
        Жилой дом с каким-то количсетвом жителей и лифтов.

        :param amount_of_residents: количество жителей;
        :param amount_of_elevators: количество лифтов в доме;

        Примеры:
        >>> house1 = House(500, 0)
        '''
        if not isinstance(amount_of_residents, int):
            raise TypeError('Количество жителей в доме должно быть int')
        if amount_of_residents < 0:
            raise ValueError('Количество жителей в доме не может быть отрицательным')
        self.amount_of_residents = amount_of_residents

        if not isinstance(amount_of_elevators, int):
            raise TypeError('Количество лифтов в доме должно быть int')
        if amount_of_elevators < 0:
            raise ValueError('Количество лифтов в доме не может быть отрицательным')
        self.amount_of_elevators = amount_of_elevators

    def add_residents(self, residents: int) -> None:
        '''
        Подсчёт количества жителей при заселении новых.

        :param residents: количество заселяемых жильцов

        Примеры:
        >>> house1 = House(500, 0)
        >>> house1.add_residents(20)
        '''
        if not isinstance(residents, int):
            raise TypeError('Количество людей, заселившихся в дом должно быть int')
        if residents < 0:
            raise ValueError('Количество людей, заселившихся в дом не может быть отрицательным')
        self.residents = residents
        self.amount_of_residents += residents

    def is_elevators(self) -> bool:
        '''
        Проверка на то, есть ли в доме лифты.

        Возвращает True, если есть лифты, и False в противном случае
        '''
        if self.amount_of_elevators != 0:
            return True
        if self.amount_of_elevators == 0:
            return False

class CreditCard:
    def __init__(self, limit: Union[int, float], balance: Union[int, float]):
        '''
            Кредитная карта с определенным лимитом и балансом на счету

            :param limit: лимит по кредитной карте
            :param balance: текущий баланс на счету

            Примеры:
            >>> credit1 = CreditCard(100000, -90000)
            '''
        if (not isinstance(limit, (int, float))) and (limit < 0):
            raise TypeError('Лимит на счету должен быть числом больше 0')
        if not isinstance(balance, (int, float)):
            raise TypeError('Баланс на счету должен быть числомt')
        if balance < 0:
            if limit < balance * (-1):
                raise ValueError('Баланс не может быть меньше лимита')
        self.limit = limit
        self.balance = balance

    def salary_payment(self, salary) -> None:
        '''
        Вычисление балансы при выплате зарплаты

        :param salary: размер выплачиваемой зарплаты

        Примеры:
        >>> credit1 = CreditCard(100000, -90000)
        >>> credit1.salary_payment(30000)
        '''
        if not isinstance(salary, (int, float)):
            raise TypeError('Зарплата должна быть числом')
        if salary < 0:
            raise ValueError('Зарплата не может быть отрицательна')
        self.salary = salary
        self.balance += salary

    def debt(self) -> (int, float):
        '''
        Вычисление задолженности банку
        '''
        if self.balance < 0:
            print(f"Задолженность составляет: {-1 * self.balance} рублей")
        if self.balance >= 0:
            print("Задолженности нет")

class ProfileInstagram:
    def __init__(self, amount_of_subscriptions: int, amount_of_subscribers: int):
        '''
        Профиль инстаграмма

        :param amount_of_subscriptions: число подписок
        :param amount_of_subscribers: число подписчиков

        Пример:
        >>> profile1 = ProfileInstagram(437, 29)
        '''
        if not isinstance(amount_of_subscriptions, int) or not isinstance(amount_of_subscribers, int):
            raise TypeError('Число подписок (подписчиков) должно быть числом')
        if amount_of_subscriptions < 0 or amount_of_subscribers < 0:
            raise ValueError('Число подписок (подписчиков) не может быть отрицательным')
        self.amount_of_subscriptions = amount_of_subscriptions
        self.amount_of_subscribers = amount_of_subscribers

    def add_subscribers(self, subscribers):
        '''
        Добавление подписчиков

        :param subscribers: число подписчиков

        Примеры:
        >>> profile1 = ProfileInstagram(437, 29)
        >>> profile1.add_subscribers(15)
        '''
        if not isinstance(subscribers, int):
            raise TypeError('Число подписчиков должно быть числом')
        if subscribers < 0:
            raise ValueError('Число подписчиков не может быть отрицательным')
        self.subscribers = subscribers
        self.amount_of_subscriptions += subscribers

    def add_subscriptions(self, subscriptions):
        '''
        Добавление подписчиков

        :param subscribers: число подписчиков

        Примеры:
        >>> profile1 = ProfileInstagram(437, 29)
        >>> profile1.add_subscriptions(15)
        '''
        if not isinstance(subscriptions, int):
            raise TypeError('Число подписок должно быть числом')
        if subscriptions < 0:
            raise ValueError('Число подписок не может быть отрицательным')
        self.subscriptions = subscriptions
        self.amount_of_subscriptions += subscriptions

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
    pass
