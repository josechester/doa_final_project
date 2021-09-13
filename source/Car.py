class Car:
    is_new = True

    def __init__(self, model, year, colour):
        self.model = model
        self.year = year
        self.colour = colour
        self.mileage = 0

    def condition(self):
        if self.is_new:
            return "New"
        else:
            return "Used"

    def drive(self, distance):
        self.is_new = False
        self.mileage += distance

    def description(self):
        print("This %s was made in %s. It is %s and its condition is %s."
              % (self.model, self.year, self.colour, self.condition()))
