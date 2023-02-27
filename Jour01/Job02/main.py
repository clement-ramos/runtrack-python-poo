class Operation:

    def __init__(self):
        self.nombre1 = 12
        self.nombre2 = 3

    def print_numbers(self):
        print("Le nombre est " + str(self.nombre1))
        print("Le nombre est " + str(self.nombre2))

operation = Operation()

operation.print_numbers()