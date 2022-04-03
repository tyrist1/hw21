from Classhome import Shop, Store, Request, Storage
from func import store_shop, view_items_all

if __name__ == '__main__':

    shop_class, store_class, location = store_shop()
    print(f"Осталось в магазине {view_items_all(shop_class.get_items())}")
    print(f"Осталось в складе {view_items_all(store_class.get_items())}")





