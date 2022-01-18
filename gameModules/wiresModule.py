from module import Module

descriptionWords = ["simple wires", "wires", "wire"]

class WiresModule(Module):
    def __init__(self, serial="", labels={}, batteries=0, strikes=0):
        self.colors = ['red', 'yellow', 'blue', 'black', 'white']

        self.orderOfWires = []
        self.numberOfWires = 0
        self.numberOfRed = 0
        self.numberOfBlue = 0
        self.numberOfYellow = 0
        self.numberOfBlack = 0
        self.numberOfWhite = 0

        self.serial = serial

    def logic(self):
        speechOutput = ""

        if self.serial == "" and self.numberOfWires != 3:
            speechOutput = "I need the serial number."
            return [-1, speechOutput]

        if self.numberOfWires <= 2 or self.numberOfWires >= 7:
            speechOutput = "I didn't hear that correctly, please try again."
            return [-1, speechOutput]

        for word in self.orderOfWires:
            speechOutput += word + " "

        speechOutput += ". "

        if self.numberOfWires == 3:
            if self.orderOfWires[0] == "blue" and self.orderOfWires[1] == "blue" and self.orderOfWires[2] == "red":
                speechOutput += "Cut the second wire."
            elif "red" not in self.orderOfWires:
                speechOutput += "Cut the second wire."
            else:
                speechOutput += "Cut the third wire."
        
        elif self.numberOfWires == 4:
            if self.numberOfRed >= 2 and self.__isSerialOdd():
                speechOutput += "Cut the last red wire."
            elif self.numberOfRed == 0 and self.orderOfWires[-1] == "yellow":
                speechOutput += "Cut the first wire."
            elif self.numberOfBlue == 1:
                speechOutput += "Cut the first wire."
            elif self.numberOfYellow >= 2:
                speechOutput += "Cut the fourth wire."
            else:
                speechOutput += "Cut the second wire."

        elif self.numberOfWires == 5:
            if self.orderOfWires[-1] == "black" and self.__isSerialOdd():
                speechOutput += "Cut the fourth wire."
            elif self.numberOfRed == 1 and self.numberOfYellow >= 2:
                speechOutput += "Cut the first wire."
            elif self.numberOfBlack == 0:
                speechOutput += "Cut the second wire."
            else:
                speechOutput += "Cut the first wire."
        elif self.numberOfWires == 6:
            if self.numberOfYellow == 0 and self.__isSerialOdd():
                speechOutput += "Cut the third wire."
            elif self.numberOfYellow == 1 and self.numberOfWhite >= 2:
                speechOutput += "Cut the fourth wire."
            elif self.numberOfRed == 0:
                speechOutput += "Cut the sixth wire."
            else:
                speechOutput += "Cut the fourth wire"

        return[0, speechOutput]

    def __isSerialOdd(self):
        try:
            digit = int(self.serial[-2])
            print(digit)
            if digit % 2 == 1:
                return True
        except Exception as e:
            print(e)
            return False
        return False

    def solve(self, rawInput):
        for word in rawInput.split():
            if word in self.colors:
                self.orderOfWires.append(word)
                self.numberOfWires += 1

                if word == "red":
                    self.numberOfRed += 1
                elif word == "blue":
                    self.numberOfBlue += 1
                elif word == "yellow":
                    self.numberOfYellow += 1
                elif word == "black":
                    self.numberOfBlack += 1
                elif word == "white":
                    self.numberOfWhite += 1

        output = self.logic()
        return output