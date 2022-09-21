from module import Module

descriptionWords = ["morse", "binary"]
isPersistent = False

class morseModule(Module):
    def __init__(self, widgets):
        self.words = {
            'dot': '.',
            'short': '.',
            'zero': '.',
            'dash': '-',
            'long': '-',
            'one': '-'
        }

        self.repeat = ""
        self.pattern = []

    def logic(self):
        speechOutput = self.repeat

        try:
            if self.pattern[0] == "...-":
                speechOutput += "3 dot 5 9 5."
            elif self.pattern[0] == "-":
                speechOutput += "3 dot 5 3 2."
            elif self.pattern[0] == ".-..":
                speechOutput += "3 dot 5 4 2."
            elif self.pattern[0] == "....":
                speechOutput += "3 dot 5 1 5."
            elif self.pattern[0] == "..-.":
                speechOutput += "3 dot 5 5 5."
            elif self.pattern[1] == '....':
                speechOutput += "3 dot 5 0 5."
            elif self.pattern[1] == '.-..':
                speechOutput += "3 dot 5 2 2."
            elif self.pattern[1] == '.':
                speechOutput += "3 dot 6 0 0."
            elif self.pattern[1] == '..':
                speechOutput += "3 dot 5 5 2."
            elif self.pattern[2] == '--':
                speechOutput += "3 dot 5 6 5."
            elif self.pattern[2] == '-..-':
                speechOutput += "3 dot 5 3 5."
            elif self.pattern[2] == '.-.':
                speechOutput += "3 dot 5 4 5."
            elif self.pattern[1] == '.-.' and self.pattern[2] == '.':
                speechOutput += "3 dot 5 7 2."
            elif self.pattern[1] == '.-.' and self.pattern[2] == '..':
                speechOutput += "3 dot 5 7 5."
            elif self.pattern[1] == '-' and self.pattern[2] == '.':
                speechOutput += "3 dot 5 8 2."
            elif self.pattern[1] == '-' and self.pattern[2] == '..':
                speechOutput += "3 dot 5 9 2."
            else:
                speechOutput == "Invalid input, please try again."
                return [-1, speechOutput]
        except:
            speechOutput == "Invalid input, please try again."
            return [-1, speechOutput]

        return [0, speechOutput]

    def solve(self, rawInput):

        tempStr = ""
        tempRepeat = ""

        for word in rawInput.split():
            if word in self.words:
                tempStr += self.words[word]
                tempRepeat += word + ","
            elif word == "next":
                tempRepeat += " next, "
                self.pattern.append(tempStr)
                tempStr = ""

        self.pattern.append(tempStr)

        tempRepeat += " end. "
        self.repeat = tempRepeat

        return self.logic()