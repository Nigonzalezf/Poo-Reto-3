class MenuItem:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def calculate_total_price(self, quantity: int = 1) -> float:
        return self.price * quantity


class Beverage(MenuItem):
    def __init__(self, name: str, price: float, is_alcoholic: bool = False):
        super().__init__(name, price)
        self.is_alcoholic = is_alcoholic


class Appetizer(MenuItem):
    def __init__(self, name: str, price: float, is_shared: bool = True):
        super().__init__(name, price)
        self.is_shared = is_shared


class MainCourse(MenuItem):
    def __init__(self, name: str, price: float, is_vegetarian: bool = False):
        super().__init__(name, price)
        self.is_vegetarian = is_vegetarian


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item: MenuItem, quantity: int = 1):
        self.items.append((item, quantity))

    def calculate_total(self) -> float:
        total = sum(item.calculate_total_price(quantity) for item, quantity in self.items)
        return total

    def apply_discount(self, percentage: float) -> float:
        total = self.calculate_total()
        discount = total * (percentage / 100)
        return total - discount

    def print_order(self):
        print("Detalles del pedido:")
        for item, quantity in self.items:
            print(f"{quantity}x {item.name} - ${item.price:.2f} cada uno")
        print(f"Total: ${self.calculate_total():.2f}")


menu = [
    Beverage("Agua", 1.00, is_alcoholic=False),
    Beverage("Coca Cola", 3.00, is_alcoholic=False),
    Beverage("Cerveza", 2.50, is_alcoholic=True),
    Beverage("Copa de Vino", 10.00, is_alcoholic=True),
    Appetizer("Papas Fritas", 5.00, is_shared=True),
    Appetizer("Patacones", 5.50, is_shared=True),
    Appetizer("Nachos", 6.00, is_shared=True),
    Appetizer("Alitas de Pollo", 9.00, is_shared=False),
    MainCourse("Hamburguesa", 10.00, is_vegetarian=False),
    MainCourse("Pizza Napolitana", 12.00, is_vegetarian=True),
    MainCourse("Ensalada", 9.50, is_vegetarian=True),
    MainCourse("Filete de Res", 15.00, is_vegetarian=False),
]

order = Order()
order.add_item(menu[0], 1)
order.add_item(menu[3], 2)
order.add_item(menu[3], 1)
order.add_item(menu[7], 1)
order.add_item(menu[11], 1)

order.print_order()
print(f"Total con 10% de descuento: ${order.apply_discount(10):.2f}")
