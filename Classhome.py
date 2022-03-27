from warehouse import shop, store
# Создайте абстрактный класс Storage

from abc import ABC, abstractmethod


class Storage(ABC):
    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def remove(self):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass

    # _________________________________________________________абстрактные поля и методы


# Шаг 2
# Реализуйте класс Store

class Store(Storage):
    def __init__(self):
        self.items = store
        self.capacity = 100

    def add(self, name, count):
        is_found = False
        if self.get_free_space() > count:
            for key in self.items.keys():
                if name == key:
                    self.items[key] = self.items[key] + count  # почему сюда прибавили
                    is_found = True
            if not is_found:
                self.items[key] = count
            print("товар добавлен")
        else:
            print(f"товар не может быть добавлен, свободных мест только на {self.get_free_space()}")

    def remove(self, name, count):
        is_found = False
        for key in self.items.keys():
            if name == key and self.items[key] - count >= 0:
                self.items[key] = self.items[key] - count
                print(f' покупка совершена, остаток товара {name} : {self.items[key]}')
            else:
                print(f'''{name} такого товара нет!!! 
                либо количество недостаточно , остаток {self.items[key]}''')

    def get_free_space(self):
        return self.capacity - sum(self.items.values())

    def get_items(self):
        return self.items

    def get_unique_items_count(self):
        return len(self.items.keys())

    # Реализуйте класс Shop.


class Shop(Store):
    def __init__(self, limit=5):
        super().__init__()
        self.items = shop
        self._capacity = 20
        self._limit = limit

    @property
    def get_item_limit(self):
        return self._limit

    def add(self, name, count):
        if self.get_unique_items_count() > self._limit:
            super.add(name, count)
        else:
            print(f' {name} не может быть добавлен')


class Request():
    def __init__(self, str):
        lst = self.get_info(str)
        self.from_ = lst[4]
        self.to = lst[6]
        self.amount = int(lst[1])
        self.product = lst[2]

    def get_info(self, str):
        return str.split(" ")

    def __repr__(self):
        return f'Доставить {self.amount} {self.product} из {self.from_} в {self.to}'
