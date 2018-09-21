def reverse(text):
    text_r = ''
    for x in text:
        text_r = x + text_r
    return text_r
print(reverse('dar'))
