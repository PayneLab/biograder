# How to add files for new homework assignments

>The biograder package supports the addition of more homework
>assignments.  Follow this series of steps to add a homework to the package.

>These instructions show how to edit all of the important files directly through the command line, but editing and creating the files through an IDE will work as well.

>In the coding examples we use bio462_hw3 as an example so it is clear what files you will be working with. Please substitute bio462_hw3 with the name of the homework being added.

## Clone the git repository

>Clone the repository in your desired directory.

```
git init
git clone https://github.com/PayneLab/biograder.git
```

>Change your working directory. Install the biograder onto your machine and start the python program.

```
cd biograder
pip install .
cd ..
pip install biograder
python
```

## Prepare file(s) and parse
>The biograder has a built-in parser to format answer/hint files
>into their respective files.  The answer key with hashed values,
>and the hints stored in plain text.

>Format the master file to match the layout of 'example_unparsed_answer_key.txt'
>located in the devdocs folder, matching the style of tab spacing, question number
>formatting, and quotes around answer keys.

>With the answer key prepped, run the biograder through the command line.
>Import the homework in the python window.

```
import biograder
parser = biograder.Parser()
parser.parseKey("path_to_answer_key.txt", "hw_name")
# 1st parameter is the path to new answer key file (if local just put the file name)
# 2nd parameter is the name or abbreviation of the hw assignment
for the biograder, we use this pattern: 'bio462_hw3'
```
>This should write the two formatted files to the working directory.

## Host files on Box

1. Download the answer file, hint file, and any other data files the homework will use onto your machine.
2. gzip the extra files, and keep the answer and hint files as .txt
3. Use md5sum to hash all the files, and send the output to a file called `index.txt`.

```
>touch index.txt
>md5sum bio462_hw3_ans.txt >> index.txt
>md5sum bio462_hw3_hint.txt >> index.txt

# if you are using a MacOS terminal, use md5 -r
```
4. Reformat the index.txt that you just created:
    1. Open the index.txt file you created.
```
nano index.txt
```
    2. At the top of the file, add a line that has the version number preceded by a crunch, e.g. `#3.1` for version 3.1
    3. Rearrange each line to have the file name, followed by a tab and no other whitespace, followed by the file hash, followed by no other whitespace. Stay in the text editor for now.

5. Create a folder on the Box drive for the new dataset, inside the `biograder` directory, with the format `[course]_[hw#]`, e.g. `bio462_hw3`. Within that folder, create another folder with a name formatted as `[course]_[hw#]_v[version]`, e.g. `bio462_hw3_v2.1`. Upload all the compressed data files, the original copy of the homework answer key, parsed answer file, and parsed hint file to this second folder.
    1. To be clear, for the 3rd homework for BIO 462, you'd create `bio462_hw3` and `bio462_hw3/bio462_hw3_v2.1`, and upload the data files to `bio462_hw3/bio462_hw3_v2.1`

