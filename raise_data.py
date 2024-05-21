import datetime


class RaiseClasses:
    @staticmethod
    def isinstance(obj, classes):
        if isinstance(obj, classes):
            return True
        else:
            raise TypeError(f"Неверный ти данных требуется передавать {classes}")


class CheckingDateCreate:
    def __init__(self):
        self.now = datetime.now().date()

    def __get__(self, instance, owner):
        return instance.__date_of_creation

    def __set__(self, instance, value):
        if self.now <= value:
            instance.__date_of_creation = value
        else:
            instance.__date_of_creation = self.now
