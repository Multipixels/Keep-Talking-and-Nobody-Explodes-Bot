import os;
import inspect
from importlib import import_module;

numbers = {
    'one': '1',
    'two': '2',
    'to': '2',
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
    'zero' : '0',
    'no': '0'
}

class WidgetManager():
    def __init__(self):
        self.widgetClass = {
            #Fills up upon starting

            #Key: Description words
            #Value: Reference to class
        }

        self.widgetName = {
            #Fills up upon starting

            #Key: Widget Name
            #Value: Object
        }

        self.widgetObject = {
            #Fills up upon starting

            #Key: Description words
            #Value: Object
        }

        for file in os.listdir(f"bombWidgets"):
            if file.endswith(".py") and file != '__init__.py':
                widgetName = file.split(".py")[0]
                widget = import_module(f"bombWidgets.{widgetName}")

                widgetClasses = inspect.getmembers(widget, inspect.isclass)
                widgetClasses = [x for x in widgetClasses if x[0] != 'Module']

                descriptionWords = getattr(widget, 'descriptionWords')
                widgetInternalName = getattr(widget, 'widgetName')
                
                newObject = widgetClasses[0][1]()

                for description in descriptionWords:
                    self.widgetClass[description] = widgetClasses[0][1]
                    self.widgetObject[description] = newObject
                self.widgetName[widgetInternalName] = newObject

        self.numberOfBatteries = 0
        self.numberOfStrikes = 0
        self.serialNumber = ""

        self.labels = {
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

    def checkKeys(self, rawInput):
        for key in self.widgetObject:
            if key in rawInput:
                for number in numbers:
                    if number in rawInput:
                        self.widgetObject[key].setValue(int(numbers[number]))
                        speechOutput = f"There are {self.widgetObject[key].getValue()} {self.widgetObject[key].getWidgetName()}."
                        
                        self.numberOfBatteries = 0

                        for widget in self.widgetObject:
                            if "battery" in self.widgetObject[widget].getTags():
                                self.numberOfBatteries += self.widgetObject[widget].getValue()

                        return [0, speechOutput]

                speechOutput = f"Invalid input, please try again."
                return [-1, speechOutput]

        if "serial" in rawInput or "cereal" in rawInput:
            return self.setSerial(rawInput)
        elif "battery" in rawInput or "batteries" in rawInput:
            return self.setBatteries(rawInput)
        elif "label" in rawInput or 'indicator' in rawInput:
            return self.setLabels(rawInput)
        elif "strike" in rawInput:
            return self.setStrikes(rawInput)       

        return [-2, ""]

    def setSerial(self, input):
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

        self.serialNumber = tempSerial[0:-1]
        
        speechOutput = f"Serial Number is {tempSerial}"
        return [0, speechOutput]

    def setBatteries(self, input):
        speechOutput = ""

        modifiedInput = input.split()

        for word in modifiedInput:
            if word in numbers:
                self.numberOfBatteries = int(numbers[word])
                speechOutput = f"There are {self.numberOfBatteries} batteries."
                return [0, speechOutput]

        speechOutput = f"Invalid input, please try again."
        return [-1, speechOutput]

    def setStrikes(self, input):
        speechOutput = ""

        modifiedInput = input.split()

        for word in modifiedInput:
            if word in numbers:
                self.numberOfStrikes = int(numbers[word])
                speechOutput = f"There are {self.numberOfStrikes} strikes."
                return [0, speechOutput]

        speechOutput = f"Invalid input, please try again."
        return [-1, speechOutput]

    def setLabels(self, input):
        speechOutput = ''
        labelAdded = ''
        labelLight = ''

        if 'off' in input or 'zero' in input or 'no light' in input or 'unlit' in input:
            if 'f r k' in input or 'f rk' in input:
                self.labels['frk'] = 0
                labelAdded = 'f r k'
                labelLight = 'off'
            elif 'car' in input or 'c a r' in input:
                self.labels['car'] = 0
                labelAdded = 'c a r'
                labelLight = 'off'
            elif 's n d' in input or 's an d' in input:
                self.labels['snd'] = 0
                labelAdded = 's n d'
                labelLight = 'off'
            elif 'c l r' in input:
                self.labels['clr'] = 0
                labelAdded = 'c l r'
                labelLight = 'off'
            elif 'i n d' in input or 'i an d' in input:
                self.labels['ind'] = 0
                labelAdded = 'i an d'
                labelLight = 'off'
            elif 'f r q' in input:
                self.labels['frq'] = 0
                labelAdded = 'f r q'
                labelLight = 'off'
            elif 'n s a' in input or 'an s a' in input:
                self.labels['nsa'] = 0
                labelAdded = 'n s a'
                labelLight = 'off'
            elif 'm s a' in input:
                self.labels['msa'] = 0
                labelAdded = 'm s a'
                labelLight = 'off'
            elif 't r n' in input or 't r an' in input:
                self.labels['trn'] = 0
                labelAdded = 't r n'
                labelLight = 'off'
            elif 'b o b' in input:
                self.labels['bob'] = 0
                labelAdded = 'b o b'
                labelLight = 'off'
            else:
                speechOutput = f"Invalid input, please try again."
                return [-1, speechOutput]
        elif 'on' in input or 'one' in input or 'light' in input or 'lit' in input:
            if 'f r k' in input:
                self.labels['frk'] = 1
                labelAdded = 'f r k'
                labelLight = 'on'
            elif 'car' in input or 'c a r' in input:
                self.labels['car'] = 1
                labelAdded = 'c a r'
                labelLight = 'on'
            elif 's n d' in input or 's an d' in input:
                self.labels['snd'] = 1
                labelAdded = 's n d'
                labelLight = 'on'
            elif 'c l r' in input:
                self.labels['clr'] = 1
                labelAdded = 'c l r'
                labelLight = 'on'
            elif 'i n d' in input or 'i an d' in input:
                self.labels['ind'] = 1
                labelAdded = 'i an d'
                labelLight = 'on'
            elif 'f r q' in input:
                self.labels['frq'] = 1
                labelAdded = 'f r q'
                labelLight = 'on'
            elif 'n s a' in input or 'an s a' in input:
                self.labels['nsa'] = 1
                labelAdded = 'n s a'
                labelLight = 'on'
            elif 'm s a' in input:
                self.labels['msa'] = 1
                labelAdded = 'm s a'
                labelLight = 'on'
            elif 't r n' in input or 't r an' in input:
                self.labels['trn'] = 1
                labelAdded = 't r n'
                labelLight = 'on'
            elif 'b o b' in input:
                self.labels['bob'] = 1
                labelAdded = 'b o b'
                labelLight = 'on'
            else:
                speechOutput = f"Invalid input, please try again."
                return [-1, speechOutput]
        else:
            speechOutput = f"Invalid input, please try again."
            return [-1, speechOutput]

        speechOutput = f"Label {labelAdded} is {labelLight}."
        return [0, speechOutput]

    def getSerial(self):
        return self.serialNumber

    def getBatteries(self):
        return self.numberOfBatteries

    def getStrikes(self):
        return self.numberOfStrikes

    def getLabels(self):
        return self.labels

    def getWidget(self, widgetNameInput):
        return self.widgetName[widgetNameInput].getValue()