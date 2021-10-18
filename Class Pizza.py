class Pizza:
    def __init__(self):
        self.size = 0
        self.toppings = []
        self.style = ""

    def add_topping(self, topping):
        self.toppings.append(topping)

    def format_toppings(self):
        topping_string = ""
        if len(self.toppings) > 1:
            for topping in self.toppings:
                if topping == self.toppings[-2]:
                    topping_string += f"{topping} and "
                elif topping == self.toppings[-1]:
                    topping_string += topping
                else:
                    topping_string += f"{topping}, "
        elif len(self.toppings) < 1:
            topping_string = "nothing on it"
        else:
            topping_string = self.toppings[0]
        return topping_string


    def print_order(self):
        toppings = self.format_toppings()
        if self.size < 1 or self.style == "":
            print("I have no clue what I want")
        else:
            print(f"I would like a {self.size}-inch, {self.style} pizza with {toppings}.")

meat_lovers = Pizza()
meat_lovers.size = 16
meat_lovers.style = "Deep dish"
meat_lovers.add_topping("Pepperoni")
meat_lovers.add_topping("Olives")
meat_lovers.print_order()