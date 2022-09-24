from module import Module

descriptionWords = ["wire sequence", "sequence wires", "sequence"]
isPersistent = True

class WireSequenceModule(Module):
    def __init__(self, widgets):
        self.colors = ["red", "blue", "black"]
        
        self.redCuts = ["C", "B", "A", "A C", "B", "A C", "A B C", "A B", "B"]
        self.blueCuts = ["B", "A C", "B", "A", "B", "B C", "C", "A C", "A"]
        self.blackCuts = ["A B C", "A C", "B", "A C", "B", "B C", "A B", "C", "C"]

        self.stages = [
            [],
            [],
            [],
            []
        ]

        self.currentStage = 0

    def logic(self):
        speechOutput = ""

        if self.stages[self.currentStage] == []:
            speechOutput = "I didn't hear that correctly, please try again."
            return [-1, speechOutput]

        if len(self.stages[self.currentStage]) > 6 or len(self.stages[self.currentStage]) % 2 != 0:
            speechOutput = f"I didn't hear that correctly, please try again. {self.stages}"
            return [-1, speechOutput]

        for word in self.stages[self.currentStage]:
            speechOutput += word + " "
        
        speechOutput += ". "

        numberOfRed = 0
        numberOfBlue = 0
        numberOfBlack = 0

        for i in range(self.currentStage - 1):
            numberOfRed += self.stages[i].count("red")
            numberOfBlue += self.stages[i].count("blue")
            numberOfBlack += self.stages[i].count("black")

        for i in range(0, len(self.stages[self.currentStage]), 2):
            color = self.stages[self.currentStage][i]
            letter = self.stages[self.currentStage][i+1]
            if color == "red":
                if letter in self.redCuts[numberOfRed]:
                    speechOutput += "Cut. "
                else: speechOutput += "Don't cut. "
                numberOfRed += 1

            if color == "blue":
                if letter in self.blueCuts[numberOfBlue]:
                    speechOutput += "Cut. "
                else: speechOutput += "Don't cut. "
                numberOfBlue += 1

            if color == "black":
                if letter in self.blackCuts[numberOfBlack]:
                    speechOutput += "Cut. "
                else: speechOutput += "Don't cut. "
                numberOfBlack += 1
        
        return [0, speechOutput]

    def solve(self, rawInput):
        
        if "next" in rawInput:
            self.currentStage += 1

        nextLetter = False
        self.stages[self.currentStage] = []

        for word in rawInput.split():
            print(f"WA {word}")
            if nextLetter:
                if word[0].upper() in ["A", "B", "C"]:
                    self.stages[self.currentStage].append(word[0].upper())
                    nextLetter = False
                else: return [-1, "Didn't hear you correctly. Try again."]

            if word in self.colors:
                print(word)
                self.stages[self.currentStage].append(word)
                nextLetter = True

        output = self.logic()
        return output


    def reset(self, widgets):
        print("test")
        self.__init__(widgets)