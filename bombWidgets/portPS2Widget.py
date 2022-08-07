from widget import Widget

descriptionWords = ["p s two port"]
tags = ["port"]

widgetName = "PS2 Port"

class PS2PortWidget:
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