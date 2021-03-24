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
        self.ansArray = None
        self.answerFile = None
        self.hintDict = None

        # Keep track of answers marked correct
        self._student_ID = student_id
        self._student_answers = {}
        self._student_attempts = {}
        self._student_correct = {}

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
        question = 1
        for line in file_lines:
            line = line.strip()
            if line.startswith('#'):
                question = line[1:]
                newList = []
                tempDict[question] = newList
            else:
                tempDict[question].append(line)
        return tempDict

    def submit(self, question, answer):
        """Check if answer is correct, save answers, keep track of attempts, and return feedback.
            Parameters:
                question (int): The question number.
                answer (str): The answer to check.
            Returns:
                bool: True (correct) or False (incorrect).
        """
        hashedGuess = self.hashGuess(str(answer))
        self._student_attempts[question] = self._student_attempts.get(question, 0) + 1
        if self.ansArray[question - 1] == hashedGuess:
            self._student_correct[question] = "Yes"
            self._student_answers[question] = str(answer)
            return True
        else:
            if self._student_correct[question] == "Yes":  # Don't overwrite correct answer
                return False
            else:
                self._student_correct[question] = "No"
                self._student_answers[question] = str(answer)
                return False

    def getHint(self, question):
        """Return hints for the specified question number.
            Parameters:
                question (int): The question number.
            Returns:
                str: The hints.
        """
        if len(self.hintDict) < question:
            return "Question number too high. Valid options are #1 - " + str(len(self.hintDict))
        question = str(question)  # cast to string for safety
        hints = "Question " + str(question) + " hints:\n"
        for hint in self.hintDict[question]:
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
        print("\n{: ^60s}".format("SESSION SUMMARY"))
        print("------------------------------------------------------------")
        print("Student ID: {:>48s}".format(self._student_ID))
        print("Homework: {:>50s}".format(self._hw_number))
        print("------------------------------------------------------------")
        print("  Question  |  Correct  |  Attempts  |        Answer        ")
        numCorrect = 0
        for i in sorted (self._student_answers):
            out_string = "  {0: ^8}  |  {1: ^7}  |  {2: ^8}  |   {3}"
            print(out_string.format(i, self._student_correct[i], self._student_attempts[i], self._student_answers[i]))
            if self._student_correct[i] == "Yes":
                numCorrect += 1
        print("------------------------------------------------------------")
        percent = (numCorrect / len(self._student_answers)) * 100
        score = "Total Score: {0}/{1} = {2:.2f}%"
        print(score.format(numCorrect, len(self._student_answers), percent))

    def hashGuess(self, guess):
        hashedGuess = \
            hashlib.sha256(guess.encode()).hexdigest()
        return str(hashedGuess)
