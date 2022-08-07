import os
import inspect
from importlib import import_module
from widgetManager import WidgetManager

moduleDescriptions = {
    #Fills up upon starting

    #Key: Description words
    #Value: Reference to class
}

# In charge of external Widgets. Holds information relevant to
# bomb widgets. Pass object onto module solution
widgets = WidgetManager()

# Fills up descriptions of moduleDescriptions
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
    output = widgets.checkKeys(input)

    if output[0] == -2:
        for key in moduleDescriptions:
            if key in input:
                workModule = moduleDescriptions[key](widgets)
                return workModule.solve(input)
        return [-1, "Invalid input, please try again"]
    return output