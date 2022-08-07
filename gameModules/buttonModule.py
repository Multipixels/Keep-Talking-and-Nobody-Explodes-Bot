from module import Module

descriptionWords = ["simple button", "button"]

class ButtonModule(Module):
    def __init__(self, widgets):
        self.colors = ['red', 'yellow', 'blue', 'white', 'black']
        self.texts = ['press', 'hold', 'detonate', 'abort']

        self.buttonColor = ""
        self.buttonText = ""
        self.buttonLight = ""

        self.labels = widgets.getLabels()
        self.batteries = widgets.getBatteries()

    def logic(self):

        speechOutput = ""

        if self.buttonLight != "":
            speechOutput = f"Button {self.buttonLight} light. "

            if self.buttonLight == "blue":
                speechOutput += "Hold until there's a four on the timer. "
            elif self.buttonLight == "yellow":
                speechOutput += "Hold until there's a five on the timer. "
            else:
                speechOutput += "Hold until there's a one on the timer. "
        else:
            if self.buttonColor == "red" and self.buttonText == "hold":
                speechOutput += "Tap the button. "
            elif self.batteries >= 2 and self.buttonText == "detonate":
                speechOutput += "Tap the button. "
            elif self.buttonColor == "blue" and self.buttonText == "abort":
                speechOutput += "Hold the button. "
            elif self.buttonColor == 'white' and self.labels['car'] == 1:
                speechOutput += "Hold the button. "
            elif self.batteries == 3 and self.labels['frk'] == 1:
                speechOutput += "Tap the button. "
            else:
                speechOutput += "Hold the button. "

        return [0, speechOutput]


    def solve(self, rawInput):
        modifiedInput = rawInput.split()

        if 'light' in rawInput:
            for word in modifiedInput:
                if word in self.colors:
                    self.buttonLight = word
        else:
            for word in modifiedInput:
                if word in self.colors:
                    self.buttonColor = word
                elif word in self.texts:
                    self.buttonText = word

        output = self.logic()
        return output