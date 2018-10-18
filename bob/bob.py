def hey(phrase):
    phrase_stripped = phrase.strip()
    if phrase_stripped.isspace() or not phrase_stripped:
        return 'Fine. Be that way!'
    if phrase_stripped[-1] == '?' and not phrase_stripped.isupper():
        return 'Sure.'
    if phrase_stripped[-1] == '?' and phrase_stripped.isupper():
        return 'Calm down, I know what Im doing!'
    if '!' in phrase_stripped and phrase_stripped.isupper():
        return 'Whoa, chill out!'
    return 'Whatever.'
