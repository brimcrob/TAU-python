# Parent class 1

class Item():
    def __init__(self,sku):
        self.sku = sku

    def print_sku(self):
        print("The sku is {}.".format(self.sku))

# Prarent Class 2
class Garment():
    def __init__(self,section, type):
        self.section = section
        self.type = type

    def print_garment(self):
        print("This garment is in section {}, {}.".format(self.section, self.type))


class Shirts(Item, Garment):
    def __init__(self, sku, section, type, name, colour):
        self.name = name
        self.colour = colour


        Item.__init__(self, sku)
        Garment.__init__(self, section, type)

    def print_shirt(self):
        print("{} {} on sale!".format(self.colour, self.name))


Blouse = Shirts("00001", 43, "Tops", "Formal Blouse", "White")

Blouse.print_sku()
Blouse.print_garment()
Blouse.print_shirt()
