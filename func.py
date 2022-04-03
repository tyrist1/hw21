from warehouse import shop, store, locations
from Classhome import Shop, Store, Request


def nname():
    print("Введите товар:")
    name = input()
    return name


def ccount():
    print("Введите количество:")
    count = int(input())

    return count

def view_items_all(my_dict):
    i = "\n"
    for k,v in my_dict.items():
        i = i + k + " - " + str(v) + '\n'
    return i

def store_shop():
    shop_class = Shop(dict_init=shop)
    store_class = Store(dict_init=store)
    print(f"Добро пожаловать в наш магазин, в нём много товаров: {view_items_all(shop_class.get_items())}"
          f"\nна складе ещё больше: {view_items_all(store_class.get_items())}")
    print("Введите  количество и товар")
    print("если хотите доставить товара со склада в магазин, жмите 1 \n"
          "если хотите отправить товар из магазина на склад жмите 2 \n"
          "если хотите купить товар жмите 3, спасибо")
    vvod = int(input())

    if vvod == 1:
        name = nname()
        if name in store.keys():
            count = ccount()
            if count <= store[name]:
               print(Request( f"Доставить {count} {name} из {locations[0]} в {locations[1]}"))
               store_class.remove(name=name, count=count)
               shop_class.add(name=name,count=count)
    if vvod == 2:
        name = nname()
        if name in store.keys():
            count = ccount()
            if count <= store[name]:
                print(Request(f"Доставить {count} {name} из {locations[1]} в {locations[0]}"))
                shop_class.remove(name=name, count=count)
                store_class.add(name=name, count=count)
    if vvod == 3:
        name = nname()
        if name in store.keys():
            count = ccount()
            if count <= store[name]:
                print(Request(f"Купить {count} {name} из {locations[1]} в {locations[2]}"))
                shop_class.remove(name=name, count=count)

    return shop_class, store_class, locations


