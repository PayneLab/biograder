from .file_download import update_index
from .file_tools import validate_version, get_version_files_paths
from .exceptions import *
import hashlib


class Homework:

    def __init__(self, hw_number, student_id, version, valid_versions, data_files, no_internet):
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

        # Initialize dataframe and definitions dicts as empty for this parent class
        self._data = {}
        self._definitions = {}
        self.answerFile = None

        # Keep track of answers marked correct
        self._student_ID = student_id
        self._student_answers = {}
        self._student_attempts = {}

    def listData(self):
        """Print a list of the dataframes contained in this dataset."""
        print("Below are the dataframes contained in this dataset:")
        for name in sorted(self._data.keys(), key=str.lower):
            df = self._data[name]
            print("\t{}\n\t\tDimensions: {}".format(name, df.shape))

    def version(self):
        """Return the dataset version of this instance, as a string."""
        return self._version

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

    def submit(self, quesNum, guess):
        """Check if answer is correct, save correct answers, and return feedback.
            Parameters:
                quesNum (int): The question number.
                guess (str): The answer to check.
            Returns:
                bool: True (correct) or False (incorrect).
        """
        hashedGuess = self.hashGuess(str(guess))
        self._student_attempts[quesNum] = self._student_attempts.get(quesNum, 0) + 1
        if self.ansArray[quesNum - 1] == hashedGuess:
            # Save answer to dictionary
            self._student_answers[quesNum] = str(guess)
            return True
        else:
            return False

    def getHint(self, quesNum):
        """Return hints for the specified question number.
            Parameters:
                quesNum (int): The question number.
            Returns:
                str: The hints.
        """
        if len(self.hintDict) < quesNum:
            return "Question number too high. Valid options are #1 - " + str(len(self.hintDict))
        quesNum = str(quesNum)  # cast to string for safety
        hints = "Question " + str(quesNum) + " hints:\n"
        for hint in self.hintDict[quesNum]:
            hints += "*" + str(hint) + "\n"
        hints = hints[:len(hints)-1]
        return hints

    def getData(self, name):
        """Check if a dataframe with the given name exists, and return a copy of it if it does.
            Parameters:
                name (str): The name of the dataframe to get.
            Returns:
                pandas.DataFrame: A copy of the desired dataframe, if it exists in this dataset.
        """
        if name in self._data.keys():
            df = self._data[name]
            return_df = df.copy(deep=True)  # We copy it, with deep=True, so edits on their copy don't affect the master for this instance
            return_df.index.name = df.index.name
            return_df.columns.name = df.columns.name
            return return_df
        else:
            raise DataFrameNotIncludedError(f"{name} dataframe not included in the {self._hw_number()} dataset.")

    def endSession(self):
        print("\n{: ^40s}".format("SESSION SUMMARY"))
        print("----------------------------------------")
        print("Student ID: {:>28s}".format(self._student_ID))
        print("Homework: {:>30s}".format(self._hw_number))
        if self._student_ID is None:
            print("\nNo answers were marked correct.")
        else:
            print("\nAnswers marked correct:")
            print("----------------------------------------")
            for i in sorted (self._student_answers):
                out_string = "Question: {0:2}    Attempts: {1:2}    Answer: {2}"
                print(out_string.format(i, self._student_attempts[i], self._student_answers[i]))

    def hashGuess(self, guess):
        hashedGuess = \
            hashlib.sha256(guess.encode()).hexdigest()
        return str(hashedGuess)
