def greet():
    """
    A simple function that prints hello
    :return: none
    """

    print("hello")

#greet() to call function
greet()
greet()

def greet2(name):
    """
     A more advanced greet function
    :param name: name of the person to geet
    :return: None
    """
    print(f"hello, {name}")

greet2("james")
greet2("bob")

def average(a, b):
    """

    :param a: first number
    :param b: second number
    :return:  float, average of a and b
    """

#average (a+b)/" used to store the value but not necessary
    return (a+b)/2
print(average(10, 5))

def divide(x, y=2):
    """
     Divide x by y
    :param x: first number
    :param y: second number
    :return:  float, division of y and x
    """
    if y == 0:
        return None
    return x / y
print(divide(10, 20))
print(divide(10, 0))
print(divide(10, 1))
print(divide(y=1, x=10))
print(divide(30))

def bond(first_name="Enrique", last_name="Peralta"):
    return f"{last_name}, {first_name} {last_name}"

def introduce(name):
    print(f"The name is: {name}")

print(bond("james", "smith"))
introduce(bond("james", "Smith"))
introduce(bond())



