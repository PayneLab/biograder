from .Homework import Homework
import os
import pandas as pd


# bio462_hw0
class bio462_hw0(Homework):

    # version="latest"
    def __init__(self, version="latest", no_internet=False):

        valid_versions = ["1.1.0"]

        data_files = {
            "1.1.0": [
                "bio462_hw0_ans.txt",
                "bio462_hw0_hint.txt",
                "randomData.txt.gz"
            ],
        }

        super().__init__(hw_number="bio462_hw0", version=version, valid_versions=valid_versions, data_files=data_files, no_internet=no_internet)

        # Load the data into dataframes in the self._data dict
        for file_path in self._data_files_paths:

            path_elements = file_path.split(os.sep)  # Get a list of the levels of the path
            file_name = path_elements[-1]  # The last element will be the name of the file

            if file_name == "bio462_hw0_ans.txt":
                self.ansArray = self.parseAnswers(file_path)
            elif file_name == "bio462_hw0_hint.txt":
                self.hintDict = self.parseHints(file_path)
            elif file_name == "randomData.txt.gz":
                self._data["randomData"] = pd.read_csv(file_path, sep='\t', dtype=object)
