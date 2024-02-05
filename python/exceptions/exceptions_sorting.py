class WrongInnerTypeOfArray(Exception):

    def __str__(self):
        return "Your array contains not supported types. Available types: int, float, decimal, complex"
