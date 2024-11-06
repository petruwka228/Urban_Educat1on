class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        house = super().__new__(cls)
        cls.houses_history.append(args)
        return house
    def __init__(self, name, number_of_floors):
        self.number_of_floors = number_of_floors
        self.name = name
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"
    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
    def  __lt__(self, other):
        if isinstance(other, int) and isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
    def __le__(self, other):
        if isinstance(other, int) and isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
    def __gt__(self, other):
        if isinstance(other, int) and isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
    def __ge__(self, other):
        if isinstance(other, int) and isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
    def __ne__(self, other):
        if isinstance(other, int) and isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
    def __add__(self, value):
        self.number_of_floors = self.number_of_floors + value
        return self.number_of_floors
    def __radd__(self, value):
        self.number_of_floors = value + self.number_of_floors
        return self.number_of_floors
    def __iadd__(self, value):
        self.number_of_floors += value
        return self.number_of_floors
    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)
del h2
del h3
print(House.houses_history)