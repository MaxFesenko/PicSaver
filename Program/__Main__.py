# This is the main module of the program.

# Setting global variable to reflect current program location
from os import path
__path__=[path.dirname(path.abspath(__file__))]
# Importing custom modules
from . import FunctionsLibrary as fl
from . import Constants as c
from . import Helpers as h


# Declaring main function of the program
#@h.unhandledExceptionProcessor
def mainFunction():
    # Introduction
    print(c.TEXT_INTRO)
    # Getting URL
    target_URL = fl.getWebPageURIFromPrompt(c.TEXT_INVITE_URL)
    print("URL: " + target_URL) #debug
    # Getting place for saving
    target_directory = fl.getTargetDirectory(c.TEXT_INVITE_DIR)
    print("Target directory: " + target_directory) #debug
    # Loading images and report to
    # target directory / [site name]_[date-time of loading launching] / [pic names]
    # and saving document with list of pics name and URLs:
    # target directory / [site name]_[date and time of loading launching]
    fl.loadImagesAndReport(target_URL, target_directory)
    h.sayingGoodByeToUser()

# Calling program in case of direct __Main__.py module launching
if __name__ == "__main__":
    mainFunction()
