from Classhome import Shop, Store, Request, Storage
from func import store_shop

if __name__ == '__main__':
    request = Request(store_shop())
    print(request.__repr__())
    shop=Shop()
    store=Store()
    print(f" осталось в магазине {shop.get_items()}")
    print(f" осталось в Cкладе {store.get_items()}")



