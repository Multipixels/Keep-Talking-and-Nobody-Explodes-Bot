from widget import Widget

descriptionWords = ["serial port", "cereal port"]
tags = ["port"]

widgetName = "Serial Port"

class SerialPortWidget:
    def __init__(self):
        self.value = 0

    def setValue(self, input):
        self.value = input

    def getValue(self):
        return self.value

    def getWidgetName(self):
        return widgetName

    def getTags(self):
        return tags