
class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    #
    # def getWidth(self):
    #     return self.a
    # def getHeigth(self):
    #     return self.b

    def get_area(self):
        return self.a * self.b

class NonPositiveDigitException(ValueError):
    pass

class Square:
    def __init__(self, a):
        try:
            self.a = a
            if a <= 0:
                raise NonPositiveDigitException("Square's side can't be 0 or less")
        except NonPositiveDigitException as e:
            print(e)

    def get_area_square(self):
        return self.a ** 2


class Sircle:
    def __init__(self, r):
        self.r = r

    def get_radius(self):
        return 3.14 * self.r ** 2