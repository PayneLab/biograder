from .Homework import Homework
import os


# hw skeleton
class hw_name_or_abbreviation(Homework):

    # version="latest"
    def __init__(self, version="latest", no_internet=False):

        # Set some needed variables, and pass them to the parent Homework class __init__ function

        # This keeps a record of all versions that the code is equipped to handle. That way, if there's a new data release but they didn't update their package, it won't try to parse the new data version it isn't equipped to handle.
        valid_versions = ["""FILL: Insert valid data versions here."""]

        ###FILL: Insert actual data files below
        data_files = {
            ###START EXAMPLE CODE###############################################
            "version_num": [
                "answer-hash-file.txt",
                "hint-file.txt",
                "other_data_file.tsv"
            ],
            ###END EXAMPLE CODE#################################################
        }

        # Call the parent class
        super().__init__(hw_number="""FILL: Insert homework name or abbreviation here, in all lowercase""", version=version, valid_versions=valid_versions, data_files=data_files, no_internet=no_internet)
        
        # Load the data into dataframes in the self._data dict
        for file_path in self._data_files_paths:
            path_elements = file_path.split(os.sep)  # Get a list of the levels of the path
            file_name = path_elements[-1]  # The last element will be the name of the file

            # the file_name should be an expected pattern
            if file_name == "answer-hash-file-name.txt":
                self.ansArray = self.parseAnswers(file_path)
            elif file_name == "hint-file.txt":
                self.hintDict = self.parseHints(file_path)
            elif file_name == "other_data_file.tsv":
                # assign the file to whatever configuration you need for the assignment
                ###START EXAMPLE CODE###############################################
                self._data["dataframeName"] = pandas.read_csv(file_path, sep='\t', dtype=object)
                ###END EXAMPLE CODE#################################################
                
