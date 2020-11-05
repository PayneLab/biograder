import warnings
import re
from .file_download import update_index
from .file_tools import validate_version, get_version_files_paths
from .exceptions import *

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
        self._version = validate_version(version, self._cancer_type, use_context="init", valid_versions=valid_versions)

        # Get the paths to the data files
        version_data_files = data_files[self._version]  # Get the data files for this version from the data files dictionary
        self._data_files_paths = get_version_files_paths(self._cancer_type, self._version, version_data_files)

        #FIXME: Might need more code to make sure every file is up to date

        # Initialize dataframe and definitions dicts as empty for this parent class
        self._data = {}
        self._definitions = {}

    def list_data(self):
        print("Below are the dataframes contained in this dataset:")
        for name in sorted(self._data.keys(), key=str.lower):
            df = self._data[name]
            print("\t{}\n\t\tDimensions: {}".format(name, df.shape))


    def parseAnswers(self, answerFile):
        tempArray = []
        for ans in answerFile:
            ans = ans.rstrip('\n')
            tempArray.append(ans)
        return tempArray

    def parseHints(self, hintFile):
        #return a dictionary or list or something
        pass

    def submit(self, guess, qNum, studentID):
        #bitGuess = str.encode(guess)
        #encrypt the submission
        #enc_guess = Encryptor().encrypt(bitGuess)

        if self.ansArray[qNum - 1] == guess:
            #add student id google sheet stuff here
            return True
        else:
            return False

    def getHint(self, hintNum):
        #lessen hintNum to highest possible hint value
        pass

