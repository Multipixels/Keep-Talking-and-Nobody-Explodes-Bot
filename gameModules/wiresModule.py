from typing import OrderedDict
from module import Module

class WiresModule(Module):
    def __init__(self):
        self.colors = ['red', 'yellow', 'blue', 'black', 'white']
        self.numberOfWires = 0
        self.orderOfWires = []

    def __logic(self):
        speechOutput = ""

        if self.numberOfWires <= 2 or self.numberOfWires >= 7:
            speechOutput = "I didn't hear that correctly, please try again."
            return [-1, speechOutput]

        for word in self.orderOfWires:
            speechOutput += word

        speechOutput += ". "

        if self.numberOfWires == 3:
            if self.orderOfWires[0] == "blue" and self.orderOfWires[1] == "blue" and self.orderOfWires[2] == "red":
                speechOutput += "Cut the second wire."
            elif "red" not in self.orderOfWires:
                speechOutput += "Cut the second wire."
            else:
                speechOutput += "Cut the third wire."
        
        
        
        
        
        
        
        return[0, speechOutput]

        


    def solve(self, rawInput):
        for word in rawInput.split():
            if word in self.colors():
                self.orderOfWires.append(word)
                self.numberOfWires += 1


        output = self.__logic()
        return output