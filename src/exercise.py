def main():
    #write your code below this line
    import numpy as np
    number1 = int(input("Write your first number: "))
    number2 = int(input("Write your second number: "))

    number3 = number1 + number2

    squareRoot = np.sqrt(number3)

    print(squareRoot)

if __name__ == '__main__':
    main()
