"""
ter1. Maximum of three numbers
Write a program that determines – using a function – the minimum of three integers which are read from the console.
"""
def main():
    num1 = int(input("enter a number: "))
    num2 = int(input("enter a number: "))
    num3 = int(input("enter a number: "))

    print(f"min of the 3 numbers is {min(num1,num2,num3)} and \n"
          f"max of the 3 numbers is {max(num1,num2,num3)}")


if __name__ == '__main__':
    main()