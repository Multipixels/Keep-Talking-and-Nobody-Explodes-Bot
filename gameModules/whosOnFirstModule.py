from module import Module

descriptionWords = ["who's on first", "whose on first", "whos on first"]

class WhosOnFirstModule(Module):
    def __init__(self, widgets):
        self.first = {
            "literally blank": " ",
            "literally nothing": " ",
            "empty": " ",
            "blank word": "blank",
            "b l a n k": "blank",
            "c letter": "c",
            "see letter": "c",
            "sea letter": "c",
            "c word with c": "cee",
            "sea word with c": "cee",
            "see word with c": "cee",
            "c word with sea": "cee",
            "c word with see": "cee",
            "see word with sea": "cee",
            "sea word with sea": "cee",
            "c e e": "cee",
            "sea e e": "cee",
            "see e e": "cee",
            "display": "display",
            "first": "first",
            "hold on": "hold on",
            "follow the lead": "lead",
            "l e a d": "lead",
            "pencil": "lead",
            "l e d": "led",
            "light": "led",
            "tv": "led",
            "leed": "leed",
            "l e d with two e": "leed",
            "lead with two e": "leed",
            "no ": "no",
            " no": "no",
            "nothing word": "nothing",
            "okay": "okay",
            "ok ": "okay",
            " ok": "okay",
            "read book": "read",
            "reed book": "read",
            "red color": "red",
            "read color": "red",
            "reed mouth": "reed",
            "read mouth": "reed",
            "read instrument": "reed",
            "reed instrument": "reed",
            "reed rod": "reed",
            "read rod": "reed",
            "says": "says",
            "see word": "see",
            "c word": "see",
            "sea word": "see",
            "their possessive": "their",
            "there possessive": "their",
            "they're possessive": "their",
            "they are possessive": "their",
            "their place": "there",
            "there place": "there",
            "they're place": "there",
            "they are place": "there",
            "their seperate": "they are",
            "there seperate": "they are",
            "they're seperate": "they are",
            "they are seperate": "they are",
            "their conjunction": "they're",
            "there conjunction": "they're",
            "they're conjunction": "they're",
            "they are conjunction": "they're",
            "u r letter": "ur",
            "you r letter": "ur",
            "you are letter": "ur",
            "u are letter": "ur",
            "u r later": "ur",
            "you r later": "ur",
            "you are later": "ur",
            "u are later": "ur",
            "yes": "yes",
            "you are seperate": "you are",
            "you're seperate": "you are",
            "your seperate": "you are",
            "you are conjugate": "you're",
            "you're conjugate": "you are",
            "your conjugate": "you are",
            "you are possessive": "you're",
            "you're possessive": "you are",
            "your possessive": "you are",
            "you word": "you",
            "you ": "you",
            " you": "you",
            "u ": "you"
        }

        self.second = {
            "blank": "blank",
            "b l a n k": "blank",
            "blank": "blank",
            "done": "done",
            "first": "first",
            "hold": "hold",
            "left": "left",
            "like": "like",
            "middle": "middle",
            "next": "next",
            "no ": "no",
            " no": "no",
            "nothing": "nothing",
            "ok": "okay",
            "press": "press",
            "ready": "ready",
            "sure": "sure",
            "you letter": "u",
            "u letter": "u",
            "two three": "uh huh",
            "two two": "uh uh",
            "four": "uhhh",
            "u r letter": "ur",
            "you r letter": "ur",
            "u are letter": "ur",
            "you are letter": "ur",
            "wait": "wait",
            "what": "what",
            "what question": "what?",
            "yes": "yes",
            "you are seperate": "you are",
            "you're seperate": "you are",
            "your seperate": "you are",
            "you are conjugate": "you're",
            "you're conjugate": "you are",
            "your conjugate": "you are",
            "you are possessive": "you're",
            "you're possessive": "you are",
            "your possessive": "you are",
            "you word": "you",
            "you": "you",
            "u ": "you"

        }

        self.firstToDirection = {
            " ": "bottom left",
            "blank": "middle right",
            "c": "top left",
            "cee": "bottom right",
            "display": "bottom right",
            "first": "top right",
            "hold on": "bottom right",
            "lead": "bottom right",
            "led": "middle left",
            "leed": "bottom left",
            "no": "bottom right",
            "nothing": "middle left",
            "okay": "top right",
            "read": "middle right",
            "red": "middle right",
            "reed": "bottom left",
            "says": "bottom right",
            "see": "bottom right",
            "their": "middle right",
            "there": "bottom right",
            "they are": "middle left",
            "they're": "bottom left",
            "ur": "top left",
            "yes": "middle left",
            "you": "middle right",
            "you are": "bottom right",
            "you're": "middle right",
            "your": "middle right"
        }

        self.secondToList = {
            "blank": ["wait", "right", "okay", "middle", "blank"],
            "done": ["sure", "uh huh", "next", "what?", "your", "ur", "you're", "hold", "like", "you", "u", "you are", "uh uh", "done"],
            "first": ["left", "okay", "yes", "middle", "no", "right", "nothing", "uhhh", "wait", "ready", "blank", "what", "press", "first"],
            "hold": ["you are", "u", "done", "uh uh", "you", "ur", "sure", "what?", "you're", "next", "hold"],
            "left": ["right", "left"],
            "like": ["you're", "next", "u", "ur", "hold", "done", "uh uh", "what?", "uh huh", "you", "like"],
            "middle": ["blank", "ready", "okay", "what", "nothing", "press", "no", "wait", "left", "middle"],
            "next": ["what?", "uh huh", "uh uh", "your", "hold", "sure", "next"],
            "no": ["blank", "uhhh", "wait", "first", "what", "ready", "right", "yes", "nothing", "left", "press", "okay", "no"],
            "nothing": ["uhhh", "right", "okay", "middle", "yes", "blank", "no", "press", "left", "what", "wait", "first", "nothing"],
            "okay": ["middle", "no", "first", "yes", "uhhh", "nothing", "wait", "okay"],
            "press": ["right", "mimddle", "yes", "ready", "press"],
            "ready": ["yes", "okay", "what", "middle", "left", "press", "right", "blank", "ready"],
            "right": ["yes", "nothing", "ready", "press", "no", "wait", "what", "right"],
            "sure": ["you are", "done", "like", "you're", "you", "hold", "uh huh", "ur", "sure"],
            "u": ["uh huh", "sure", "next", "what?", "you're", "ur", "uh uh", "done", "u"],
            "uh huh": ["uh huh"],
            "uh uh": ["ur", "u", "you are", "you're", "next", "uh uh"],
            "uhhh": ["ready", "nothing", "left", "what", "okay", "yes", "right", "no", "press", "blank", "uhhh"],
            "ur": ["done", "u", "ur"],
            "wait": ["uhhh", "no", "blank", "okay", "yes", "left", "first", "press", "what", "wait"],
            "what": ["uhhh", "what"],
            "what?": ["you", "hold", "you're", "your", "u", "done", "uh uh", "like", "you are", "uh huh", "ur", "next", "what?"],
            "yes": ["okay", "right", "uhhh", "middle", "first", "what", "press", "ready", "nothing", "yes"],
            "you are": ["your", "next", "like", "uh huh", "what", "done", "uh uh", "hold", "you", "u", "you're", "sure", "ur", "you are"],
            "you": ["sure", "you are", "your", "you're", "next", "uh huh", "ur", "hold", "what?", "you"],
            "your": ["uh uh", "you are", "uh huh", "your"],
            "you're": ["you", "you're"]   
        }

        self.step = 0
        self.input = ""

    def logic(self):
        speechOutput = ""

        if self.input == "":
            speechOutput = "Sorry, I didn't hear that."
            return [-1, speechOutput]
        
        if self.step == 1:
            speechOutput = f"I heard {self.input}, {self.firstToDirection[self.input]}"
            return [0, speechOutput]

        if self.step == 2:
            speechOutput = f"I heard {self.input}, "
            for word in self.secondToList[self.input]:
                speechOutput += f"{word}, "
            return [0, speechOutput]

        speechOutput = "Sorry, I didn't hear that."
        return [-1, speechOutput]


    def solve(self, rawInput):

        firstCounter = 0
        if "second" in rawInput:
            self.step = 2
            for key in self.second:
                if key in rawInput:
                    self.input = self.second[key]
                    break
        else:
            self.step = 1
            for key in self.first:
                if key in rawInput:
                    if self.first[key] == "first" and firstCounter == 0:
                        firstCounter += 1
                    else:
                        self.input = self.first[key]
                        break

        output = self.logic()
        return output