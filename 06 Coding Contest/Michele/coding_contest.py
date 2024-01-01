"""
Load and open the JSON-file via Python. Via iteration extract the content of the file and plot
(using the library matplotlib) the name and salary of the employees. Don't forget to add a
title and the legends for the two axis X and Y and to set the bar color as blue.
Finally convert the matplotlib graphics to a PNG graphics entitled salary.png and store
it on the same location as the Python program and the JSON-file.
"""
import json
import matplotlib.pyplot as plt

# Open the JSON file
file = open('salary.json', 'r')

# Load JSON content into a Python dictionary data={}
""" The json module automatically detects the JSON data type 
and converts it into the corresponding Python data type"""
data = json.load(file)

""" Explanation: format of data
data = {'employee': [{'name': 'Tom', 'salary': 50000}, {'name': 'Jim', 'salary': 10000}, 
{'name': 'Beth', 'salary': 100000}, {'name': 'Mark', 'salary': 60000}]}

The `data` dictionary has a key `'employee'` that is associated with a list of dictionaries. 
Each dictionary within the list represents an employee and contains keys like `'name'` and 
`'salary'`. So, you have a dictionary that contains a key pointing to a list, 
and each element of that list is a dictionary. This nested structure is quite common in 
JSON data where objects can contain arrays or other objects.
-> data is a dictionary with a key employee
-> employee is a list with different dictionaries
-> each dictionary has a key name and a key salary 
"""

# Extract names and salaries from the data into lists for the y and x axis
# with a for loop
name_list = []
salary_list = []
for i in data["employee"]:
    name_list.append(i["name"])
    salary_list.append(i["salary"])

# or with list comprehension
names = [employee['name'] for employee in data['employee']]
salaries = [employee['salary'] for employee in data['employee']]

""" Explanation: for loop
i represents each dictionary in the 'employee' list of the 'data' dictionary during 
each iteration of the loop. In this case, each i is a dictionary with keys "name" and "salary". 
By using i["name"] and i["salary"], you are accessing the values associated with these keys 
in each dictionary and appending them to the respective lists (name_list and salary_list).

-> i["name"]: Accesses the value associated with the key "name" in the current dictionary i.
-> i["salary"]: Accesses the value associated with the key "salary" in the current dictionary i.
"""
# Plotting the data
# create the bar plot, add the x-axis (names) and y-axis (salaries)
# and set the color of the bars to blue
plt.bar(names, salaries, color='blue')
plt.xlabel('Employee Names') # add the x-axis label
plt.ylabel('Salaries') # add the y-axis label
plt.title('Employee Salaries Overview') # add a title for the bar chart
plt.tight_layout() # Enforce optimal spacing to prevent overlapping of plot elements
plt.show() # show the bar chart

# saving it as png file
plt.savefig("salary.png")



