Briefly:
    To run the program, please launch "__Main__.py" 
	from root/Program directory via Python 3.6.

Details:
    This program's purpose is to download all images from
    web page provided by user.

    It's written and debugged for Python v.3.6.4.

    This program is not supported by Python 2.7
    because of urllib (urllib2) limitations.

    Program consists of following modules:
    __Main__         - defines overall logic of program, responsible for program launching;
    FunctionsLibrary - contains all main program functions;
    Helpers          - contain axillary functions and decorators;
    Constants        - stores constants used in program.

Following external libraries used:
    os.path - for setting default path to current catalogue of program
    os.makedirs, remove - for creating / removing directories
    sys.stdout - for providing additional dynamic information to user in command prompt,
        e.g. progress of program run and countdown whe leaving the program
    time.sleep - for decorating program leaving simple countdown
    time.localtime, strftime - for getting time on the fly and converting it to necessary format
    urllib.request - for creating request to set URI with predefined headers and
        getting correspondent response
    bs4.BeautifulSoup - for reading loaded HTML with predefined HTML parser
    re.search - for getting image names from URIs via regular expression

Naming conventions used:
    CAPITALIZED_WITH_UNDERSCORES    - constants;
    lowercase_with_underscores      - variables;
    CamelCaseWording                - classes, modules;
    mixedCaseWording                - methods.

Virtual environment was used. Creation notes:
    1.	Create local folder, e.g.: D:\_Projects\FSecure\PicSaver
    2.	Add WORKON_HOME System Environment variables,
    set WORKON_HOME to D:\_Projects\FSecure\PicSaver
    4.	Run following query in command prompt:
    mkvirtualenv PicSaver
    5.	Run command in cmd.exe  OR  in PyCharm terminal:
    workon PicSaver

Please feel free to contact me in case of any questions,
feedback or concerns and issues.

    Regards,
        Max.
    max.fesenko1986@mail.com (C)
