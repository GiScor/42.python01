def ft_plant_growth():
    class Plant:
        def __init__(self, name, height, d_old, factor):
            self.name = name
            self.height = height
            self.initial_height = height
            self.d_old = d_old
            self.factor = factor

        def show(self):
            print(self.name, ": ", self.height, "cm, ",
                  self.d_old, " days old", sep="")

        def grow(self):
            self.height += round(self.height * self.factor, 5)

        def age(self, days):
            for i in range(days):
                self.d_old += 1
                self.grow()

    print("======== Plant growth: ========")
    s = Plant('Sblurbo', 0.67, 1542, 0.025)
    s.show()
    for i in range(1, 8):
        print("=== Day", i, "===")
        s.age(1)
        print(s.name, ": ", round(s.height, 2), "cm, ",
              s.d_old, " days old", sep="")
    print("=== ", round(s.height - s.initial_height, 2),
          "cm gained this week ===", sep="")


if __name__ == "__main__":
    ft_plant_growth()
