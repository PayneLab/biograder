from .file_download import update_index
from .file_tools import validate_version, get_version_files_paths
from .exceptions import *
import hashlib
import gspread
from oauth2client.service_account import ServiceAccountCredentials


class Homework:
    # filepath
    # filehandle

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

        # FIXME: Might need more code to make sure every file is up to date

        # Initialize dataframe and definitions dicts as empty for this parent class
        self._data = {}
        self._definitions = {}
        self.answerFile = None

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
        guess = self.hashGuess(str(guess))

        if self.ansArray[qNum - 1] == guess:

            # fi
            # Connect to Google Sheets
            # scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets",
            #          "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
            # creds = ServiceAccountCredentials.from_json_keyfile_name("biograder/biograder/credentials.json", scope)
            # client = gspread.authorize(creds)
            #
            # # fixme: self._hw_number is now formatted as "bio462_hw3" instead of "hw3" for connection to sheets
            # # Update student grades
            # hwGrades = client.open("BiograderGrades").worksheet(self._hw_number)
            # studentIDs = hwGrades.col_values(1)
            # if studentID in studentIDs:
            #     studentIndex = studentIDs.index(studentID) + 1
            #     qNumIndex = qNum + 1
            #     hwGrades.update_cell(studentIndex, qNumIndex, 100)
            return True
        
        else:
            return False

    def getHint(self, ques_num):
        # lessen hintNum to highest possible hint value
        if len(self.hintDict) < ques_num:
            return "Question number too high. Valid options are #1 - " + str(len(self.hintDict))
        ques_num = str(ques_num)  # cast to string for safety
        hints = "Question " + str(ques_num) + " hints:\n"
        for hint in self.hintDict[ques_num]:
            hints += "*" + str(hint) + "\n"
        hints = hints[:len(hints)-1]
        print(hints)

    def hashGuess(self, guess):
        hashedGuess = \
            hashlib.sha256(guess.encode()).hexdigest()
        return str(hashedGuess)
