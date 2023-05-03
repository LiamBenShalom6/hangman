import math

def func(num1, num2):
    
    """The function calculates the hypotenuse in the triangle.
   :param num1: one side
   :param num2: other side
   :type num1: int
   :type num2: int
   :return: the hypotenuse in the triangl
   :rtype: float
   """
   
    return math.sqrt((math.pow(num1, 2)) + (math.pow(num2, 2)))

def main():
    # Call the function func
    print(func(num1=4, num2=8))
    print(help(func))
    print(func.__doc__)

if __name__ == "__main__":
    main()