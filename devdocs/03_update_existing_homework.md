# How to update an existing homework

**Steps for updating answers and hints for existing homeworks:**
1. Update the HW#.txt file for the appropriate homework.
2. Parse the HW#.txt file using the biograder.Parser() function.
    ```
    import biograder
    parser = biograder.Parser()
    parser.parseKey("path_to_answer_key.txt", "hw_name")
    ```
3. Go to the appropriate files in Box and use the "Upload New Version" button to upload the new answer and hint files.
4. Open the index.txt file for the homework you are updating, and select the button "Open" to open this file on your computer.
5. Re-hash the answer and hint files with md5sum, and update the index.txt file with their new hashes. (DO NOT change the version number or the shared file url in index.txt. That will break the system.)
6. Save the index.txt file to save your changes directly back to Box.
7. Re-hash the index.txt file with md5sum, and update index_hash.txt with the new hash.
8. Re-download the updated homework on Google Colab and test if the new answers and hints appear.

**Steps for updating code for an existing homework that requires a version update:**

Note: In the process of updating a homework, we want to be very careful that we don't break things for current users of the old homework while we're working on the update, and we want to make sure that after they have the updated package and data, they can still access the old data. I'll reiterate the following points in context in the instructions below, but to achieve these goals, make sure to do the following:

*   **Don't delete the old data files from Box**--leave them exactly as they are.
*   **Don't upload the new version of the index and index hash until the new package version is released on PyPI.** Otherwise, the package will be broken for all current users, because it will try to load the new data files, but it won't have the code for handling them, and will almost always run into errors.
*   **If/when you make ANY changes to the homework's class's __init__ function, don't delete whatever the old code was.** We need to preserve it, so the package can still load the old data versions. Instead, create an `if` statement that checks the self._version attribute, and if it's the old data version, runs the old code; else, if it's the new data version, run the new code.

**Important:** Whenever you're testing changes to your code, make sure to locally install the package using `pip`, using the following instructions. These instructions will take the local copy of the package that you've been editing and install it in your Anaconda environment's package installation directory. This will make it so that when you've opened a Python prompt or a Jupyter Notebook from that Anaconda environment and then import the package, you'll be importing your edited version of the package. This allows you to test the edits you've made, without having to push them to PyPI. So, to install your locally edited version of the package:
1. Open your Anaconda prompt or terminal
2. Activate your development environment (`conda activate MyEnvironment`, subbing in the name of your environment)
3. Navigate to the biograder directory that contains the `setup.py` file (which is the upper biograder directory, not the lower one). `pip` reads this file to know how to install the package.
4. In that directory, run this command: `pip install .` (don't forget the dot--it's a reference to your current directory, telling pip to build the package based on the `setup.py` file it finds in the current directory)
5. Alternatively, if you're in a different directory, you could run `pip install /path/to/biograder/directory/with/setup/py/file`, subbing in the proper path to the biograder `setup.py` file, and replacing / with \ if you're on Windows. `pip` will follow that path, find the `setup.py` file, and then install the package based off of it.

During the next several steps, you will be writing the code to load the new data version files. You want to be able to run this on your machine, so you can test the code as you work on it. However, you can't automatically do that, because when you create the dataset, the __init__ function will automatically update the dataset index, which will download the old version of the index, as stored on Box, which you don't want. However, you can't update the index on Box yet, because that would break the package for all current users trying to access the dataset.

    So, while you're working on the homework __init__ function, you need to go to the file biograder/homework.py and comment out the try/except block at the beginning of the function that calls update_index. Also comment out the line of code that validates the file version, since we don't have the indices necessary to do that; below it, add this line and comment: `self._version = version # TEMP FOR DEV; REPLACE W/ ABOVE WHEN DONE`.

1. Go through the raw data files from the new data release, and select which ones to download.
    A. For data files that were already included in the previous data version, you will often just use the corresponding file from the new data freeze. However, sometimes the new data freeze will have additional versions of the same data file, perhaps allowing you to get a version of the table generated by a different lab, using a different data transformation, or that groups the data in a different way. Consult the data freeze's README file to know which file is recommended for use in analysis--that's the one we want. Confirm with Dr. Payne.
    B. There also may be new data types that weren't included in the previous data version at all. For incorporating these new files, again consult the data freeze's README to know which version of the file to use, and confirm with Dr. Payne.
