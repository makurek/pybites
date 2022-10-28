"""
In this Bite you extract words from a text that contain
non-ascii characters. So Fichier non trouvé would
return a list of one matching word: ['trouvé'].

Calling extract_non_ascii_words with He wonede at
Ernleȝe at æðelen are chirechen it returns:
['Ernleȝe', 'æðelen'], etc.

See the tests for more. Have fun!
"""

input = "He wonede at Ernleȝe at æðelen are chirechen"

def is_unicode(word):
    for letter in word:
        if ord(letter) > 127:
            return True
        else:
            continue
    return False

def extract_non_ascii_words(text):
    """Filter a text returning a list of non-ascii words"""
    s = input.split()
    result = []
    for word in s:
        if is_unicode(word):
            result.append(word)
    return result

print(extract_non_ascii_words(input))