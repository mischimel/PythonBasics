"""
6. Larger Than n
In a program, write a function that accepts two arguments:
a list, and a number n. Assume that the list contains numbers.
The function should display all of the numbers in the list that are greater than the number n.
"""
def main():

    def greater_n(list, n):
        # instantiate variables
        numbers = []
        for i in list:
            if i > n:
                numbers.append(i)
            else:
                None

        print(numbers)

    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    my_n = 6
    greater_n(my_list,my_n)

if __name__ == '__main__':
    main()