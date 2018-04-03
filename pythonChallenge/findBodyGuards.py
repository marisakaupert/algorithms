import re


def findBodyGuards(text_file):
    result_string = ""
    pattern = r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]'
    with open(text_file, "r") as lines:
        for line in lines:
            search = re.findall(pattern, line)
            for letter in search:
                result_string = result_string + letter

    print(result_string)


findBodyGuards("pageSource2.txt")

# Next url:
# http://www.pythonchallenge.com/pc/def/linkedlist.php
