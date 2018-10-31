def hey(phrase):
    phrase_stripped = phrase.strip()
    if phrase_stripped.isspace() or not phrase_stripped:
        return 'Fine. Be that way!'
    if phrase_stripped.endswith('?') and phrase_stripped.isupper():
        return "Calm down, I know what I'm doing!"
    if phrase_stripped.endswith('?'):
        return 'Sure.'
    if phrase_stripped.isupper():
        return 'Whoa, chill out!'
    return 'Whatever.'
