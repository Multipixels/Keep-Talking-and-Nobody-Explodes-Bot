from widget import Widget

descriptionWords = ["stereo port", "stereo r c a port", "r c a port"]
tags = ["port"]

widgetName = "Stereo RCA Port"

class StereoRCAPortWidget:
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