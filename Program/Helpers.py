# Module with additional helper functions.

# Importing standard libraries
from sys import stdout
from time import sleep
# Importing custom modules
try:
    from . import Constants  as c
except:
    from Program import Constants  as c


# Converter of list to string with elements
# separated via logical OR operator
# (Note: particularly for this program this helps
# to get string of image extensions for using
# in regular expression and thus to set expressions
# only once - in Constants module):
def lstToStrWithOr(lst):
    img_extensions_str = ""
    for extension in lst:
        img_extensions_str = img_extensions_str \
                             + extension.replace(".","")\
                             + "|"
    return img_extensions_str[:len(img_extensions_str) - 1]

# Checking trailing slash and adding it if missing:
def lastSlashChecker(str):
    if str[len(str) - 1] != "/":
        str += "/"
    return str

# Getting site name from URI:
def gettingSiteNameFromUri(uri):
    site_name = uri.split("/")[2]
    return site_name

# Getting protocol from URI:
def gettingProtocolFromUri(uri):
    protocol = uri.split(":")[0]
    return protocol

# Getting combination of protocol and site name:
def gettingProtocolNDomainNameFromURI(uri):
    uriSplit = uri.split("/")
    protocolNDomain = uriSplit[0] + "//" + uriSplit[2] + "/"
    return protocolNDomain

# Adding progress notification:
def progressNotification(i, uri_lst):
    stdout.write("\r")
    stdout.write("Images are being loaded, please wait: "
                     + str("{0:.0f}%".format(100 * i / len(uri_lst))))
    stdout.flush()

# Countdown on user leaving
def goodByeCountDown():
    k = 3
    sleep_time = 0.8
    while k != 0:
        stdout.write("\r")
        stdout.write(str(k))
        stdout.flush()
        sleep(sleep_time)
        k -= 1

# Saying goodbye to user:
def sayingGoodByeToUser():
    print("\n------------------------------------------")
    input("\nPress Enter to quit the program.")
    print("\nBye!!!")
    #sleep(1.2)
    goodByeCountDown()

# Decorator for processing unhandled exceptions
def unhandledExceptionProcessor(func):
    def wrapper():
        try:
            func()
        except Exception as e:
            print(c.ERROR_GENERIC_UNHANDLED % e)
            sayingGoodByeToUser()
            quit()
    return wrapper
