import os
import sys
from importlib import import_module
import gameModules
# from gameModules.wiresModule import WiresModule
# from gameModules.buttonModule import ButtonModule

#moduleList = []
for file in os.listdir(f"gameModules"):
    if file.endswith(".py") and file != '__init__.py':
        moduleName = file.split(".py")[0]
        import_module(f"gameModules.{moduleName}")
        #moduleList.append(moduleName)

#importlib.import_module(f"gameModules\{file}")
#import_module("gameModules.wiresModule")

#m = dir()
#print(m)
#print(moduleList)
#pkg = importlib.import_module('gameModules')

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
    'ten': '10',
    'zero' : '0'
}

modules = {
    #'complicated wires': ComplicatedWires(),
    #'simple wires': WiresModule,
    'wires': gameModules.wiresModule.WiresModule,
    'wire': gameModules.wiresModule.WiresModule,
    'simple button': gameModules.buttonModule.ButtonModule,
    'button': gameModules.buttonModule.ButtonModule
}

serialNumber = ""
numberOfBatteries = 0

def redirectInformation(input):
    if "serial" in input or "cereal" in input:
        return setSerial(input)
    elif "battery" in input:
        return setBatteries(input)
    else:
        for key in modules:
            if key in input:
                workModule = modules[key](serialNumber)
                return workModule.solve(input)
        return [-1, "Invalid input, please try again"]
        #res = [val for key, val in modules.items() if input in key]
        #if input in modules:
        #    print("it works")
        #else:
        #    print("no work")
        #print(res)
        #module = WiresModule(serialNumber)
        #return module.solve(input)
    #else:
        #return [-1, "Invalid input, please try again"]

#redirectInformation("wires red red red")

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

def setBatteries(input):
    global numberOfBatteries

    numberOfBatteries = -1
    speechOutput = ""

    modifiedInput = input.split()

    for word in modifiedInput:
        if word in numbers:
            numberOfBatteries = numbers[word]
            speechOutput = f"There are {numberOfBatteries} batteries."
            return [0, speechOutput]

    speechOutput = f"Invalid input, please try again."
    return [-1, speechOutput]