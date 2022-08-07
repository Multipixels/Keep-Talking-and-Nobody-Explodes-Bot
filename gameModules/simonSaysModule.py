from module import Module

descriptionWords = ["simon", "salmon"]

class SimonSaysModule(Module):
    def __init__(self, widgets):
        self.colors = ['red', 'yellow', 'blue', 'green']

        self.orderOfColors = []

        self.strikes = widgets.getStrikes()
        self.serial = widgets.getSerial()
        self.vowel = False

    def logic(self):
        speechOutput = ""
        solution = []

        if self.orderOfColors == [] or self.strikes < 0:
            speechOutput = "Invalid input, please try again."
            return [-1, speechOutput]

        if self.serial == "":
            speechOutput = "I need the serial number, please try again."
            return [-1, speechOutput]

        for color in self.orderOfColors:
            speechOutput += color + " "
        
        if self.vowel:
            if self.strikes == 0:
                for color in self.orderOfColors:
                    if color == "red":
                        solution += "blue "
                    elif color == "blue":
                        solution += "red "
                    elif color == "green":
                        solution += "yellow "
                    elif color == "yellow":
                        solution += "green "
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
                        solution += "red "
                    elif color == "green":
                        solution += "yellow "
                    elif color == "yellow":
                        solution += "blue "
        else:
            if self.strikes == 0:
                for color in self.orderOfColors:
                    if color == "red":
                        solution += "blue "
                    elif color == "blue":
                        solution += "yellow "
                    elif color == "green":
                        solution += "green "
                    elif color == "yellow":
                        solution += "red "
            elif self.strikes == 1:
                for color in self.orderOfColors:
                    if color == "red":
                        solution += "red "
                    elif color == "blue":
                        solution += "blue "
                    elif color == "green":
                        solution += "yellow "
                    elif color == "yellow":
                        solution += "green "
            elif self.strikes >= 2:
                for color in self.orderOfColors:
                    if color == "red":
                        solution += "yellow "
                    elif color == "blue":
                        solution += "green "
                    elif color == "green":
                        solution += "blue "
                    elif color == "yellow":
                        solution += "red "

        speechOutput += ". Input "

        for color in solution:
            speechOutput += color

        return [0, speechOutput]


    def solve(self, rawInput):

        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        if any(char in vowels for char in self.serial):
            self.vowel = True

        for word in rawInput.split():
            if word in self.colors:
                self.orderOfColors.append(word)

        return self.logic()