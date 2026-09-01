def translate_word(word):

    vowels = "aeiou"

    if word[0] in vowels or word[:2] in ("xr", "yt"):
        return word + "ay"
    
    index = 0
    for i in range(len(word)):
        if word[i:i+2] == "qu":
            index = i + 2
            break
        elif word[i] in vowels:
            index = i
            break
        elif word[i] == "y" and i > 0:
            index = i
            break
        else:
            index = i + 1

    return word[index:] + word[:index] + "ay"

def translate(text):
    words = text.split()
    result = ""
    for word in words:
        if result != "":
            result = result + " "
        result = result + translate_word(word)
    return result