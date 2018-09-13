############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

        self.pairings = []

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        # Fill in the rest
        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        # Fill in the rest
        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    # Fill in the rest
    muskmelon = MelonType("musk", 1998, "green", True, True, "Muskmelon")
    casaba = MelonType("cas", 2003, "orange", False, False, "Casaba")
    crenshaw = MelonType("cren", 1996, "green", False, False, "Crenshaw")
    yellow_watermelon = MelonType("yw", 2013, "yellow", False, True, "Yellow Watermelon")

    muskmelon.add_pairing("mint")
    casaba.add_pairing("strawberries")
    casaba.add_pairing("mint")
    crenshaw.add_pairing("proscuitto")
    yellow_watermelon.add_pairing("ice cream")

    all_melon_types.append(muskmelon)
    all_melon_types.append(casaba)
    all_melon_types.append(crenshaw)
    all_melon_types.append(yellow_watermelon)

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # Fill in the rest
    for melon in melon_types:
        print("")
        print(melon.name ,"pairs with" )
        for pairing in melon.pairings:
            print("-", pairing)

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest
    melon_dict = {}
    for melon in melon_types:
        melon_dict[melon.code] = melon
    return melon_dict

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def __init__(self, melon_type, shape_rating, color_rating, field, harvester):
        self.type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvester = harvester

    def is_sellable(self):
        return self.shape_rating > 5 and self.color_rating > 5 and self.field != 3

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    melon1 = Melon(melon_types[3], 8,7,2,"Sheila")
    melon2 = Melon(melon_types[3], 3,4,2,"Sheila")
    melon3 = Melon(melon_types[3], 9,8,3,"Sheila")
    melon4 = Melon(melon_types[1], 10,6,35,"Sheila")
    melon5 = Melon(melon_types[2], 8,9,35,"Michael")
    melon6 = Melon(melon_types[2], 8,2,35,"Michael")
    melon7 = Melon(melon_types[2], 2,3,4,"Michael")
    melon8 = Melon(melon_types[0], 6,7,4,"Michael")
    melon9 = Melon(melon_types[3], 7,10,3,"Sheila")

    melon_list = [melon1, melon2, melon3, melon4, melon5, melon6, melon7, melon8, melon9]
    return melon_list

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 
    for melon in melons:
        part_1 = "Harvested by {}, from Field {}".format(melon.harvester, melon.field)
        if melon.is_sellable():
            print(part_1 + " (CAN BE SOLD)")
        else:
            print(part_1 + " (NOT SELLABLE)")