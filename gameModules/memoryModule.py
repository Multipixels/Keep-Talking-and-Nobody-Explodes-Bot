from module import Module

descriptionWords = ["memory"]
isPersistent = True

class MemoryModule(Module):
    def __init__(self, widgets):
        self.numbers = {
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4
        }

        self.stages = [
            [],
            [],
            [],
            [],
            []
        ]

        self.answers = [
            [], #Position, Value
            [],
            [],
            [],
            []
        ]
        self.currentStage = 0

    def logic(self):
        speechOutput = ""

        if len(self.stages[self.currentStage]) != 5:
            speechOutput = "I didn't hear that correctly, please try again."
            return [-1, speechOutput]

        for word in self.stages[self.currentStage]:
            speechOutput += str(word) + " "

        speechOutput += ". "

        display = self.stages[self.currentStage][0]
        values = self.stages[self.currentStage][1:]
        
        press = -1

        print(self.stages, self.answers)

        if self.currentStage == 0:
            if display == 1:
                press = values[1]
            elif display == 2:
                press = values[1]
            elif display == 3:
                press = values[2]
            elif display == 4:
                press = values[3]
        elif self.currentStage == 1:
            if display == 1:
                press = 4
            elif display == 2:
                press = values[self.answers[0][0]]
            elif display == 3:
                press = values[0]
            elif display == 4:
                press = values[self.answers[0][0]]
        elif self.currentStage == 2:
            if display == 1:
                press = self.answers[1][1]
            elif display == 2:
                press = self.answers[0][1]
            elif display == 3:
                press = values[2]
            elif display == 4:
                press = 4
        elif self.currentStage == 3:
            if display == 1:
                press = values[self.answers[0][0]]
            elif display == 2:
                press = values[0]
            elif display == 3:
                press = values[self.answers[1][0]]
            elif display == 4:
                press = values[self.answers[1][0]]
        elif self.currentStage == 4:
            if display == 1:
                press = self.answers[0][1]
            elif display == 2:
                press = self.answers[1][1]
            elif display == 3:
                press = self.answers[3][1]
            elif display == 4:
                press = self.answers[2][1]

        position = values.index(press)
        self.answers[self.currentStage] = [position, press]

        speechOutput += f"Press {press}."
        return [0, speechOutput]

    def solve(self, rawInput):
        if "next" in rawInput:
            self.currentStage += 1

        if self.currentStage > 4:
            self.currentStage -= 1
            return [-1, "Cannot enter a 6th stage, resetting back to 5. Try again."]

        self.stages[self.currentStage] = []

        for word in rawInput.split():
            if word in self.numbers:
                self.stages[self.currentStage].append(self.numbers[word])

        output = self.logic()
        if output[0] == -1 and "next" in rawInput:
            self.currentStage -= 1
        return output

    def reset(self, widgets):
        self.__init__(widgets)