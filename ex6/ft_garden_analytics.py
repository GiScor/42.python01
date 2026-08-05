class Plant:
    def __init__(self, name: str, height: float, d_old: int, factor: float):
        self.stats = self.Stats(self)
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
        self.stats._show += 1
        print(self._name, ": ", round(self._height, 2), "cm, ",
              self._d_old, " days old", sep="", end=end)

    def grow(self):
        self.stats._grow += 1
        self._height += round(self._height * self._factor, 5)

    def age(self, days):
        self.stats._age += 1
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

    '''
    Create a class method that allows you to create an “anonymous” plant
    directly when you do not yet have all the information,
    WTF?????????
    '''
    @classmethod
    def anonym(cls):
        return cls("Unknown", 1, 1, .1)

    @staticmethod
    def year_old(days):
        if days >= 365:
            return(True)
        else:
            return(False)

    class Stats():
        def __init__(self, owner, grow=0, age=0, show=0):
            self._owner = owner
            self._grow = grow
            self._age = age
            self._show = show

        def display(self, end="\033[0m\n"):
            print("\033[0;36m"
                  f"=== Stats for {self._owner._name}"
                  f"\033[0;36m === ")
            print(f"> Grown {self._grow} time(s)")
            print(f"> Aged {self._age} time(s)")
            print(f"> Showed {self._show} time(s)", end=end)


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
        self.stats = self.Stats(self)
        self.stats._shade = 0
        self._diameter = trunk_diameter
        self._shading = False
        super().__init__(name, height, d_old, factor)

    def show(self):
        super().show(end=", ")
        print(f"{self._diameter}cm trunk")

    def produce_shade(self):
        self.stats._shade += 1
        if self._shading:
            print("Already producing shade, bruh!")
        else:
            print(f"[asking {self._name} to produce shade]")
            self._shading = True
            print(f"{self._name} is now producing a shade {self._height}cm"
                  f" long and {self._diameter}cm wide")

    class Stats(Plant.Stats):
        def __init__(self, owner, grow=0, age=0, show=0, shade=0):
            super().__init__(owner, grow=0, age=0, show=0)
            self._shade = shade

        def display(self):
            super().display(end="\n")
            print(f"> Produced shade {self._shade} time(s)\033[1;0m")


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


def ft_garden_analytics():
    print("=== Garden stats ===")
    print("=== Check year-old ===")
    print(f"Is {366} days more than a year? -> {Plant.year_old(366)}")
    print("=== Flower")
    a = Flower('Cazzus', 1, 366, 1, 'green')
    print(f"Grow {a._name} 1 time")
    a.grow()
    print(f"Age {a._name} 2 times")
    a.age(2)
    a.show()
    a.stats.display()
    b = Tree('Frondantonerzio', 199, 78901, 10, 500)
    b.produce_shade()
    b.age(3102)
    b.stats.display()
    c = Plant.anonym()
    c.show()


if __name__ == "__main__":
    ft_garden_analytics()
