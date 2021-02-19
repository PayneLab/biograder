from .Homework import Homework
import os


class Homework18(Homework):

    # version="latest"
    def __init__(self, version="latest", no_internet=False):

        valid_versions = ["0.0.3", "1.0.0", "1.0.2"]

        data_files = {
            "0.0.3": [
                "HW18_Ans.txt",
                "HW18_Hint.txt"
            ],
            "1.0.0": [
                "HW18_Ans.txt",
                "HW18_Hint.txt"
            ],
            "1.0.2": [
                "HW18_Ans.txt",
                "HW18_Hint.txt"
            ],
        }

        super().__init__(hw_number="hw18", version=version, valid_versions=valid_versions, data_files=data_files, no_internet=no_internet)
        # need to reference file of answer key and hints
        for file_path in self._data_files_paths:
            path_elements = file_path.split(os.sep)  # Get a list of the levels of the path
            file_name = path_elements[-1]

            if file_name == "HW18_Ans.txt":
                self.ansArray = self.parseAnswers(file_path)
            elif file_name == "HW18_Hint.txt":
                self.hintDict = self.parseHints(file_path)
