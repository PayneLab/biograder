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
parser.parseKey("path_to_answer_key.txt", "HW'-'_Ans.txt", "HW'-'_Hint.txt")
# 1st parameter is the path to answer key file (if local just put the file name)
# 2nd parameter is the name you want your hashed and formatted answer file to have (doesn't matter specifically)
# 3rd parameter is the same idea but with the name of the hint file
for the biograder, we use this pattern: 'bio462_hw3_ans.txt' and 'bio462_hw3_hint.txt'
```
>This should write the two formatted files to the directory that you ran the biograder in.
>The format of these files should mat

## Host files on Box
>

>Create a folder on the Box drive for the new dataset, inside the biograder/biograder 
>directory, with the format data_[which_homework], e.g. data_bio462_hw3. Within that 
>folder, 