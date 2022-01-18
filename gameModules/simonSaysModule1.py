from module import Module

descriptionWords = ["wire sequence", "sequence wires", "sequence"]

class WireSequenceModule(Module):
    def __init__(self, serial="", labels={}, batteries=-0, strikes=0):
        self.colors = ['red', 'yellow', 'blue', 'green']

        self.orderOfColors = []

        self.strikes = strikes

    def logic(self):
        speechOutput = ""
        solution = []

        if self.orderOfColors == [] or self.strikes < 0:
            speechOutput = "Invalid input, please try again."
            return [-1, speechOutput]

        for color in self.orderOfColors:
            speechOutput += color + " "

        
        if self.strikes == 0:
            for color in self.orderOfColors:
                if color == "red":
                    solution += "blue "
                elif color == "blue":
                    solution += "red "
                elif color == "green":
                    solution += "yellow "
                elif color == "yellow":
                    solution += "green"
        elif self.strikes == 1:
            for color in self.orderOfColors:
                if color == "red":
                    solution += "yellow "
                elif color == "blue":
                    solution += "green "
                elif color == "green":
                    solution += "blue "
                elif color == "yellow":
                    solution += "red "
        elif self.strikes >= 2:
            for color in self.orderOfColors:
                if color == "red":
                    solution += "green "
                elif color == "blue":
                    solution += "Red "
                elif color == "green":
                    solution += "yellow "
                elif color == "yellow":
                    solution += "blue "

        speechOutput += ". Input "

        for color in solution:
            speechOutput += color

        return [0, speechOutput]


    def solve(self, rawInput):
        for word in rawInput.split():
            if word in self.colors:
                self.orderOfColors.append(word)

        return self.logic()