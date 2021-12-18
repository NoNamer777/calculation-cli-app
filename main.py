import matplotlib.pyplot as ppl
import numpy as np


def add_numbers(num_a: int, num_b: int) -> int:
    return num_a + num_b


def subtract_numbers(num_a: int, num_b: int) -> int:
    return num_a - num_b


def divide_numbers(num_a: int, num_b: int) -> float:
    return num_a / num_b


def multiply_numbers(num_a: int, num_b: int) -> int:
    return num_a * num_b


def input_to_int() -> int:
    try:
        print('What number do you want to use?')

        return int(input())

    except ValueError:
        print('Whoopss.. Looks like your not providing me with a number, try again..')

        return input_to_int()


def execute_calculation(func_name, calculation_message: str) -> None:
    first_number = input_to_int()
    second_number = input_to_int()

    outcome = func_name(first_number, second_number)

    print(calculation_message.format(first_number, second_number, outcome))


if __name__ == "__main__":
    print("Hi, what's your name?")
    name = input()

    print(f"\nHello {name}")
    operation: str = None

    while operation != 'stop':
        print("\nWhat would you like to do?")

        operation = input().lower()

        if operation == 'add':
            execute_calculation(add_numbers, "adding {} + {} = {}")

        elif operation == 'subtract':
            execute_calculation(subtract_numbers, "subtracting {} - {} = {}")

        elif operation == 'multiply':
            execute_calculation(multiply_numbers, "multiplying {} * {} = {}")

        elif operation == 'divide':
            execute_calculation(divide_numbers, "dividing {} / {} = {}")

        elif operation == 'diagram':
            numpy_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

            ppl.plot(numpy_arr)

            ppl.show()

        elif operation != 'stop':
            print('Whooppss... I did not recognize your command... try again?')
