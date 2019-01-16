import re


def abbreviate(words):
    return re.sub('[^A-Z]', '', re.sub('[^a-zA-Z]', '', words.replace("'", "").title()))
