# Censor Words Longer Than Four Characters
# * Create a function that takes a string and censors words over four characters with *.

# ! Examples
# ? censor("The code is fourty") ➞ "The code is ******"

# ? censor("Two plus three is five") ➞ "Two plus ***** is five"

# ? censor("aaaa aaaaa 1234 12345") ➞ "aaaa ***** 1234 *****"
# ! Notes
# todo Don't censor words with exactly four characters.
# todo If all words have four characters or less, return the original string.
# todo The amount of * is the same as the length of the word.


def censor(x):
    y = x.split()
    t = [item for item in y if len(item)> 4]
    z = "".join(t)
    new_string = x.replace(z, "*****")
    return new_string
print(censor("Two plus three is five"))
print( censor("The code is fourty"))
print(censor("aaaa aaaaa 1234 12345"))






def censor(text):
    words = text.split()  # Split the text into words
    censored_words = []
    
    for word in words:
        if len(word) > 4:
            censored_words.append('*' * len(word))  # Replace word with asterisks
        else:
            censored_words.append(word)  # Keep the word as is
    
    return ' '.join(censored_words)  # Join the words back into a string

# Test cases
print(censor("The code is fourty"))  # ➞ "The code is ******"
print(censor("Two plus three is five"))  # ➞ "Two plus ***** is five"
print(censor("aaaa aaaaa 1234 12345"))  # ➞ "aaaa ***** 1234 *****"
