
def add(x, y):
    return (x + y)
    
def substract(x, y):
    return x - y

def multiply(x, y):
    return x*y

def divide(x, y)        :
    try:
      z = x/y
    except ZeroDivisionError as e:
      print(e)
    else:
      z = 0
    
    return z

def square(x):
    pass

