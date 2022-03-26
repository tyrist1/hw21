from abc import ABC, abstractmethod


class BaseStorage:

    @property
    @abstractmethod
    def items(self):
        pass

    @property
    @abstractmethod
    def capacity(self):
        pass

# _________________________________________________________абстрактные поля и методы
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

class Storage(BaseStorage, ABC):
    def __init__(self, items, capacity):
        self._items = {}
        self._capacity = 100

    @abstractmethod
    def add(self, name, count):
        is_found = False
        if self.get_free_space() > count:
            for key in self._items.keys():
                if name == key:
                    self._items[key] = self._items[key] + count
                    is_found = True
            if not is_found:
                self._items[key] = count
            print("товар добавлен")
        else:
            print("товар не может быть добавлен")


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
# `add`(<название>, <количество>)  - увеличивает запас items
#
# `remove`(<название>, <количество>) - уменьшает запас items
#
# `get_free_space()` - вернуть количество свободных мест
#
# `get_items()` - возвращает сожержание склада в словаре {товар: количество}
#
# `get_unique_items_count()` - возвращает количество уникальных товаров.





