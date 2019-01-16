import re

def abbreviate(words):
    return re.sub('[^A-Z]', '', words.replace("'", "").title())
