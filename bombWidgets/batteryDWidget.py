from widget import Widget

descriptionWords = ["d battery", "d batteries"]
tags = ["battery"]

widgetName = "D Battery"

class DBatteryWidget:
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