from module import Module

descriptionWords = ["keypad", "symbols"]
isPersistent = False

class KeypadModule(Module):
    def __init__(self, widgets):
        self.symbols = {
            "copyright": 1,
            "black star": 2,
            "filled star": 2,
            "white star": 3,
            "hollow star": 3,
            "smiley": 4,
            "smile": 4,
            "two k": 5,
            "double k": 5,
            "mirror k": 5,
            "mirrored k": 5,
            "omega": 6,
            "spider": 7,
            "squid knife": 7,
            "eye with mustache": 8,
            "eye mustache": 8,
            "pumpkin": 8,
            "cursive h": 9,
            "hook n": 9,
            "teepee": 10,
            "six": 11,
            "squiggly n": 12,
            "at": 13,
            "a t": 13,
            "a e": 14,
            "melted three": 15,
            "euro": 16,
            "circle": 17,
            "n with hat": 18,
            "backward n": 18,
            "backwards n": 18,
            "dragon": 19,
            "three with tail": 19,
            "alien three": 19,
            "question mark": 20,
            "paragraph": 21,
            "right c": 22,
            "forward c": 22,
            "regular c": 22,
            "backward c": 23,
            "left c": 23,
            "pitchfork": 24,
            "pitch fork": 24,
            "trident": 24,
            "tripod": 25,
            "cursive": 26,
            "loop": 26,
            "puzzle": 27,
            "tracks": 27,
            "balloon": 28,
            "o with tail": 28,
            "weird nose": 29,
            "weird a": 30,
            "upside downey": 30,
            "upside downy": 30,
            " t b ": 31,
            " b t ": 31,
            "b inside t": 31,
            "t inside b": 31
        }

        self.answers = (
            (28, 13, 30, 12, 7, 9, 23),
            (16, 28, 23, 26, 3, 9, 20),
            (1, 8, 26, 5, 15, 30, 3),
            (11, 21, 31, 7, 5, 20, 4),
            (24, 4, 31, 22, 21, 19, 2),
            (11, 16, 27, 14, 24, 18, 6)
        )

        self.inputKeypad = []
        self.inputKeypadNames = []

    def logic(self):
        speechOutput = "I heard: "

        if len(self.inputKeypad) == 0:
            speechOutput = "I didn't hear any symbols."
            return [-1, speechOutput]

        if len(self.inputKeypad) != 4:
            speechOutput = "I didn't hear that right. I only heard "
            for answer in self.inputKeypadNames:
                speechOutput += f"{answer}, "
            speechOutput += "."
            return [-1, speechOutput]

        for answer in self.inputKeypadNames:
            speechOutput += f"{answer}, " 
        speechOutput += ". "

        correctSet = -1

        for answer in self.answers:
            for input in self.inputKeypad:
                if input not in answer:
                    break
                if input == self.inputKeypad[-1]:
                    correctSet = answer

        if correctSet == -1:
            speechOutput = "Didn't find a solution."
            return [-1, speechOutput]

        speechOutput += "The order is: "     
        for symbol in correctSet:
            if symbol in self.inputKeypad:
                speechOutput += f"{self.inputKeypadNames[self.inputKeypad.index(symbol)]}, "

        return [0, speechOutput] 

    def solve(self, rawInput):
        for key in self.symbols:
            if key in rawInput and self.symbols[key] not in self.inputKeypad:
                self.inputKeypad.append(self.symbols[key])
                self.inputKeypadNames.append(key)

        output = self.logic()
        return output
                