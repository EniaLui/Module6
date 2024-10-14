import math

class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__sides = list(sides)
        self.__color = list(color)
        self.filled: bool

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(i, int) and 0 <= i <= 255 for i in (r, g, b))

    def set_color(self, r,g,b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r,g,b]
        else:
            pass

    def __is_valid_sides(self, *new_sides):
        return all (isinstance(i, int) and 0 < i for i in new_sides) and len(new_sides) == self.sides_count

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

class Circle (Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color,*sides)
        self.__radius = self.get_sides()[0] / (2 * math.pi)

    def get_square (self):
        return math.pi * (self.__radius ** 2)

class Triangle (Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color,sides)

    def get_square(self):
        a = self.get_sides()[0] #a,b,c = стороны треугольника
        b = self.get_sides()[1]
        c = self.get_sides()[2]
        return sqrt(self.__len__() * (self.__len__() - a) * (self.__len__() - b) * (self.__len__() - c))

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) == 1:
            sides = sides * self.sides_count
        super().__init__(color,*sides)


    def get_volume(self):
        return self.get_sides()[0] ** 3

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
