import string


def remove_and_split(string, word):
    newstr = string.replace(word, "")
    return newstr.strip()

this = " Harry is a coder "
n = remove_and_split(this, "Harry")
print(n)