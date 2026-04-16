# 1-mashq
class MyFile:
    def __enter__(self):
        self.file = open("a.txt", "w")
        return self.file

    def __exit__(self, exc_type, exc, tb):
        self.file.close()

with MyFile() as f:
    f.write("Hello")
# 2-mashq
class Decorator:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        print("Before")
        self.func()
        print("After")

@Decorator
def say():
    print("Hello")

say()
# 3-mashq
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

d = D()
d.show()
# 4-mashq
class Student:
    def __init__(self):
        self._grade = 0

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        if value >= 0:
            self._grade = value
# 5-mashq
class Vector:
    def __init__(self, x):
        self.x = x

    def __mul__(self, other):
        return self.x * other.x

v1 = Vector(3)
v2 = Vector(4)
print(v1 * v2)
