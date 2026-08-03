class Plant:
    def __init__(self, name: str, height: float, d_old: int, factor: float):
        self._name = "\033[0;32m" + name + "\033[0m"
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
        self._bloomed = False
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
        super().show()
        print(f" Color: {self._color}")
        if self._bloomed:
            print(f" {self._name} is blooming!")
        else:
            print(f" {self._name} has not bloomed yet.")

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
                  self._color, sep="")

    def bloom(self):
        if not self._bloomed:
            print(f"[asking {self._name} to bloom]")
            self._bloomed = True
        else:
            print("Already blooming!")


class Tree(Plant):
    def __init__(self, name, height, d_old, factor, trunk_diameter):
        self._diameter = trunk_diameter
        self._shading = False
        super().__init__(name, height, d_old, factor)

    def show(self):
        super().show(end=", ")
        print(f"{self._diameter}cm trunk")

    def produce_shade(self):
        if self._shading:
            print("Already producing shade, bruh!")
        else:
            print(f"[asking {self._name} to produce shade]")
            self._shading = True
            print(f"{self._name} is now producing a shade {self._height}cm"
                  f" long and {self._diameter}cm wide")


class Vegetable(Plant):
    def __init__(self, name, height, d_old, factor,
                 harvest_season, nutritional_value):
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value
        super().__init__(name, height, d_old, factor)

    def show(self):
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {self._nutritional_value}")

    def grow(self):
        super().grow()
        self._nutritional_value += 1

# class Colors:
    # """ ANSI color codes """
    # BLACK = "\033[0;30m"
    # RED = "\033[0;31m"
    # GREEN = "\033[0;32m"
    # BROWN = "\033[0;33m"
    # BLUE = "\033[0;34m"
    # PURPLE = "\033[0;35m"
    # CYAN = "\033[0;36m"
    # LIGHT_GRAY = "\033[0;37m"
    # DARK_GRAY = "\033[1;30m"
    # LIGHT_RED = "\033[1;31m"
    # LIGHT_GREEN = "\033[1;32m"
    # YELLOW = "\033[1;33m"
    # LIGHT_BLUE = "\033[1;34m"
    # LIGHT_PURPLE = "\033[1;35m"
    # LIGHT_CYAN = "\033[1;36m"
    # LIGHT_WHITE = "\033[1;37m"
    # BOLD = "\033[1m"
    # FAINT = "\033[2m"
    # ITALIC = "\033[3m"
    # UNDERLINE = "\033[4m"
    # BLINK = "\033[5m"
    # NEGATIVE = "\033[7m"
    # CROSSED = "\033[9m"
    # END = "\033[0m"


def ft_plant_types():
    print("=== Garden Plant Types ===")
    print("=== Flower")
    a = Flower("Fiorellino", 10.0, 10, 0.01, "cacca")
    a.set_height(11)
    a.set_color("sborra")
    a.set_color("blue")
    a.bloom()
    a.show()
    print("=== Tree")
    b = Tree("Bruntallo", 300.0, 493, 0.1, 150.0)
    b.show()
    b.produce_shade()
    print("=== Vegetable")
    c = Vegetable("Groccolo", 8.0, 21, 0.1, "October", 0)
    print(f"[Make {c._name} grow for 20 days]")
    c.age(20)
    c.show()


if __name__ == "__main__":
    ft_plant_types()
