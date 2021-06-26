"""
calculator main application file.

This applicaiton is our caluculator functionality appliction.
It provides aritmetic operations on two numbers like addition, subtraction, multiplication division.
"""

from additions import add
from multiplications import mul
from divisions import div
from subtractions import sub



print(f"value of __name__ is: {__name__}")

FIRST_NUMBER = 0
SECOND_NUMBER = 0

def main():
    print("welcome to calculator application developed in colloboration with palani and rao")
    FIRST_NUMBER = int(input("Enter the first number: "))
    SECOND_NUMBER = int(input("Enter the second number: "))

    choice = int(input("Enter your choice: 1 -> add, 2 -> sub, 3->mul, 4->div"))
    if choice ==1:
        print(f"add: {add(FIRST_NUMBER, SECOND_NUMBER)}")
    elif choice == 2:
        print(f"sub: {sub(FIRST_NUMBER, SECOND_NUMBER)}")
    elif choice == 3:
        print(f"mul: {mul(FIRST_NUMBER, SECOND_NUMBER)}")
    elif choice == 4:
        print(f"div: {div(FIRST_NUMBER, SECOND_NUMBER)}")
    else:
        print("Invalid choice.")




if __name__ == "__main__":
    main()