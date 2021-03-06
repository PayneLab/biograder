import hashlib


class Parser:
    def __init__(self):
        pass

    # give path of base file, and desired hw name (bio462_hw3)
    def parseKey(self, file_path, hwName):
        """

        :param file_path: path to the RAW, unparsed answer/hint file formatted like "example_unparsed_answer_key.txt"
        :param hwName: the name of the hw assignment (the created ans and hint files will be named with this value
        """
        with open(file_path, 'r') as file_path:
            file_lines = file_path.readlines()

        answerText = ""
        hintsText = ""
        startHint = True
        toAppend = ""
        for line in file_lines:
            line = line.strip()
            if line.startswith('*'):
                endOfNum = self.find_nth(line, "*", 2)
                question_num = line[1:endOfNum]
                spaceShift = 1
                adjust = 1
                # count and adjust by the number of whitespace characters to avoid whitespace in the answer hash
                while str.isspace(line[endOfNum + adjust]):
                    adjust += 1
                    spaceShift = adjust

                answer = line[endOfNum+spaceShift:]
                # hashes each answer via SHA256
                answer = str(self._hashText(answer))

                toAppend = answer + "\n"
                answerText += toAppend
                startHint = True
            elif line.startswith('>'):
                start = line.find("\"") + 1
                end = line.find("\"", start + 1)
                hint = line[start:end]
                if startHint:
                    toAppend = "#" + question_num + "\n"
                    hintsText += toAppend
                    startHint = False
                toAppend = hint + "\n"
                hintsText += toAppend
        # make files
        answerText = answerText[:len(answerText)-1]
        hintsText = hintsText[:len(hintsText)-1]

        ansFileName = hwName + "_ans.txt"
        hintFileName = hwName + "_hint.txt"

        ansFile = open(ansFileName, "w")
        ansFile.write(answerText)
        ansFile.close()
        hintFile = open(hintFileName, "w")
        hintFile.write(hintsText)
        hintFile.close()

    def find_nth(self, text, toFind, n):
        """
        Returns the index of the next desired character for parsing select substrings
        """
        start = text.find(toFind)
        while start >= 0 and n > 1:
            start = text.find(toFind, start + len(toFind))
            n -= 1
        return start

    def _hashText(self, text):
        """
        Accepts String input, and converts it into its hash form.  Process cannot be reversed
        and is thus secure.
        """
        hashedText = \
            hashlib.sha256(text.encode()).hexdigest()
        return hashedText
