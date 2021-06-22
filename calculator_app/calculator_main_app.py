"""
calculator main application file.

This applicaiton is our caluculator functionality appliction.
It provides aritmetic operations on two numbers like addition, subtraction, multiplication division.
"""
print(f"value of __name__ is: {__name__}")

FIRST_NUMBER = 0
SECOND_NUMBER = 0

def main():
    print("welcome to calculator application developed in colloboration with palani and rao")
    FIRST_NUMBER = int(input("Enter the first number: "))
    SECOND_NUMBER = int(input("Enter the second number: "))



if __name__ == "__main__":
    main()