import logging
from calculator_logger import setup_logger

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    return a / b

def multiply(a, b):
    return a * b

def power(a, b):
    return a ** b

def root(a, b):
    return a ** (1/b)

logger = setup_logger()
logger.debug("=" * 40)
logger.info("Calculator intantiated!")
logger.debug("=" * 40)

while True:
    print("1. Add       2. Subtract")
    print("3. Multiply  4. Divide")
    print("5. Power     6. Root")
    user_input = input("Enter what you want to do: (1/2/3/4/5/6)")

    if user_input in ['1', '2', '3', '4', '5', '6']:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))

        if user_input == '1':
            print(f"Sum of {a} and {b} is ", add(a, b))
            logger.info('Addition performed')

        elif user_input == '2':
            print(f"Subtraction of {a} and {b} is ", subtract(a, b))
            logger.info('Subtraction performed')

        elif user_input == '3':
            print(f"Multiplication of {a} and {b} is ", multiply(a, b))
            logger.info('Multiplication performed')

        elif user_input == '4':
            try:
                print(f"Division of {a} and {b} is ", divide(a, b))
                logger.info('Division performed')
            except ZeroDivisionError:
                print("Tried to divide a number by Zero (0)")
                logger.error("Tried to divide a number by Zero (0)")

        elif user_input == '5':
            print(f"Power of {a} and {b} is ", power(a, b))
            logger.info('Indices performed')

        else:
            print(f"Root of {a} and {b} is ", root(a, b))
            logger.info('Root performed')
        
        choice = input("Do you want to continue? (y/n): ")
        if choice == 'n':
            logger.info("User opted to stop calculation.\n")
            break
        logger.info("User opted to continue calculation.")
    else:
        print("Invalid input!")
        logger.error("User input is invalid.")
        