2. After downloading the files, gzip them (unless they're Excel files--leave those uncompressed).
3. Within the data directory for that dataset in the copy of the git repository on your local machine, create a directory for the new version. Name it with the format `[homework]_v[version]`. For example, if you were adding version 2.1 of the bio462_hw1 homework, you'd create the directory `bio462_hw1_v2.1/` within the directory `biograder/biograder/data_bio462_hw1/`. Copy the selected data files for the new version into this directory.
4. In the following steps, if you need to replace any existing code for loading and parsing the data, don't delete whatever the old code was. We need to preserve it, so the package can still load the old data versions. Instead, create an `if` statement that checks the self._version attribute, and if it's the old data version, runs the old code; else, if it's the new data version, run the new code.
5. Add the version number for the new data version to the valid_versions list at the beginning of the homeworks's __init__ function.
6. Edit the `data_files` dictionary created at the beginning of the homeworks's class's __init__ function, so that it contains a key that is the new version number, with a value that is a list of all the files in the new data version.
7. Write new `if`/`elif` statements in the dataframe loading portion of the __init__ function to load and parse any data files that weren't included in the previous data version. In those statements, add an additional condition that self._version match the new data version, so that the block won't be executed if they're loading the old version.
8. As necessary, edit the `if`/`elif` statements for data files that were already included in the previous data release. 
    A. You can usually use most of the same loading code to load and parse these files, if their format didn't change drastically. To check for differences, I recommend manually reading in the old and new versions of the file in a Python interpreter, using the pandas read_csv function, and comparing the two versions of the files. You can also manually type in the old loading and parsing code, but use it on the new file, and see if it works (or do this with the Python debugger).
    B. If you're using the same file between two versions, but the file name has changed, you'll have to edit the if statement so that it will accept both file names. So, instead of something like `if file_name == old_file_name:` you can say `if file_name in [old_file_name, new_file_name]:`
    C. As mentioned above, if you do need to make changes, **don't delete the old code**, because we still want to be able to load the old files. Instead, add an `if` statement that checks the data version (stored in the self._version attribute of the dataset class), and executes the old code if we're loading the old version, or executes the new code if we're loading the new version.
    D. There may have been conditional statements that were based on the version of the data--they would look like

        ```
        if self._version == "2.0":
            # Process older file version...
        elif self._version == "2.5":
            # Process new file version...
        ```

        If you were updating to data version 3.0, for example, but the particular file was the same as in version 2.5, you'd need to edit the conditional to look like the following, so that it would still process the file the same way as version 2.5:

        ```
        if self._version == "2.0":
            # Process older file version...
        elif self._version in ["2.5", "3.0"]:
            # Process new file version…
        ```


        To find all places where you'd need to make the edit, you could just do a search for the string `_version`.

9. Make a new index file and index hash. However, instead of creating a new index file, append the new indexing information to the end of the existing index file, to create something like this:

![bio462_hw1_multi_version_index](images/bio462_hw1_multi_version_index.png)
 (Note that even if a file stays exactly the same between two data versions, we still have a different copy of it in each version's data directory on Box, and thus have a unique shared URL for that file in that data version.)

10. If the homework was previously password protected but is now just under publication embargo:
    A. Go on Box and remove the password requirement from all the data files for all versions. You do this by clicking on a file, then clicking the "Share" button on the right hand side of the file's row, then clicking the "Link settings" button on the popup box, and then unchecking the "Require password" box on the next popup box.
    B. Remove the homework from the `password_protected_datasets` list in the `download` function in the `biograder/file_download.py` file
    C. Update the homeworks's data reuse status from "password access only" to "publication embargo" in the `list_datasets` function in the `biograder/__init__.py` file
    D. Change the password access only warning at the end of the homework's `__init__` function to be a publication embargo warning, with the publication embargo date.
11. If the homework was perviously under publication embargo but now has no restrictions:
    A. Update the homework's data reuse status from "publication embargo" to "no restrictions" in the `list_datasets` function in the `biograder/__init__.py` file
    B. Remove the publication embargo warning from the end of the homework's `__init__` function.
12. **IMPORTANT:** Uncomment the lines of code in the biograder/homework.py file that you commented out in step one, and delete the temporary line of code.
13. Release the new version of the package on GitHub and PyPI, following all of the instructions in the "release_new_package_version" document. Make sure to update the `version.txt` file on Box so users will know they need to update the package. Then, immediately after releasing the new package on PyPI, upload the updated homework's index and index_hash files on Box. 
    A. Make sure to update the files on Box quickly, because until the index and index hash files are updated, the package will be broken for anyone who tries to use the new package version. 
    B. **Make sure to re-hash the index, using md5sum, and to upload a new index hash file in addition to the new index.** If you don't, the package will think the index file was corrupted during downloads.
    C. While updating the files on Box, make sure to use the "Upload New Version" button for the existing versions of the files, instead of separately uploading the new versions of files, so that the shared URLs for the files don't change. If the URLs changed, it would make it so no one could download the files with the URLs embedded in the package.
