class ModuleManager:
    
    def __init__(self):
        self.numbers = {
            'one': '1',
            'two': '2',
            'three': '3',
            'four': '4',
            'five': '5',
            'six': '6',
            'seven': '7',
            'eight': '8',
            'nine': '9',
            'zero' : '0'
        }
        self.serialNumber = ""
    
    def redirectInformation(self, input):
        if "serial" in input or "cereal" in input:
            return self.setSerial(input)

    def setSerial(self, input):
        tempSerial = ""
        speechOutput = ""

        modifiedInput = input[input.find("is"):]
        modifiedInput = modifiedInput.split()

        if len(modifiedInput != 6):
            speechOutput = "Invalid input, please try again."
            return [-1, speechOutput]

        for word in modifiedInput:
            if word in self.numbers:
                tempSerial.append(self.numbers[word])
            else:
                tempSerial.append(word[0])

        self.serialNumber = tempSerial
        
        speechOutput = "Serial Number is {tempSerial}"
        return [0, speechOutput]