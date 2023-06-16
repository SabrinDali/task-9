# Write a Rectangle class, allowing you to build a rectangle
# with length and width attributes.
# Create a Perimeter() method to calculate the perimeter of the rectangle
# Area() method to calculate the area of the rectangle.

class RectangleShape:
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def rectangle_perimeter(self):
        return 2 * (self.length + self.width)

    def rectangle_area(self):
        return self.length * self.width

# newRectangle = RectangleShape(5, 7)
# print(newRectangle.rectangle_perimeter())
# print(newRectangle.rectangle_area())


    def display(self):
       print("The length of rectangle is: ", self.length)
       print("The width of rectangle is: ", self.width)
       print("The perimeter of rectangle is: ", self.rectangle_perimeter())
       print("The area of rectangle is: ", self.rectangle_area())

# Create a Parallelepipede child class inheriting from the Rectangle class
# and with a height attribute and another Volume() method
# to calculate the volume of the Parallelepiped.


class Parallelepipede(RectangleShape):
    def __init__(self, length, width , height):
        RectangleShape.__init__(self, length, width)
        self.height = height

    def volume(self):
        return self.length * self.width * self.height

# new_rectangle = RectangleShape(8, 12)
# new_rectangle.display()
# new_parallelepipede = Parallelepipede(8 , 12 , 10)
# print("the volume of New Parallelepipede is: " , new_parallelepipede.volume())




