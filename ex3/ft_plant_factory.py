class Plant:
    def __init__(self, name, height, d_old, factor):
        self.name = name
        self.height = height
        self.initial_height = height
        self.d_old = d_old
        self.factor = factor
        # print("Created:", end=" ")
        # self.show()

    def show(self):
        print(self.name, ": ", self.height, "cm, ",
              self.d_old, " days old", sep="")

    def grow(self):
        self.height += round(self.height * self.factor, 5)

    def age(self, days):
        for i in range(days):
            self.d_old += 1
            self.grow()


def ft_plant_factory():
    print("======== Plant laboratory output: ========")
    a = Plant('Sblurbo', 0.67, 1542, 0.025)
    print("Created:", end=" ")
    a.show()
    b = Plant('Franco', 84, 42, 0.2)
    print("Created:", end=" ")
    b.show()
    c = Plant('X-1', 180, 312, 0.1)
    print("Created:", end=" ")
    c.show()
    d = Plant('Money Tree', 9.99, 7, 0.09)
    print("Created:", end=" ")
    d.show()
    e = Plant('Bulbasaur', 70, 197, 0.005)
    print("Created:", end=" ")
    e.show()


if __name__ == "__main__":
    ft_plant_factory()
