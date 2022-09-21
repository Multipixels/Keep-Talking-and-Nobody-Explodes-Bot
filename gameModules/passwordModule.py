from turtle import speed
from module import Module

descriptionWords = ["password"]
isPersistent = False

class passwordModule(Module):
    def __init__(self, widgets):
        self.letters = []

        self.answers = ["about", "after", "again", "below", "could", "every", "first", "found", "great", "house", "large", "learn", "never", "other", "place", "plant", "point", "right", "small", "sound", "spell", "still", "study", "their", "there", "these", "thing", "think", "three", "water", "where", "which", "world", "would", "write"]


    def logic(self):
        speechOutput = ""

        answerCopy = self.answers[:]
        roundAnswers = []

        print(answerCopy)

        index = 0
        while index != 5 and len(self.letters) != index and len(self.letters[index]) > 0:
            for answer in answerCopy:
                if answer[index] in self.letters[index]:
                    roundAnswers.append(answer) 
            answerCopy = roundAnswers[:]
            roundAnswers = []
            print(answerCopy)
            index += 1

        if len(answerCopy) >= 1:
            speechOutput = "Try: "
            for word in answerCopy:
                speechOutput += f"{word}, "
            return [0, speechOutput]
        
        speechOutput = "Error: Can't find any words"
        return [-1, speechOutput]
        
        

    def solve(self, rawInput):
        temporaryLetterHold = []
        for word in rawInput.split():
            if word == "next":
                self.letters.append(temporaryLetterHold)
                temporaryLetterHold = []
                continue
            
            if word != "password":
                temporaryLetterHold.append(word[0])

        if len(temporaryLetterHold) != 0:
            self.letters.append(temporaryLetterHold)

        output = self.logic()
        return output