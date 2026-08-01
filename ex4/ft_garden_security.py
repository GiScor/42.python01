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
                  "Used default value (0)", "\n=============================" +
                  '\033[0m', end="\n")
            self._d_old = 0
        else:
            self._d_old = d_old
        print('\033[5m', "CREATED:", '\033[0m',
              sep='', end=" ")
        self.show()

    def show(self):
        print(self._name, ": ", round(self._height, 2), "cm, ",
              self._d_old, " days old", sep="")

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


def ft_garden_security():

    p1 = Plant('Cacchius', 22, 10, 0.1)
    p2 = Plant('Kruzmaltroniuz', 4, -1, 0.003)
    p1.set_height(10)
    p1.set_age(11)
    p2.set_height(-10)
    p1.set_age(-11)
    p1.show()
    p2.show()


if __name__ == "__main__":
    ft_garden_security()
