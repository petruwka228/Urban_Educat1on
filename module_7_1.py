class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    __file_name = 'product.txt'

    def get_products(self):
        try:
            file = open(self.__file_name, 'r')
            data = file.read().strip()
            file.close()
            return data
        except FileNotFoundError:
            return ""

    def add(self, *products):
        current_products = self.get_products().splitlines()
        current_names = [i.split(", ")[0] for i in current_products]
        file = open(self.__file_name, 'a')
        for product in products:
            if product.name not in current_names:
                file.write(str(product) + '\n')
                current_names.append(product.name)
            else:
                print(f'Продукт {product.name} уже есть в магазине')
        file.close()
s1 = Shop()

p1 = Product('Potato', 50.5, 'Vegetables')

p2 = Product('Spaghetti', 3.4, 'Groceries')

p3 = Product('Potato', 5.5, 'Vegetables')



print(p2) # __str__



s1.add(p1, p2, p3)



print(s1.get_products())