from warehouse import shop, store, locations
from Classhome import Shop, Store


def nname():
    name = input()
    return name


def ccount():
    count = input()
    return count


def store_shop():
    print(f"""Добро пожаловать в наш магазин, в нём много товаров: {shop.items()}
                на складе ещё больше {store.items()}""")
    print("введите  количество и товар")
    print("""если хотите доставить товара со склада в магазин, жмите 1
    если хотите отправить товар из магазина на склад жмите 2
    если хотите купить товар жмите 3, спасибо""")

    if input() == 1:
        result = f"Доставить {ccount()} {nname()} из {locations[0]} в {locations[1]}"
        Store.remove(name=nname(), count=ccount())
        Shop.add(name=nname(), count=ccount())
        if input == 2:
            result = f"Доставить {ccount()} {nname()} из {locations[1]} в {locations[0]}"
            Store.add(name=nname(), count=ccount())
            Shop.remove(name=nname(), count=ccount())
            if input == 3:
                result = f"Купить {ccount()} {nname()} из {locations[1]} в {locations[2]}"
                Shop.remove(name=nname(), count=ccount())
    return result


