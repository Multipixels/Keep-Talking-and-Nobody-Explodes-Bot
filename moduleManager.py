import os
import sys
import inspect
from importlib import import_module
import gameModules

moduleDescriptions = {

}

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

serialNumber = ""
numberOfBatteries = 0
numberOfStrikes = 0

labels = {
    'snd': -1,
    'clr': -1,
    'car': -1,
    'ind': -1,
    'frq': -1,
    'sig': -1,
    'nsa': -1,
    'msa': -1,
    'trn': -1,
    'bob': -1,
    'frk': -1
}

for file in os.listdir(f"gameModules"):
    if file.endswith(".py") and file != '__init__.py':
        moduleName = file.split(".py")[0]
        module = import_module(f"gameModules.{moduleName}")

        moduleClasses = inspect.getmembers(module, inspect.isclass)
        moduleClasses = [x for x in moduleClasses if x[0] != 'Module']

        descriptionWords = getattr(module, 'descriptionWords')
        for description in descriptionWords:
            moduleDescriptions[description] = moduleClasses[0][1]

def redirectInformation(input):
    if "serial" in input or "cereal" in input:
        return setSerial(input)
    elif "battery" in input:
        return setBatteries(input)
    elif "label" in input or 'indicator' in input:
        return setLabels(input)
    elif "strike" in input:
        return setStrikes(input)
    else:
        for key in moduleDescriptions:
            if key in input:
                workModule = moduleDescriptions[key](serialNumber, labels, numberOfBatteries, numberOfStrikes)
                return workModule.solve(input)
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

def setBatteries(input):
    global numberOfBatteries

    speechOutput = ""

    modifiedInput = input.split()

    for word in modifiedInput:
        if word in numbers:
            numberOfBatteries = numbers[word]
            speechOutput = f"There are {numberOfBatteries} batteries."
            return [0, speechOutput]

    speechOutput = f"Invalid input, please try again."
    return [-1, speechOutput]

def setStrikes(input):
    global numberOfStrikes

    speechOutput = ""

    modifiedInput = input.split()

    for word in modifiedInput:
        if word in numbers:
            numberOfStrikes = numbers[word]
            speechOutput = f"There are {numberOfStrikes} strikes."
            return [0, speechOutput]

    speechOutput = f"Invalid input, please try again."
    return [-1, speechOutput]

def setLabels(input):
    global labels

    speechOutput = ''
    labelAdded = ''
    labelLight = ''

    if 'off' in input or 'zero' in input or 'no light' in input or 'unlit' in input:
        if 'f r k' in input:
            labels['frk'] = 0
            labelAdded = 'f r k'
            labelLight = 'off'
        elif 'car' in input or 'c a r' in input:
            labels['car'] = 0
            labelAdded = 'c a r'
            labelLight = 'off'
        elif 's n d' in input or 's an d' in input:
            labels['snd'] = 0
            labelAdded = 's n d'
            labelLight = 'off'
        elif 'c l r' in input:
            labels['clr'] = 0
            labelAdded = 'c l r'
            labelLight = 'off'
        elif 'i n d' in input or 'i an d' in input:
            labels['ind'] = 0
            labelAdded = 'i an d'
            labelLight = 'off'
        elif 'f r q' in input:
            labels['frq'] = 0
            labelAdded = 'f r q'
            labelLight = 'off'
        elif 'n s a' in input or 'an s a' in input:
            labels['nsa'] = 0
            labelAdded = 'n s a'
            labelLight = 'off'
        elif 'm s a' in input:
            labels['msa'] = 0
            labelAdded = 'm s a'
            labelLight = 'off'
        elif 't r n' in input or 't r an' in input:
            labels['trn'] = 0
            labelAdded = 't r n'
            labelLight = 'off'
        elif 'b o b' in input:
            labels['bob'] = 0
            labelAdded = 'b o b'
            labelLight = 'off'
        else:
            speechOutput = f"Invalid input, please try again."
            return [-1, speechOutput]
    elif 'on' in input or 'one' in input or 'light' in input or 'lit' in input:
        if 'f r k' in input:
            labels['frk'] = 0
            labelAdded = 'f r k'
            labelLight = 'off'
        elif 'car' in input or 'c a r' in input:
            labels['car'] = 0
            labelAdded = 'c a r'
            labelLight = 'off'
        elif 's n d' in input or 's an d' in input:
            labels['snd'] = 0
            labelAdded = 's n d'
            labelLight = 'off'
        elif 'c l r' in input:
            labels['clr'] = 0
            labelAdded = 'c l r'
            labelLight = 'off'
        elif 'i n d' in input or 'i an d' in input:
            labels['ind'] = 0
            labelAdded = 'i an d'
            labelLight = 'off'
        elif 'f r q' in input:
            labels['frq'] = 0
            labelAdded = 'f r q'
            labelLight = 'off'
        elif 'n s a' in input or 'an s a' in input:
            labels['nsa'] = 0
            labelAdded = 'n s a'
            labelLight = 'off'
        elif 'm s a' in input:
            labels['msa'] = 0
            labelAdded = 'm s a'
            labelLight = 'off'
        elif 't r n' in input or 't r an' in input:
            labels['trn'] = 0
            labelAdded = 't r n'
            labelLight = 'off'
        elif 'b o b' in input:
            labels['bob'] = 0
            labelAdded = 'b o b'
            labelLight = 'off'
        else:
            speechOutput = f"Invalid input, please try again."
            return [-1, speechOutput]
    else:
        speechOutput = f"Invalid input, please try again."
        return [-1, speechOutput]

    speechOutput = f"Label {labelAdded} is {labelLight}."
    return [0, speechOutput]

