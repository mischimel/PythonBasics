import json

import matplotlib.pyplot as plt

data: None


# Opening, loading and closing json file
def open_json():
    global data
    try:
        infile = open('salary.json', 'r')
        data = json.load(infile)
        print("Opening the json-file 'salary.json' successful")
    except IOError:
        print("Could not open the json-file 'salary.json' for reading")
    finally:
        infile.close()


# Generate plot with for loop generating a list
def plot():
    x_axis, y_axis = [], []
    for i in data["employee"]:
        x_axis.append(i["name"])
        y_axis.append(i["salary"])

        # Shorter alternative with list comprehension
    # xAxis = [i["name"] for i in data["employee"]]
    # yAxis = [i['salary'] for i in data["employee"]]

    plt.bar(x_axis, y_axis, color='blue')

    # Create plot legends
    plt.xlabel("Name")
    plt.ylabel("Salary")
    plt.title("Salary Overview")

    # Enforces padding
    plt.tight_layout()

    plt.show()


# Showing and saving it as jpg file
def save_as_png(my_plt):
    try:
        my_plt.savefig("salary.png")
        my_plt.show()

    except IOError:
        print("Could not save it to a png-file")


if __name__ == "__main__":
    open_json()
    plot()
    save_as_png(plt)
