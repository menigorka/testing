import math

class Geometry:
    def circle_area(radius):
        return math.pi * radius ** 2

    def triangle_area(side1, side2, side3):
        s = (side1 + side2 + side3) / 2
        return math.sqrt(s * (s - side1) * (s - side2) * (s - side3))

    def is_right_triangle(side1, side2, side3):
        sides = [side1, side2, side3]
        sides.sort()
        return math.isclose(sides[0] ** 2 + sides[1] ** 2, sides[2] ** 2)

if __name__ == "__main__":
   
   #примеры использования
    print("Площадь круга:", Geometry.circle_area(5))
    print("Площадь треугольника:", Geometry.triangle_area(3, 4, 5))
    print("Прямоугольный треугольник?", Geometry.is_right_triangle(3, 4, 5))