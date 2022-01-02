from gameModules import *
from gameModules.wiresModule import WiresModule

numbers = {
    'one': '1',
    'two': '2',
    'too': '2',
    'three': '3',
    'for' : "4",
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero' : '0'
}

serialNumber = ""

def redirectInformation(input):
    if "serial" in input or "cereal" in input:
        return setSerial(input)
    elif "wire" in input:
        print(serialNumber)
        module = WiresModule(serialNumber)
        return module.solve(input)
    else:
        return [-1, "Invalid input, please try again"]

def setSerial(input):
    global serialNumber

    tempSerial = ""
    speechOutput = ""

    modifiedInput = input.split(' is ')[-1]
    modifiedInput = modifiedInput.split()

    if len(modifiedInput) != 6:
        speechOutput = "Invalid input, please try again."
        return [-1, speechOutput]

    for word in modifiedInput:
        if word in numbers:
            tempSerial += numbers[word] + " "
        else:
            tempSerial += word[0] + " "

    serialNumber = tempSerial
    
    speechOutput = f"Serial Number is {tempSerial}"
    return [0, speechOutput]