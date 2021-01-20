import warnings
import re
from .file_download import update_index
from .file_tools import validate_version, get_version_files_paths
from .exceptions import *
import hashlib

class Homework:
    #filepath
    #filehandle

    def __init__(self, hw_number, version, valid_versions, data_files, no_internet):
        self._hw_number = hw_number.lower()

        if not no_internet:
            try:
                update_index(self._hw_number)
            except NoInternetError:
                pass

        # Validate the version
        self._version = validate_version(version, self._hw_number, use_context="init", valid_versions=valid_versions)

        # Get the paths to the data files
        version_data_files = data_files[self._version]  # Get the data files for this version from the data files dictionary
        self._data_files_paths = get_version_files_paths(self._hw_number, self._version, version_data_files)

        #FIXME: Might need more code to make sure every file is up to date

        # Initialize dataframe and definitions dicts as empty for this parent class
        self._data = {}
        self._definitions = {}

    def list_data(self):
        print("Below are the dataframes contained in this dataset:")
        for name in sorted(self._data.keys(), key=str.lower):
            df = self._data[name]
            print("\t{}\n\t\tDimensions: {}".format(name, df.shape))


    def parseAnswers(self, file_path):
        self.answerFile = open(file_path, "r")
        tempArray = []
        for ans in self.answerFile:
            ans = ans.rstrip('\n')
            tempArray.append(ans)
        return tempArray

    def parseHints(self, file_path):
        tempDict = {}
        with open(file_path, 'r') as file_path:
            file_lines = file_path.readlines()
        quesNum = 1
        for line in file_lines:
            line = line.strip()
            if line.startswith('#'):
                quesNum = line[1:]
                newList = []
                tempDict[quesNum] = newList
            else:
                tempDict[quesNum].append(line)
        return tempDict

    def submit(self, qNum, guess, studentID):

        guess = str(guess)
        guess = self.hashGuess(str(guess))

        if self.ansArray[qNum - 1] == guess:
            #TODO: add student id google sheet stuff here

            return True
        else:
            return False

    def getHint(self, ques_num):
        #lessen hintNum to highest possible hint value
        if len(self.hintDict) < ques_num:
            return "Question number too high. Valid options are #1 - " + str(len(self.hintDict))
        ques_num = str(ques_num)  #cast to string for safety
        hints = "Question " + str(ques_num) + " hints:\n"
        for hint in self.hintDict[ques_num]:
            hints += "*" + str(hint) + "\n"
        hints = hints[:len(hints)-1]
        print(hints)
        # return hints

    def hashGuess(self, guess):
        hashedGuess = \
            hashlib.sha256(guess.encode()).hexdigest()
        # print(hashedGuess)
        return str(hashedGuess)
