from .Homework import Homework
import os


# hw skeleton
class bio462_hw6(Homework):

    # version="latest"
    def __init__(self, student_id, version="latest", no_internet=False):

        # Set some needed variables, and pass them to the parent Homework class __init__ function

        # This keeps a record of all versions that the code is equipped to handle. That way, if there's a new data release but they didn't update their package, it won't try to parse the new data version it isn't equipped to handle.
        valid_versions = ["1.0.0"]

        
        data_files = {
            
            "1.0.0": [
            "bio462_hw6_ans.txt",
            "bio462_hw6_hint.txt"],
            
        }

        #call the parent class
        super().__init__(hw_number="bio462_hw6", student_id=student_id, version=version, valid_versions=valid_versions, data_files=data_files, no_internet=no_internet)
        # need to reference file of answer key and hints
        for file_path in self._data_files_paths:
            path_elements = file_path.split(os.sep)  # Get a list of the levels of the path
            file_name = path_elements[-1]

            # the file_name should be an expected pattern
            if file_name == "bio462_hw6_ans.txt":
                self.ansArray = self.parseAnswers(file_path)
            elif file_name == "bio462_hw6_hint.txt":
                self.hintDict = self.parseHints(file_path)
