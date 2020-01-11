# First, pip installing 'google' is necessary for this code to work.
# The module 'google' also has a dependency on 'beautifulsoup' but
# pip install should install 'beautifulsoup' automatically.
# Importing colorama and termcolor is optional, I'm using it only for text font color.

from googlesearch import search     # The main module needed to allow the google search.
from colorama import init           # Optional module to add color functionality.
from termcolor import colored       # Optional module to assign the colors to text.

# Using 'from' to reduce risks of name collisions

import sys              # To allow exiting the program from inside the program.
import webbrowser       # The main module needed to allow opening links.

init()      # Initializing colorama.
errorFontColor = 'red'
helpFontColor = 'green'


# Putting these variables outside the classes to ensure they are not edited accidentally.

class MainFunctions:
    def __init__(self, mode=1, printFontColor='white', inputFontColor='cyan', topLevelDomain='com', language='en',
                 resultAmount=10):      # Used to assign default settings.
        self.mode = mode
        self.printFontColor = printFontColor
        self.inputFontColor = inputFontColor
        self.topLevelDomain = topLevelDomain
        self.language = language
        self.resultAmount = resultAmount

    def settings(self):     # Used to start up the correct class function according to the setting the user chose.
        settingsOption = input(colored("Which setting would you like to change? ", self.inputFontColor))
        if settingsOption == "Mode" or settingsOption == "m":
            self.settingsmode()     # Starts up the class function to change the mode.
        elif settingsOption == "Print font color" or settingsOption == "p":
            self.settingsPrintFontColor()       # Starts up the class function to change the print font color.
        elif settingsOption == "Input font color" or settingsOption == "i":
            self.settingsInputFontColor()       # Starts up the class function to change the input font color.
        elif settingsOption == "Top Level Domain" or settingsOption == "t":
            self.settingsTopLevelDomain()       # Starts up the class function to change the top level domain.
        elif settingsOption == "Language" or settingsOption == "l":
            self.settingsLanguage()     # Starts up the class to change function the language of the results.
        elif settingsOption == "Result Amount" or settingsOption == "r":
            self.settingsResultAmount()     # Starts up the class function to change the amount of results which will appear.
        elif settingsOption == "help" or settingsOption == "h":     # A help command for the user to use if they want to see the possible commands for this class.
            print(colored("""
            Mode or m- The option to switch from basic and advanced.
            Print font color or p - The option to change the print font color.
            Input font color or i - The option to change the input font color.
            Top Level Domain or t - The option to change the top level domain.
            Language or l - The option to change the result language.
            Result Amount or r - The option to change how many results you see.
            help or h - The program will display this message.
            back or b - The program will display the previous section.
            """, helpFontColor))
            self.settings()     # Returns the user to the settings class instead of ending the program.
        elif settingsOption == "back" or settingsOption == "b":
            self.start()        # A command to return the user to the previous class function.
        else:
            print(colored("Error. Please input 'help' for a list of available commands.", errorFontColor))
            self.settings()     # Tells the user to use 'help' and returns them to the current class function.

    def settingsmode(self):     # Used to change the mode settings.
        modeInput = input(colored("Which mode would you like? ", self.inputFontColor))
        if modeInput == "basic" or modeInput == "b":        # If function to detect the possible correct inputs and
            self.mode = 1                                   # execute the correct code in response.
            self.settings()
        elif modeInput == "advanced" or modeInput == "a":
            self.mode = 2
            self.settings()
        elif modeInput == "help" or modeInput == "h":
            print(colored("""
            basic or b- The program will automatically open the first link that Google provides.
            advanced or a- The program will display links equal in amount with the value specified in Result Amount
                           before letting the user choose which link to open.
            help or h - The program will display this message.
            back or b - The program will display the previous section.
            """, helpFontColor))
            self.settingsmode()
        elif modeInput == "back" or modeInput == "b":
            self.settings()
        else:
            print(colored("Error. Please input 'help' for a list of available commands.", errorFontColor))
            self.settingsmode()

    def settingsPrintFontColor(self):       # Used to change the print font color.
        printFontColorInput = input(colored("What color would you like? ", self.inputFontColor))
        if printFontColorInput == "yellow" or printFontColorInput == "blue" or printFontColorInput == "magenta" or printFontColorInput == "cyan" or printFontColorInput == "white":     # If function to detect the possible correct inputs and execute the correct code in response.
            self.printFontColor = printFontColorInput
            self.settings()
        elif printFontColorInput == "green":
            print(colored("Green is used for help texts. Please pick another.", errorFontColor))
            self.settingsPrintFontColor()
        elif printFontColorInput == "red":
            print(colored("Red is used for error texts. Please pick another.", errorFontColor))
            self.settingsPrintFontColor()
        elif printFontColorInput == "help" or printFontColorInput == "h":
            print(colored("The available colors are:", helpFontColor))
            print(colored("yellow", "yellow"))      #Separate prints to showcase the different possible colors.
            print(colored("blue", "blue"))
            print(colored("magenta", "magenta"))
            print(colored("cyan", "cyan"))
            print(colored("white", "white"))
            print(colored("""
            Green and Red have been used for help and error texts respectively.
            help or h - The program will display this message.
            back or b - The program will display the previous section.
            """, helpFontColor))
            self.settingsPrintFontColor()
        elif printFontColorInput == "back" or printFontColorInput == "b":
            self.settings()
        else:
            print(colored("Error. Please input 'help' for a list of available commands.", errorFontColor))
            self.settingsPrintFontColor()

    def settingsInputFontColor(self):       # Essentially the same as above.
        inputFontColorInput = input(colored("What color would you like? ", self.inputFontColor))
        if inputFontColorInput == "yellow" or inputFontColorInput == "blue" or inputFontColorInput == "magenta" or inputFontColorInput == "cyan" or inputFontColorInput == "white":
            self.inputFontColor = inputFontColorInput
            self.settings()
        elif inputFontColorInput == "green":
            print(colored("Green is used for help texts. Please pick another.", errorFontColor))
            self.settingsPrintFontColor()
        elif inputFontColorInput == "red":
            print(colored("Red is used for error texts. Please pick another.", errorFontColor))
            self.settingsPrintFontColor()
        elif inputFontColorInput == "help" or inputFontColorInput == "h":
            print(colored("The available colors are:", helpFontColor))
            print(colored("yellow", "yellow"))
            print(colored("blue", "blue"))
            print(colored("magenta", "magenta"))
            print(colored("cyan", "cyan"))
            print(colored("white", "white"))
            print(colored("""
            Green and Red have been used for help and error texts respectively.
            help or h - The program will display this message.
            back or b - The program will display the previous section.
            """, helpFontColor))
            self.settingsInputFontColor()
        elif inputFontColorInput == "back" or inputFontColorInput == "b":
            self.settings()
        else:
            print(colored("Error. Please input 'help' for a list of available commands.", errorFontColor))
            self.settingsInputFontColor()

    def settingsTopLevelDomain(self):       # Used to change the Top Level Domain. Same concept as above.
        topLevelDomainInput = input(colored("Which Top Level Domain would you like? ", self.inputFontColor))
        if topLevelDomainInput == "com" or topLevelDomainInput == "net" or topLevelDomainInput == "co.id" or topLevelDomainInput == "com.sg":
            self.topLevelDomain = topLevelDomainInput
            self.settings()
        elif topLevelDomainInput == "org" or topLevelDomainInput == "edu" or topLevelDomainInput == "gov" or topLevelDomainInput == "uk" or topLevelDomainInput == "ca" or topLevelDomainInput == "de" or topLevelDomainInput == "jp" or topLevelDomainInput == "fr" or topLevelDomainInput == "au" or topLevelDomainInput == "us" or topLevelDomainInput == "ru" or topLevelDomainInput == "ch" or topLevelDomainInput == "it" or topLevelDomainInput == "nl" or topLevelDomainInput == "se" or topLevelDomainInput == "no" or topLevelDomainInput == "es" or topLevelDomainInput == "mil":
            print(colored("Please only use the 'com', 'net', 'co.id' and 'com.sg' TLDs. Indonesia seems to be blocking other TLDs. Once you connect to the 'co.id' TLD, Indonesia will force your requests back into 'co.id' no matter what you input and force the language into Indonesian."))
            self.settingsTopLevelDomain()
        elif topLevelDomainInput == "help" or topLevelDomainInput == "h":       # The code below are Google's TLD identifiers.
            print(colored("""
            The available TLDs are:
            com - Commercial
            org - Non-commercial
            edu - US accredited post-secondary institutions
            gov - United States Government
            uk - United Kingdom
            net - Network services
            ca - Canada
            de - Germany
            jp - Japan
            fr - France
            au - Australia
            us - United States
            ru - Russian Federation
            ch - Switzerland
            it - Italy
            nl - Netherlands
            se - Sweden
            no - Norway
            es - Spain
            mil - United States Military
            co.id - Indonesia
            com.sg - Singapore

            Note: This is not a complete list of TLDs, there are 273 TLDs currently offered by Google so this program
                  will only be accepting the top 20 most popular TLDs, Indonesian and Singaporean TLDs.

            IMPORTANT NOTE: Indonesia also seem to be intercepting the requests causing most TLDs to fail except for
                            'com', 'net', 'co.id' and 'com.sg'. It will first display results in english but after using
                            'co.id' once, Indonesia will force the requests back to the Indonesian TLD and Indonesian
                            language.

            help or h - The program will display this message.
            back or b - The program will display the previous section.
            """, helpFontColor))
            self.settingsTopLevelDomain()
        elif topLevelDomainInput == "back" or topLevelDomainInput == "b":
            self.settings()
        else:
            print(colored("Error. Please input 'help' for a list of available commands.", errorFontColor))
            self.settingsTopLevelDomain()

    def settingsLanguage(self):     # Used to change the language of the results.
        languageInput = input(colored("Which language would you like? ", self.inputFontColor))
        if languageInput == "en" or languageInput == "en-GB" or languageInput == "zh-CN" or languageInput == "zh-TW" or languageInput == "es" or languageInput == "hi" or languageInput == "ar" or languageInput == "ms" or languageInput == "ru" or languageInput == "bn" or languageInput == "pt-BR" or languageInput == "pt-PT" or languageInput == "fr" or languageInput == "id":
            self.language = languageInput
            self.settings()
        elif languageInput == "help" or languageInput == "h":       # Similar to the above, these are Google's language identifiers.
            print(colored("""
            The available languages are:
            en - English (US)
            en-GB - English (UK)
            zh-CN - Chinese (PRC)
            zh-TW - Chinese (Taiwan)
            es - Spanish
            hi - Hindi
            ar - Arabic
            ms - Malay
            ru - Russian
            bn - Bengali
            pt-BR - Portuguese (Brazil)
            pt-PT - Portuguese (Portugal)
            fr - French
            id - Indonesian

            Note: This is not a complete list of languages, there are 56 languages currently offered by Google so this
                  program will only be accepting the top 10 most spoken languages and Indonesian language.

            help or h - The program will display this message.
            back or b - The program will display the previous section.
            """, helpFontColor))
            self.settingsLanguage()
        elif languageInput == "back" or languageInput == "b":
            self.settings()
        else:
            print(colored("Error. Please input 'help' for a list of available commands.", errorFontColor))
            self.settingsLanguage()

    def settingsResultAmount(self):     # Used to change the amount of results the user gets.
        resultAmountInput = input(colored("How many results do you want to see? ", self.inputFontColor))
        if resultAmountInput == "back" or resultAmountInput == "b":
            self.settings()
        try:
            resultAmountInput = int(resultAmountInput)
        except ValueError:      # Detects string inputs which are not 'back' or 'b' which therefore are abnormal data inputs.
            print(colored("Input is invalid. Please only input integer values.", errorFontColor))
            self.settingsResultAmount()
        except NameError:       # To prevent errors related to the googlesearch module.
            print(colored("Input is invalid. Please only input integer values.", errorFontColor))
            self.settingsResultAmount()
        else:
            if resultAmountInput < 1:       # To prevent abnormal integer inputs which would cause an error during the search.
                print(colored("Input is invalid. Please only input integer values above 0.", errorFontColor))
                self.settingsResultAmount()
            self.resultAmount = resultAmountInput
            self.settings()

    def start(self):        # The starting 'menu' of sorts for the program.
        startInput = input(colored("What would you like to do? ", self.inputFontColor))
        if startInput == "Search" or startInput == "s":
            self.search()
        elif startInput == "Settings" or startInput == "se":
            self.settings()
        elif startInput == "help" or startInput == "h":
            print(colored("""
            Search or s - The program will initialize the search engine.
            Settings or se - The program will initialize the setting options.
            help or h - The program will display this message.
            Exit or e - The program will exit.
            """, helpFontColor))
            self.start()
        elif startInput == "Exit" or startInput == "e":
            print(colored("Thank you for using my program.", self.printFontColor))
            sys.exit()
        else:
            print(colored("Error. Please input 'help' for a list of available commands.", errorFontColor))
            self.start()

    def search(self):       # Used to trigger either the basic or advanced versions of the code.
        if self.mode == 1:
            self.basic()
        else:
            self.advanced()

    def basic(self):        # The basic program which automatically opens the first link Google provides.
        query = input(colored("What would you like to search? ('SearchExit' to exit) ", self.inputFontColor))       # Takes the item which the user wants to search.
        if query == "SearchExit":
            self.start()
        else:
            for i in search(query, stop=1):        # Searches the item, it will first output a generator which 'i' will convert into a link which we can actually use.
                webbrowser.open(i)      # Function used to open the link.
            self.basic()

    def advanced(self):     # The advanced program which will give the user a list of links for them to choose from.
        query = input(colored("What would you like to search? ('SearchExit' to exit) ", self.inputFontColor))       # The same as above.
        num = 1     # Just for allowing the use of numbered list.
        lst = []        # Initializing a list to allow link selection.
        if query == "SearchExit":
            self.start()
        else:
            for i in search(query, tld=self.topLevelDomain, lang=self.language, num=100, stop=self.resultAmount):
                print(colored(str(num) + ". " + i, self.printFontColor))        # Printing the numbered list.
                lst.append(i)
                num = num + 1
            try:
                choice = eval(input(colored("Which link would you like to open? ", self.inputFontColor)))
            except TypeError:
                print(colored("Input is invalid. Please only input integer values.", errorFontColor))
                self.advanced()
            else:
                try:
                    webbrowser.open(lst[choice - 1])
                except KeyError:
                    print(colored("Input is invalid. Please only input valid integers.", errorFontColor))
                    self.advanced()
                else:
                    self.advanced()

print("This program allows you to search google from python.\n")
m = MainFunctions()
m.start()       # Initiates the main program.