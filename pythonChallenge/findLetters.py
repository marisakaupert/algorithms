import string


def findLetters(text_file):
    result_string = ""
    alphabet = string.ascii_lowercase
    with open(text_file, "r") as lines:
        for line in lines:
            for value in line:
                if value in alphabet:
                    result_string = result_string + value

    print(result_string)


findLetters("pageSource1.txt")

# Next url:
# http://www.pythonchallenge.com/pc/def/equality.html
