# How to add files for new Homework assignment

>The Biograder package supports the addition of more homework
>assignemnts.  Follow this series of steps to make it work

## Prepare file(s) and parse
>The biograder has a built-in parser to format answer/hint files
>into their respective files.  The answer key with hashed values, 
>and the hints stored in plaintext.
 
>Format the master file to match the layout of 'example_unparsed_answer_key.txt' 
>located in the devdocs folder, matching the style of tab spacing, question number 
>formatting, and quotes around answer keys.

>With the answer key prepped, run the biograder through the command line.
>With the biograder installed, import it into a python window. 

```
import biograder
parser = biograder.Parser()
parser.parseKey("path_to_answer_key.txt", "hw_name")
# 1st parameter is the path to answer key file (if local just put the file name)
# 2nd parameter is the name of the hw assignment
for the biograder, we use this pattern: 'bio462_hw3'
```
>This should write the two formatted files to the directory that you ran the biograder in.
>The format of these files should mat

## Host files on Box

1. Download the answer file, hint file, and any extra data files onto your machine.
2. gzip the extra files, and keep the answer and hint files as txt
3. Use md5sum to hash all the files, and send the output to a file called `index.txt`.
4. Reformat this index.txt that you just created:
    1. On each line, have the file name and hash for one file. This is the format of the md5sum output, but you need to edit it so the filenames are first, followed by a tab and no other whitespace, followed by the file hash, followed by no other whitespace.
    2. At the top of the file, add a line that has the version number preceded by a crunch, e.g. "#3.1" for version 3.1
5. Create a folder on the Box drive for the new dataset, inside the `biograder` directory, with the format `[course]_[hw#]`, e.g. `bio462_hw3`. Within that folder, create another folder with a name formatted as `[course]_[hw#]_v[version]`, e.g. `bio462_hw3_v2.1`. Upload all the compressed data files, hashed answer file, and hint file to this second folder.
    1. To be clear, for the 3rd homework for BIO 462, you'd create `bio462_hw3` and `bio462_hw3/bio462_hw3_v2.1`, and upload the data files to `bio462_hw3/bio462_hw3_v2.1`
6. Create a shared direct download link for each file, and store it in index.txt:
    1. Click on the file
    2. Click on the "Share" button for the file
    3. In the box that pops up, click the switch to "Enable shared link"
    4. Change the access level from "Invited people only" to "People with the link", leaving the access level on "Can view and download"
    5. Click on the "Link settings" button, and at the bottom of the new box that pops up, you'll find the link to directly download the file, under the header "Direct Link". This is the link we need to put in our index; the link in the previous popup box was just for viewing the file.
        1. Optional: If you need to password protect the file (which isn't necessary for security of homework keys), check the "Require password" box under the "Password Protect" header and enter the desired password. It must be the same password for all files within one homework assignment.
    6. Copy the direct download link, and paste it into index.txt. Put it on the same line as the file it corresponds to, after the hash, separated from the hash by a tab and no other whitespace, and followed by no other whitespace.
7. Now that you've finished the index file, use md5sum to create a checksum for the index file, and store the hash in a file called `index_hash.txt`. md5sum will automatically output both the hash and file name, but you just want the hash, so delete the file name. Also make sure there is no whitespace before or after the hash.
8. Upload index.txt and index_hash.txt to the parent directory you created for the homework--for example, with the bio462 hw3 data, you'd upload them to the `bio462_hw3/` folder, not to `bio462_hw3/bio462_hw3_v2.1/`. 
9. Create shared direct download links for the index.txt and index_hash.txt files, following the same steps as for creating shared direct download links for the data files. Even if this is a password protected dataset, you do not need to password protect these files.
10. Within the biograder/biograder directory in the copy of the git repository on your local machine, create a directory for the dataset, with the format `data_[homework]`, e.g. `data_bio462_hw3`.
11. Within that directory, create a file called `index_urls.tsv`. The first line of this file should have the name of the index file (`index.txt`), followed by a tab, followed by the direct download link for the index file. The second line of this file should have the name of the index hash file (`index_hash.txt`), followed by a tab, followed by the direct download link for the index hash file. There must be no extra whitespace on either line.
12. Add index urls file to the MANIFEST.in file, which is in the same directory as setup.py
13. Add dataset's data folder to the .gitignore, which is in the same directory as setup.py, but use an exclamation point to include the index_urls.tsv file (see existing entries in the .gitignore for examples)

