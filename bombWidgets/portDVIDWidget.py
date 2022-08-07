from widget import Widget

descriptionWords = ["d v i d port", "dvi d port"]
tags = ["port"]

widgetName = "DVID Port"

class DVIDPortWidget:
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