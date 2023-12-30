# This program displays a simple line graph.
import matplotlib.pyplot as plt
def main():
    # Create lists with the X and Y coordinates of each data point.
    x_coords = [0, 1, 2, 3, 4]
    y_coords = [0, 3, 1, 5, 2]
    # Build the line graph.
    plt.plot(x_coords, y_coords)
    # change the lower and upper limits of the X and Y axes
    #plt.xlim(xmin=1, xmax=100)
    #plt.ylim(ymin=10, ymax=50)
    # customize each tick mark’s label
    plt.xticks([0, 1, 2, 3, 4], ['2016', '2017', '2018', '2019', '2020'])
    plt.yticks([0, 1, 2, 3, 4, 5], ['$0m', '$1m', '$2m', '$3m', '$4m', '$5m'])
    # Display the line graph.
    plt.show()

# Call the main function.
if __name__ == '__main__':
    main()