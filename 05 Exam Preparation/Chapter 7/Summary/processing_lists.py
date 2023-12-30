def calculate_total(nums):
    # Calculate the total of numeric values in the list
    total = 0
    for num in nums:
        total += num
    return total

def calculate_average(nums):
    # Calculate the average of numeric values in the list
    total = calculate_total(nums)
    average = total / len(nums)
    return average

def save_list_to_file(my_list, filename):
    # Save the contents of a list to a file
    with open(filename, 'w') as file:
        for item in my_list:
            file.write(str(item) + '\n')

def read_list_from_file(filename):
    # Read data from a file into a list
    with open(filename, 'r') as file:
        lines = file.readlines()
        # Convert lines to a list of integers
        my_list = [int(line.strip()) for line in lines]
        return my_list

# Example usage
numbers = [10, 20, 30, 40, 50]

# Calculate total and average
total_sum = calculate_total(numbers)
average_value = calculate_average(numbers)

print("Total:", total_sum)
print("Average:", average_value)

# Save the list to a file
save_list_to_file(numbers, 'numbers.txt')

# Read the list from the file
read_numbers = read_list_from_file('numbers.txt')
print("List from file:", read_numbers)



