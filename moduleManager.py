import os
import inspect
from importlib import import_module
from widgetManager import WidgetManager

moduleDescriptions = {
    #Fills up upon starting

    #Key: Description words
    #Value: Reference to class
}

moduleObjects = {
    #Fills up upon starting

    #Key: Description words
    #Value: Reference to object
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
        isPersistent = getattr(module, 'isPersistent')

        if isPersistent == True:
            persistentModule = moduleClasses[0][1](widgets)

            for description in descriptionWords:
                moduleObjects[description] = persistentModule
        for description in descriptionWords:
            moduleDescriptions[description] = moduleClasses[0][1]

def redirectInformation(input):
    output = widgets.checkKeys(input)

    if output[0] == -2:
        for key in moduleDescriptions:
            if key in input:
                if key in moduleObjects:
                    workModule = moduleObjects[key]
                    print("test")
                    
                    if "reset" in input:
                        workModule.reset(widgets)
                        result = [0, "Reset Successful"]    
                    else:
                        result = workModule.solve(input)
                else:
                    workModule = moduleDescriptions[key](widgets)
                    result = workModule.solve(input)
                return result

        return [-1, "Invalid input, please try again"]
    return output