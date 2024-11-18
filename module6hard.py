import math

class Figure:
    def __init__(self, sides_count=0, *sides):
        self.sides_count = sides_count
        self.__sides = list(sides) if len(sides) == sides_count else [1] * sides_count
        self.__color = [0, 0, 0]
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(c, int) and 0 <= c <= 255 for c in [r, g, b])

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def get_sides(self):
        return self.__sides

    def __is_valid_sides(self, *sides):
        return all(isinstance(side, int) and side > 0 for side in sides) and len(sides) == self.sides_count

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

class Circle(Figure):
    def __init__(self, color, radius):
        super().__init__(1, radius)
        self.set_color(*color)
        self.__radius = radius

    def get_square(self):
        return math.pi * (self.__radius ** 2)

class Triangle(Figure):
    def __init__(self, color, *sides):
        super().__init__(3, *sides)
        self.set_color(*color)

    def get_square(self):
        s = len(self) / 2
        a, b, c = self.get_sides()
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

class Cube(Figure):
    def __init__(self, color, edge_length):
        super().__init__(12, edge_length, edge_length, edge_length, edge_length, edge_length, edge_length, edge_length, edge_length, edge_length, edge_length, edge_length, edge_length)
        self.set_color(*color)
        self.__edge_length = edge_length

    def get_volume(self):
        return self.__edge_length ** 3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)

cube1 = Cube((222, 35, 130), 6)



# Проверка на изменение цветов:

circle1.set_color(55, 66, 77) # Изменится

print(circle1.get_color())

cube1.set_color(300, 70, 15) # Не изменится

print(cube1.get_color())



# Проверка на изменение сторон:

cube1.set_sides(5, 3, 12, 4, 5) # Не изменится

print(cube1.get_sides())

circle1.set_sides(15) # Изменится

print(circle1.get_sides())



# Проверка периметра (круга), это и есть длина:

print(len(circle1))



# Проверка объёма (куба):

print(cube1.get_volume())

