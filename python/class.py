# Характеристики кофейного напитка:
# - Название (например, "Капучино")
# - Объем (например, 300 мл)
# - Цена (например, 150 рублей)

class Coffee:
    def __init__(self, name, volume, price):
        self.name = name
        self.volume = volume
        self.price = price



class Order:
    def __init__(self):
        self.items = []  # Инициализация списка товаров при создании заказа

    def add_item(self, coffee_item):
        self.items.append(coffee_item)  # Добавление товара в заказ

    def calculate_total(self):
        total_price = 0
        for item in self.items:
            total_price += item.price
        return total_price
    
    def display_order(self):
        print("=========================")
        print("  Чек: Кофейня 'Бодрый Бобёр'")
        print("-------------------------")
        
        if not self.items:
            print("       Ваш заказ пуст")
        else:
            for item in self.items:
                # Для каждой позиции в заказе выводим ее данные
                print(f"- {item.name} ({item.volume} мл) ..... {item.price} руб.")
        
        print("-------------------------")
        # Вызываем наш же метод для подсчета итога
        total = self.calculate_total()
        print(f"ИТОГО К ОПЛАТЕ: {total} руб.")
        print("=========================")


cappuccino = Coffee("Капучино", 250, 180)
espresso = Coffee("Эспрессо", 50, 120)
latte = Coffee("Латте", 350, 200)
order_1 = Order()
order_1.add_item(cappuccino)
order_1.add_item(espresso)
order_1.add_item(espresso)
# order_1.display_order()
print(order_1.calculate_total())