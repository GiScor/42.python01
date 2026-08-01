def ft_garden_data():
    class Plant:
        def __init__(self, name, height, age):
            self.name = name
            self.height = height
            self.age = age

        def show(self):
            print(self.name, ": ", self.height, "cm, ",
                  self.age, " days old", sep="")

    print("=============== Garden info: ===============")
    coprino = Plant('Coprinopsis atramentaria', 670, 15)
    coprino.show()
    sblurbo = Plant('Sblurbo', 0.67, 1542)
    sblurbo.show()
    cactus = Plant('Metacactus', 142, '∞')
    cactus.show()


if __name__ == "__main__":
    ft_garden_data()
