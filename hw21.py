from abc import ABC, abstractmethod


class Storage(ABC):
    def __init__(self, items, capacity):
        self._items = items
        self._capacity = capacity

    @property
    def items(self):
        return self._items

    @property
    def capacity(self):
        return self._capacity

    @abstractmethod
    def add(self, name, count):
        pass

    @abstractmethod
    def remove(self, name, count):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass


class Store(Storage):
    def __init__(self, items, capacity=100):
        super().__init__(items, capacity)

    def add(self, name, count):
        if self.get_free_space() >= count:
            if name not in self.items:
                self.items[name] = count
            else:
                self.items[name] += count
            return True
        else:
            return False

    def remove(self, name, count):
        if self.items[name] >= count:
            self.items[name] -= count
            if self.items[name] == 0:
                del self.items[name]
            return True

    def get_free_space(self):
        return self.capacity - sum(self.items.values())

    def get_unique_items_count(self):
        return len(self.items)


class Shop(Store):
    def __init__(self, items, capacity=20):
        super().__init__(items, capacity)

    def add(self, name, count):
        if len(self.items) < 5:
            super().add(name, count)
            return True
        elif len(self.items) == 5 and name in self.items:
            super().add(name, count)
            return True


class Request:
    def __init__(self, where_from, to_where, r_amount, product):
        self.where_from = where_from
        self.to_where = to_where
        self.r_amount = r_amount
        self.product = product

    def __repr__(self):
        return f"Доставить {self.r_amount} {self.product} из {self.where_from} в {self.to_where}"


def main():
    shop_items = {"икорка": 3, "печеньки": 2, "мандаринки": 1, "шампусик": 5}
    store_items = {"мыло": 1, "веревки": 1, "крокодилы": 1, "чебурашки": 5}
    shop = Shop(shop_items)
    store = Store(store_items)
    print("У нас есть магазин и склад:")
    while len(shop_items) > -1:
        print(f"в магазине товары в наличии: {shop_items}")
        print(f"на складе товары в наличии: {store_items}")
        print("Укажите откуда, куда, сколько и чего перевозим")
        where_from = input("Укажите откуда>>>")
        to_where = ""
        if where_from == "склад":
            to_where = "магазин"
        elif where_from == "магазин":
            to_where = "склад"
        product = input("Укажите что забираем>>>")
        r_amount = int(input("Укажите сколько забираем>>>"))
        request = Request(where_from, to_where, r_amount, product)
        print(request)
        if where_from == "склад":
            if store.remove(product, r_amount):
                if shop.add(product, r_amount):
                    print(f"Курье забрал из {where_from} -> {product} - {r_amount}шт и выехал {to_where} ")
                    print("Курьер привез")
                else:
                    print("Магазин переполнен")
            else:
                print("Товара не хватает на складе")
        elif where_from == "магазин":
            if shop.remove(product, r_amount):
                if store.add(product, r_amount):
                    print(f"Курье забрал из {where_from} -> {product} - {r_amount}шт и выехал {to_where} ")
                    print("Курьер привез")
                else:
                    print("Склад переполнен")
            else:
                print("Товара не хватает в магазине")


if __name__ == "__main__":
    main()
