from widget import Widget

descriptionWords = ["a a battery", "double a battery", "a a batteries", "double a batteries"]
tags = ["battery"]

widgetName = "Double A Battery"

class AABatteryWidget:
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