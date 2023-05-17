class NewClass():
    Attribute = 3

    def __init__(self, number=5) -> None:
        self.mynumber = number

    def GetNumber(self):
        return self.mynumber


myclass = NewClass()

print(f"class attribute = {myclass.Attribute}")
print(f"class method {myclass.GetNumber()}")
