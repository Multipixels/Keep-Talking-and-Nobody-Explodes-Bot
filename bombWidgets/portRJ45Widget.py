from widget import Widget

descriptionWords = ["r j 45 port", "r j forty five port"]
tags = ["port"]

widgetName = "RJ45 Port"

class RJ45PortWidget:
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