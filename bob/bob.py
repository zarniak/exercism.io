def hey(phrase):
    if phrase.isspace() or not phrase: return 'Fine. Be that way!'
    if phrase.strip().find('?')+1 == len(phrase.strip()) and not phrase.isupper(): return 'Sure.'
    if phrase.strip().find('?')+1 == len(phrase.strip()) and phrase.isupper(): return 'Calm down, I know what Im doing!'
    if phrase.strip().find('!') and phrase.isupper(): return 'Whoa, chill out!'
    return 'Whatever.'
