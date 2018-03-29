def myfunc(word):
    new_word=""
    for index,letter in enumerate(word):
        if index%2 == 0:
            new_word += letter.upper()
        else:
            new_word += letter.lower()
    return (new_word)
myfunc('neena')
