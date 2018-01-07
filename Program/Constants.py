# This module contains constants used in program.
# They are detached to simplify maintenance.

# Text constants for normal interaction w user:
TEXT_INTRO =\
    "\n----------------IMAGE   SCRAPPER---------------" \
    "\nThis program saves all images from web page provided by user." \
    "\nBy default images will be saved to folder from which the program is launched." \
    "\nThough user will be asked to change download folder."
TEXT_INVITE_URL = \
    "\n------Paste   URI   below end press Enter------\n" \
    "Please enter target web page URI," \
    " e.g.: https://www.pexels.com/search/cat/\n"
TEXT_INVITE_DIR = \
    "\n--Provide target directory for saving results--" \
    "\nPlease enter directory to save results to custom directory" \
    " ( e.g.: D:/folder/sub-folder/ ) and press Enter." \
    "\nOr just leave it blank and press Enter " \
    "to save results to default directory:\n"
# Mock of text for report file, where
# first %s is for string with successfully loaded images' URIs
# second %s is for string with URIs of images failed to load  b
TEXT_REPORT = \
    "----------Images loaded successfully----------\n" \
    "\n%s" \
    "\n    ---------Images failed to load----------\n" \
    "\n    %s"

# Text constants for errors:
ERROR_URI__PROTOCOL = \
    "URI INPUT ERROR: http(s):// protocol is missing in URI, try again."
ERROR_URI_NONE = \
    "URI INPUT ERROR: Wep page URI is not entered, try again."
ERROR_URI_OTHER = \
    "URI INPUT ERROR: No Way! URI is not valid, try again."
ERROR_GENERIC_UNHANDLED = \
    "\n----------------------------------------------" \
    "\n---------------------ERROR--------------------" \
    "\n----------------------------------------------" \
    "\nSorry, unexpected error occurred. Error: " \
    "\n%s" \
    "\nPlease send above error and target URI to max.fesenko1986@gmail.com\n"

# Primitive dictionary with parameters for request headers:
HEADERS = \
    {'User-Agent': 'Mozilla/5.0'}

# List of image extensions to work with:
IMG_EXTENSIONS = \
    ['.gif', '.jpg', '.png', '.jpeg']

INTERMEDIATE_CATALOGUE_NAME = "___saved_pictures/"

# Test constants used for debugging and testing:
TEST_URL = \
    "https://www.pexels.com/search/cat/"
TEST_DIRECTORY = \
    "D:/test"