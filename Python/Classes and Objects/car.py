class Car:

    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("The "+self.model+" is being driven.")

    def stop(self):
        print("The "+self.model+" has stopped.")