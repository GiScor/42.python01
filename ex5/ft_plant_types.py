class Plant:
    def __init__(self, name, height, d_old, factor):
        self._name = name
        self._factor = factor
        if height < 0:
            print('\033[91m' + "============ERROR============\n",
                  "Height can't be negative.\n",
                  "Used default value (0.1)", "\n============================="
                  + '\033[0m', end="\n")
            self._height = 0.1
            self._initial_height = 0.1
        else:
            self._height = height
            self._initial_height = height
            if d_old < 0:
                print('\033[91m' + "============ERROR============\n",
                      "Age can't be negative.\n",
                      "Used default value (0)",
                      "\n=============================" +
                      '\033[0m', end="\n")
                self._d_old = 0
            else:
                self._d_old = d_old
                print('\033[5m', "CREATED:", '\033[0m',
                      sep='', end=" ")
                self.show()

    def show(self, end="\n"):
        print(self._name, ": ", round(self._height, 2), "cm, ",
              self._d_old, " days old", sep="", end=end)

    def grow(self):
        self._height += round(self._height * self._factor, 5)

    def age(self, days):
        if days < 0:
            print("Error: cannot age negative days")
        else:
            for i in range(days):
                self._d_old += 1
                self.grow()

    def set_height(self, height):
        if height < 0:
            print('\033[91m' + "========UPDATE ERROR=========\n",
                  "PLANT: ", '\033[93m' + self._name + '\033[91m', '\n',
                  '\033[1m', height, '\033[0m' + '\033[91m' +
                  " is invalid.\nHeight can't be a negative value"
                  "\n=============================" + '\033[0m',
                  sep="", end="\n")
        else:
            self._height = height
            print(self._name, ": ", "Height updated: ",
                  self._height, "cm", sep="")

    def set_age(self, d_old):
        if d_old < 0:
            print('\033[91m' + "========UPDATE ERROR=========\n",
                  "PLANT: ", '\033[93m' + self._name + '\033[91m', "\n",
                  '\033[1m', d_old, '\033[0m' + '\033[91m' +
                  " is invalid.\nAge can't be a negative value"
                  "\n=============================" + '\033[0m',
                  sep="", end="\n")
        else:
            self._d_old = d_old
            print(self._name, ": ", "Age updated: ",
                  self._d_old, " days", sep="")

    def get_height(self):
        print(self._name, ": ", "Height: ", self._height, "cm", sep="")

    def get_age(self, d_old):
        print(self._name, ": ", "Age: ", self._d_old, " days", sep="")


class Flower(Plant):
    allowed_colors = ["red", "blue", "green", "yellow",
                      "orange", "purple", "pink", "brown",
                      "black", "white", "gray"]
    def __init__(self, name, height, d_old, factor, color):
        if color not in self.allowed_colors:
            print('\033[91m' + "============ERROR============\n",
                  "Invalid color: " + '\033[0m' + "<", color, ">" + '\033[91m',
                  "\nUsed default color (\"red\")",
                  "\n============================="
                  + '\033[0m', sep="", end="\n")
            self._color = "red"
        else:
            self._color = color
        super().__init__(name, height, d_old, factor)

    def show(self):
        super().show(end=", ")
        print(self._color)

    def set_color(self, color):
        if color not in self.allowed_colors:
            print('\033[91m' + "============ERROR============\n",
                  "Invalid color: " + '\033[0m' + "<", color, ">" + '\033[91m',
                  "\nUsed default color (\"red\")",
                  "\n============================="
                  + '\033[0m', sep="", end="\n")
            self._color = "red"
            print(self._name, ": ", "Color updated: ",
                  self._color, sep="")
        else:
            self._color = color
            print(self._name, ": ", "Color updated: ",
                  self._color, " days", sep="")


class Colors:
    """ ANSI color codes """
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    LIGHT_WHITE = "\033[1;37m"
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    END = "\033[0m"


def ft_plant_types():
    a = Flower("fiorellino", 10, 10, 0.01, "cacca")
    a.set_height(11)
    a.set_color("sborra")
    a.show()


if __name__ == "__main__":
    ft_plant_types()
