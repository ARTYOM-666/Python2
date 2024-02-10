import doctest

class Auto:
    """Базовый класс, представляющий автомобиль (любой)."""

    def __init__(self, brand: str, model: str, horse_power: int, price: float):
        """
        Инициализация нового объекта Auto.

        :param brand: Марка автомобиля.
        :param model: Модель автомобиля.
        :param horse_power: Количество лошадинных сил у авто.
        :param price: Цена авто.

        Примеры:
        >>> automobile = Auto("Wolkswagen", "Tiguan", 249, 1560000)
        """
        if not isinstance(brand, str):
            raise TypeError("Марка автомобиля должна быть типа str")
        self.brand = brand

        if not isinstance(model, str):
            raise TypeError("Модель автомобиля должна быть типа str")
        self.model = model

        if not isinstance(horse_power, int):
            raise TypeError("Количество лошадинных сил автомобиля должно быть целым число")
        if horse_power < 0:
            raise ValueError("Количество лошадинных сил не может быть отрицательным числом")
        self.horse_power = horse_power

        if not isinstance(price, (int, float)):
            raise TypeError("Цена автомобиля должна быть типа int или float")
        if price < 0:
            raise ValueError("Цена автомобиля не может быть отрицательным числом")
        self.price = price

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта Automobile для печати.

        :return: Строковое представление автомобиля для печати.

        Примеры:
        >>> automobile = Auto("Wolkswagen", "Tiguan", 249, 1560000)
        >>> print(automobile)
        Wolkswagen Tiguan, 249 л.с., 1560000 руб.
        """
        return f"{self.brand} {self.model}, {self.horse_power} л.с., {self.price} руб."

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта Automobile для отладки.

        :return: Строковое представление автомобиля для печати.

        Примеры:
        >>> automobile = Auto("Wolkswagen", "Tiguan", 249, 1560000)
        >>> automobile.__repr__()
        'Auto (brand = "Wolkswagen", model = "Tiguan", horse_power = 249, price = 1560000'
        """
        return f'Auto (brand = "{self.brand}", model = "{self.model}", horse_power = {self.horse_power}, price = {self.price}'


    def check_engine(self) -> bool:
        """
        Проверка двигателя на наличие ошибок.

        :return: True, если двигатель имеет ошибки, False в противном случае.

        Примеры:
        >>> automobile = Auto("Wolkswagen", "Tiguan", 249, 1560000)
        >>> automobile.check_engine()
        """
        ...

    def start_engine(self) -> None:
        """
        Запуск двигателя.

        Примеры:
        >>> automobile = Auto("Wolkswagen", "Tiguan", 249, 1560000)
        >>> automobile.start_engine()
        """
        if self.check_engine() == False:
            ...

    def stop_engine(self) -> None:
        """
        Выключение двигателя.

        Примеры:
        >>> automobile = Auto("Wolkswagen", "Tiguan", 249, 1560000)
        >>> automobile.stop_engine()
        """
        ...

class Electrocar(Auto):
    """Класс, представляющий электрокар, наследующийся от Auto"""

    def __init__(self, brand: str, model: str, horse_power: int, price: float, battery_capacity: int, power_reserve: int):
        """
        Инициализация нового объекта Electrocar.

        :param brand: Марка электрокара.
        :param model: Модель эклетромобиля.
        :param horse_power: Количество лошадиных сил в электромобиле.
        :param price: Цена электромобиля.
        :param battery_capacity: Емкость аккумулятора в электромобиле.
        :param power_reserve: Запас хода электромобиля.

        Примеры:
        >>> elcar = Electrocar("Tesla", "Model S", 762, 4590000, 568, 507)
        """
        super().__init__(brand, model, horse_power, price)

        if not isinstance(battery_capacity, int):
            raise TypeError("Емкость батареи должна быть целым числом")
        if battery_capacity < 0:
            raise ValueError("Емкость батареи должна быть положительным числом")
        self.battery_capacity = battery_capacity

        if not isinstance(power_reserve, int):
            raise TypeError("Запас хода должен быть целым числом")
        if power_reserve < 0:
            raise ValueError("Запас хода должен быть положительным числом")
        self.power_reserve = power_reserve

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта Electrocar для отладки.

        :return: Строковое представление электромобиля.

        Примеры:
        >>> elcar = Electrocar("Tesla", "Model S", 762, 4590000, 568, 507)
        >>> elcar.__repr__()
        'Electrocar (brand = "Tesla", model = "Model S", horse_power = 762, price = 4590000, battery_capacity = 568, power_reserve = 507)'
        """
        return f'Electrocar (brand = "{self.brand}", model = "{self.model}", horse_power = {self.horse_power}, price = {self.price}, battery_capacity = {self.battery_capacity}, power_reserve = {self.power_reserve})'

    def start_engine(self, battery_charge: int) -> None:
        """
        Запуск двигателя.
        Метод был перегружен вследствие того, что в электромобилях дополнительно необходимо проверить уровень заряда аккумулятора.

        Примеры:
        >>> elcar = Electrocar("Tesla", "Model S", 762, 4590000, 568, 507)
        >>> elcar.start_engine()
        """
        if not isinstance(battery_charge, float):
            raise TypeError("Заряд батареи должен быть числом")
        if battery_charge < 0:
            raise ValueError("Заряд батареи должен быть положительным числом")
        if battery_charge == 0:
            raise ValueError("Уровень батареи критически низок для запуска двигателя")
        if self.check_engine() == False:
            ...

    def regeneration_mode_on(self) -> None:
        """
        Включение режима рекуперации.

        Примеры:
        >>> elcar = Electrocar("Tesla", "Model S", 762, 4590000, 568, 507)
        >>> elcar.regeneration_mode_on()
        """
        ...

    def regeneration_mode_off(self) -> None:
        """
        Выключение режима рекуперации.

        Примеры:
        >>> elcar = Electrocar("Tesla", "Model S", 762, 4590000, 568, 507)
        >>> elcar.regeneration_mode_off()
        """
        ...

    def power_save_mode_on(self, charge_percentage: int) -> None:
        """
        Включение режима экономии заряда аккумулятора.

        :param charge_percentage: процент заряда аккумулятора, начиная с которого включается режим энергосбережения.

        Примеры:
        >>> elcar = Electrocar("Tesla", "Model S", 762, 4590000, 568, 507)
        >>> elcar.power_save_mode_on(40)
        """
        if not isinstance(charge_percentage, int):
            raise TypeError("Заряд аккумулятора, начиная с которого включится режим экономии заряда, должен быть целым числом")
        if charge_percentage < 0:
            raise ValueError("Заряд аккумулятора, начиная с которого включится режим экономии заряда, должен быть целым положительным числом")
        ...


if __name__ == "__main__":
    doctest.testmod()
    pass
