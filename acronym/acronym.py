import re


def abbreviate(words):
    words_titled = words.replace("'", "").title()
    return re.sub('[^A-Z]', '', words_titled)
