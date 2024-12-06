import matplotlib.pyplot as plt

def read_file():
    with open("DS6.txt") as f:
        coordinates = f.readlines()
    return coordinates

def int_coordinates(coordinates):
    for i in range(len(coordinates)):
        coordinates[i] = coordinates[i].split()
        coordinates[i][0] = int(coordinates[i][0])
        coordinates[i][1] = int(coordinates[i][1])
        coordinates[i] = tuple(coordinates[i])
    return coordinates

def get_coordinates():
    return int_coordinates(read_file()) 

def draw(coordinates):
    x, y = zip(*coordinates)
    plt.figure(figsize=(9.6, 5.4)) 
    plt.xlabel("Y-axis|")
    plt.ylabel("X-axis")
    plt.scatter(y, x, color="red", marker="o", label="Coordinates from DS6")
    plt.savefig("picture.png", dpi=100)
    plt.show()


def main():
    coordinates = get_coordinates()
    draw(coordinates)

if __name__ == "__main__":
    main()