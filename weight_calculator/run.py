class Calculator:
    def __init__(self):
        self.selection = None
        self.toConvert = None

    def poundsToKg(self, toConvert: float) -> None:
        print(f"Your weight in kg is {round(toConvert * float(0.454))}")

    def kgToPounds(self, toConvert: float) -> None:
        print(f"Your weight in pounds is {(round(toConvert * float(2.205)))}")

    def selectConversion(self):
        print("Calculator:")
        print("1. Pounds to kg")
        print("2. Kg to pounds")
        self.selection = input("Please select a number: ")

    def convert(self):
        while True:
            try:
                if(self.selection == str(1)):
                    self.toConvert = float(input("Enter your weight in pounds: "))
                    self.poundsToKg(self.toConvert)
                    break
                elif(self.selection == str(2)):
                    self.toConvert = float(input("Enter your weight in kg: "))
                    self.kgToPounds(self.toConvert)
                    break
            except ValueError:
                print("Not a valid input! Please select an option by inputting the digit.")

if __name__ == "__main__":
    calculator = Calculator()
    calculator.selectConversion()
    calculator.convert()
