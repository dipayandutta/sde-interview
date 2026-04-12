"""
This is the main calculation point
"""

from addition import Addition
from banner import Banner
from division import Division
from multiplication import Multiplication
from operations import operations
from subtraction import Subtraction


class CalculateEngine:
    def __init__(self):
        # initialize the banner object
        banner = Banner()
        banner.show_banner()  # print the banner on the screen
        self.result = 0

    def calculate_numbers(self) -> None:
        first_number = int(input("Enter First Number"))

        continue_calculation = True  # Default bool value to True
        while continue_calculation:
            print("Choose Symbol for the operation")

            for key, value in operations.items():
                print(f"{key}")

            user_selected_operation = input("Plaese Enter Symbol").strip()

            second_number = int(input("Enter the Second Number"))

            ops = operations.get(user_selected_operation)
            # print(ops)

            if ops == "add":
                # initialize the addition
                addition_numbers = Addition(first_number, second_number)
                self.result = addition_numbers.add()
                # print(result)

            elif ops == "minus":
                subtract_numbers = Subtraction(first_number, second_number)
                self.result = subtract_numbers.minus()
            elif ops == "divide":
                divide_numbers = Division(first_number, second_number)
                self.result = divide_numbers.divide()
                # print(result)
            elif ops == "multiplication":
                multiply_numbers = Multiplication(first_number, second_number)
                self.result = multiply_numbers.multiply()
                # print(result)
            else:
                print(f"Please enter a valid Symbol")

            print(self.result)
            next_operation = input(f"Type 'Yes' to continue").lower()

            if next_operation in ("yes", "y"):
                first_number = self.result

            elif next_operation in ("no", "n"):
                continue_calculation = False
