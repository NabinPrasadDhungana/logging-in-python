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
            result = add(a, b)
            print(f"Sum of {a} and {b} is ", result)
            logger.info('Addition performed: %s + %s = %s', a, b, result)

        elif user_input == '2':
            result = subtract(a, b)
            print(f"Subtraction of {a} and {b} is ", result)
            logger.info('Subtraction performed: %s - %s = %s', a, b, result)

        elif user_input == '3':
            result = multiply(a, b)
            print(f"Multiplication of {a} and {b} is ", result)
            logger.info('Multiplication performed: %s * %s = %s', a, b, result)

        elif user_input == '4':
            try:
                result = divide(a, b)
                print(f"Division of {a} and {b} is ", result)
                logger.info('Division performed: %s / %s = %s', a, b, result)
            except ZeroDivisionError:
                print("Tried to divide a number by Zero (0)")
                logger.exception("Tried to divide a number by Zero (0)")

        elif user_input == '5':
            result = power(a, b)
            print(f"Power of {a} and {b} is ", result)
            logger.info('Power performed: %s ** %s = %s', a, b, result)

        else:
            result = root(a, b)
            print(f"Root of {a} and {b} is ", result)
            logger.info('Root performed: %s root %s = %s', a, b, result)
        
        choice = input("Do you want to continue? (y/n): ")
        if choice == 'n':
            logger.info("User opted to stop calculation.\n")
            break
        logger.info("User opted to continue calculation.")
    else:
        print("Invalid input!")
        logger.error("User input is invalid.")
        