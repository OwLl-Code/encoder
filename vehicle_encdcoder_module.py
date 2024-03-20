import json  # импортируем модуль json для работы с JSON-данными


class Vehicle:  # объявляем класс Vehicle
    def __init__(
        self, registration_number, year_of_production, passenger, mass
    ):  # определяем конструктор класса
        self.registration_number = (
            registration_number  # инициализируем свойство с регистрационным номером
        )
        self.year_of_production = (
            year_of_production  # инициализируем свойство с годом производства
        )
        self.passenger = passenger  # инициализируем свойство с количеством пассажиров
        self.mass = mass  # инициализируем свойство с массой


class MyEncoder(json.JSONEncoder):  # создаем пользовательский кодировщик JSON
    def default(self, veh):  # переопределяем метод default
        if isinstance(veh, Vehicle):  # если объект является экземпляром класса Vehicle
            return veh.__dict__  # возвращаем словарь с атрибутами объекта
        return super().default(self, veh)  # вызываем родительский метод default


class MyDecoder(json.JSONDecoder):  # создаем пользовательский декодер JSON
    def decode_vehicle(
        self, veh
    ):  # определяем метод для декодирования данных о транспортном средстве
        return Vehicle(
            **veh
        )  # создаем объект класса Vehicle на основе переданных данных


def main():  # определяем функцию main
    print("Чем я могу помочь вам?")  # выводим приветственное сообщение
    print("1 - создать JSON-строку, описывающую транспортное средство")
    print("2 - декодировать JSON-строку в данные о транспортном средстве")
    answer = input("Ваш выбор: ")  # запрашиваем у пользователя выбор

    if answer == "1":  # если выбор - создать JSON-строку
        rn = input(
            "Регистрационный номер: "
        )  # запрашиваем данные о транспортном средстве
        yop = int(input("Год производства: "))
        psg = input("Пассажир [да/нет]: ").upper() == "ДА"
        mss = float(input("Масса: "))
        my_vehicle = Vehicle(rn, yop, psg, mss)  # создаем объект класса Vehicle
        print("Результирующая JSON-строка:")
        print(
            json.dumps(my_vehicle, cls=MyEncoder)
        )  # выводим JSON-строку, созданную из объекта

    elif answer == "2":  # если выбор - декодировать JSON-строку
        json_str = input(
            "Введите JSON-строку о транспортном средстве: "
        )  # запрашиваем JSON-строку
        try:
            new_car = json.loads(
                json_str, object_hook=MyDecoder().decode_vehicle
            )  # декодируем JSON-строку
            print(new_car.__dict__)  # выводим атрибуты декодированного объекта
        except TypeError:
            print("JSON-строка не содержит допустимого описания транспортного средства")

    print("Завершено")  # выводим сообщение о завершении выполнения


if __name__ == "__main__":  # если файл запущен самостоятельно
    print("Запущено как самостоятельный модуль")  # выводим сообщение
    main()  # вызываем функцию main
else:
    print("Запущено как импортируемый модуль")  # выводим сообщение
