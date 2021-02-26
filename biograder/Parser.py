import hashlib


class Parser:
    def __init__(self):
        pass

    # give path of base file, and desired hw name (bio462_hw3)
    def parseKey(self, file_path, hwName):
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
                # TODO: instead of simply shifting over 2, check for the end of whitespace
                answer = line[endOfNum+2:]

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
        start = text.find(toFind)
        while start >= 0 and n > 1:
            start = text.find(toFind, start + len(toFind))
            n -= 1
        return start

    def _hashText(self, text):
        hashedText = \
            hashlib.sha256(text.encode()).hexdigest()
        return hashedText
