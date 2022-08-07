from module import Module

descriptionWords = ["complicated wires"]

class ComplicatedWiresModule(Module):
    def __init__(self, widgets):
        self.colors = {
            "white": 0,
            "red": 1,
            "blue": 2,
            "purple": 3,
            "both": 3
        }

        self.fromColors = {
            0: "white ",
            1: "red ",
            2: "blue ",
            3: "red and blue "
        }

        self.symbols = {
            "star": 1,
            "LED": 2,
            "light": 2,
            "lit": 2,
            "one": 2,
            "on": 2,
        }

        self.fromSymbols = {
            0: "none",
            1: "star",
            2: "L E D",
            3: "star and LED"
        }

        self.orderOfWires = []
        self.orderOfWireSymbols = []

        self.serial = widgets.getSerial()
        self.batteries = widgets.getBatteries()
        self.parallelPorts = widgets.getWidget("Parallel Port")

    def logic(self):
        speechOutput = ""

        if len(self.orderOfWires) == 0:
            speechOutput = "I didn't hear that correctly, please try again."
            return [-1, speechOutput] 

        for i in range(len(self.orderOfWires)):
            
            color = self.orderOfWires[i]
            symbol = self.orderOfWireSymbols[i]

            speechOutput += f"{self.fromColors[color]} "

            if symbol != 0:
                speechOutput += f"{self.fromSymbols[symbol]} "

            if symbol == 0:
                if color == 0:
                    speechOutput += " cut. "
                elif not self.__isSerialOdd():
                    speechOutput += " cut. "
                else:
                    speechOutput += " don't cut. "
            elif symbol == 1:
                if color == 0 or color == 1:
                    speechOutput += " cut. "
                elif color == 2:
                    speechOutput += " don't cut. "
                elif color == 3 and self.parallelPorts > 0:
                    speechOutput += " cut. "
                else:
                    speechOutput += " don't cut. "
            elif symbol == 2:
                if color == 0:
                    speechOutput += " don't cut. "
                elif color == 1 and self.batteries >= 2:
                    speechOutput += " cut. "
                elif color == 2 and self.parallelPorts > 0:
                    speechOutput += " cut. "
                elif color == 3 and not self.__isSerialOdd():
                    speechOutput += " cut. "
                else:
                    speechOutput += "don't cut. "
            elif symbol == 3:
                if (color == 0 or color == 1) and self.batteries >= 2:
                    speechOutput += " cut. "
                elif color == 2 and self.parallelPorts > 0:
                    speechOutput += " cut. "
                else:
                    speechOutput += " don't cut. "

        return [0, speechOutput]

    def __isSerialOdd(self):
        try:
            digit = int(self.serial[-1])
            print(digit)
            if digit % 2 == 1:
                return True
        except Exception as e:
            print(e)
            return False
        return False


    def solve(self, rawInput):
        color = -1
        symbol = 0

        for word in rawInput.split():
            if word in self.colors:
                if color == 0 or color == -1:
                    color = self.colors[word]
                elif color == 1 and self.colors[word] == 2:
                    color = 3
                elif color == 2 and self.colors[word] == 1:
                    color = 3

            if word in self.symbols:
                if symbol == 0:
                    symbol = self.symbols[word]
                elif symbol == 1 and self.symbols[word] == 2:
                    symbol = 3
                elif symbol == 2 and self.symbols[word] == 1:
                    symbol = 3

            if word == "next":

                if color == -1:
                    pass
                else:
                    self.orderOfWires.append(color)
                    self.orderOfWireSymbols.append(symbol)
                    color = -1
                    symbol = 0

        if color != -1:
            self.orderOfWires.append(color)
            self.orderOfWireSymbols.append(symbol)

        output = self.logic()
        return output