6. Create a shared direct download link for each file:
    1. Click on the file
    2. Click on the "Share" button for the file
    3. In the box that pops up, click the switch to "Enable shared link"
    4. Change the access level from "Invited people only" to "People with the link", leaving the access level on "Can view and download"
    5. Click on the "Link settings" button, and at the bottom of the new box that pops up, you'll find the link to directly download the file, under the header "Direct Link". This is the link we need to put in our index; the link in the previous popup box was just for viewing the file.
        1. Optional: If you need to password protect the file (which isn't necessary for security of homework keys), check the "Require password" box under the "Password Protect" header and enter the desired password. It must be the same password for all files within one homework assignment.
    6. Copy the direct download link, and paste it into index.txt. Put it on the same line as the file it corresponds to, after the hash, separated from the hash by a tab and no other whitespace, followed by no other whitespace. To exit the text editor, type ctrl x.

7. Now that you've finished the index file, use md5sum to create a checksum for the index file, and store the hash in a file called `index_hash.txt`. md5sum will output both the hash and file name, but you only want the hash. Make sure there is no whitespace before or after the hash.

```
touch index_hash.txt
md5sum index.txt >> index_hash.txt
nano index_hash.txt
# delete file name and all whitespaces from file
# ctrl x to exit

# if you are using a MacOS terminal, use md5 -r
```

8. Upload index.txt and index_hash.txt to the parent directory you created for the homework on Box--for example, with the bio462 hw3 data, you'd upload them to the `bio462_hw3/` folder, not to `bio462_hw3/bio462_hw3_v2.1/`.

9. Create shared direct download links for the index.txt and index_hash.txt files, following the same steps as for creating shared direct download links for the data files. Even if this is a password protected dataset, you do not need to password protect these files.

10. Within the biograder/biograder directory in the copy of the git repository on your local machine, create a directory for the dataset, with the format `data_[homework]`, e.g. `data_bio462_hw3`.

```
cd biograder/biograder
mkdir data_bio462_hw3
```

11. Within that directory, create a file called `index_urls.tsv`. The first line of this file should have the name of the index file (`index.txt`), followed by a tab, followed by the direct download link for the index file. The second line of this file should have the name of the index hash file (`index_hash.txt`), followed by a tab, followed by the direct download link for the index hash file. There must be no extra whitespace on either line.

```
cd data_bio462_hw3
touch index_urls.tsv
nano index_urls.tsv
# write the file names with their box link
# ctrl x to exit
```

12. Add index urls file to the MANIFEST.in file

```
cd ..
cd ..
nano MANIFEST.in
# write in homework in the same format the other homeworks are written
# ctrl x to exit
```


## Adding the code for a new dataset

If you have already installed the biograder onto your machine, skip step #1.

1. **Important:** Whenever you're testing changes to your code, make sure to locally install the package using `pip`, using the following instructions. These instructions will take the local copy of the package that you've been editing and install it in your Anaconda environment's package installation directory. This will make it so that when you've opened a Python prompt or a Jupyter Notebook from that Anaconda environment and then import the package, you'll be importing your edited version of the package. This allows you to test the edits you've made, without having to push them to PyPI. So, to install your locally edited version of the package :
    1. Open your Anaconda prompt or terminal
    2. Activate your development environment (`conda activate MyEnvironment`, subbing in the name of your environment)
    3. Navigate to the biograder directory that contains the `setup.py` file (which is the upper biograder directory, not the lower one). `pip` reads this file to know how to install the package.
    4. In that directory, run this command: `pip install .` (don't forget the dot--it's a reference to your current directory, telling pip to build the package based on the `setup.py` file it finds in the current directory)
    5. Alternatively, if you're in a different directory, you could run `pip install /path/to/biograder/directory/with/setup/py/file`, subbing in the proper path to the biograder `setup.py` file, and replacing / with \ if you're on Windows. `pip` will follow that path, find the `setup.py` file, and then install the package based off of it.

2. Copy the child_dataset_template.py file to create a new class for the new dataset, inheriting from the abstract `Homework` class. When you copy the template to a new file, store the new file in the biograder/biograder/ directory, and set its name as the dataset's name or acronym, all lowercase, with .py as the extension. For example, the loader for the bio462 third homework is called `bio462_hw3.py`; for the same course's first homework, it's called `bio462_hw1.py`.
    1. The name of the class for the new dataset should be the dataset's name or acronym in `_` delimited lowercase_format. For example, the Bio 462 homework 3's class is `bio462_hw3`, and the 1st homework's class is `bio462_hw1`.
    2. See child_dataset_template.py for more info.

```
cp devdocs/child-dataset-template.py biograder/bio462_hw3.py
cd biograder
nano bio462_hw3.py
# replace all filler strings and function names with the correct homework number
# ctrl x to exit
```

3. At the top of `biograder/__init__.py`, add a line to import the dataset class from its file, using the lowercase file name and the homework name (e.g. `from .bio462_hw1 import bio462_hw1`)

```
nano __init__.py
# add import line
# ctrl x to exit
```

4. Add the new dataset name to the list of all datasets at the very beginning of the `download` function in `biograder/file_download.py` (located within the `if` statement that handles the case where the user passes `"all"` for the `dataset` parameter). If the homework is password protected, add it to the `password_protected_datasets` list in the `download` function. Also make sure it has a password access only warning at the end of its `__init__` function.

```
nano file_download.py
# add dataset name in if statement
# ctrl x to exit
```

## Testing the homework

You will want to test that the homework is uploaded correctly locally before you commit it to the repository.

1. Install biograder the same way you installed it at the beginning of these instructions. This will update the package with your new changes.

2. Open python.

```
>cd ..
>python
```

3. Import biograder and download the homework you added.

```
>import biograder
>biograder.download('bio462_hw3', version = 'latest')
>hw = biograder.bio462_hw3()
>hw.submit(question_number, answer, student_ID)
# Should return true
>hw.getHint(question_number)
# Should return all hints for that question
```
If the output is what you expect, you have added the homework correctly. Exit python.

4. Now you will push the changes to the biograder or sister repository you are creating in GitHub. To push your new files to the repository run this code while linked to your GitHub account. Make sure you are in the correct branch when you push.

```
cd biograder
# You should be in the same directory as setup.py
git add .
git commit -am “comment”
git push
```

Your additions should be in the GitHub. Merge into the main branch as needed or allowed.
