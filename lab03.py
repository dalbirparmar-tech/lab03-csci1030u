# Fill in the body of each function below (look for the TODO comments).
#
# The function names and their arguments are already written for you - do NOT
# rename them or change their arguments, because the automated tests call them by
# name. Replace each `pass` with your code, and use `return` to send the answer
# back (not `print`).


def pig_latin(word):
    # TODO (Part 1): return the Pig Latin form of a single lowercase word.
    #   If it starts with a vowel (a, e, i, o, u): add "way" to the end.
    #   Otherwise: move the first letter to the end and add "ay".
    hasvowel: bool = ( (word[0]) == 'a' or (word[0]) == 'e' or (word[0]) == 'i' or (word[0]) == 'o' or (word[0]) == 'u')
    piglatinword = word
    if hasvowel:
        piglatinword += "way"
    else:
     piglatinword = piglatinword[1:] + piglatinword[0] + "ay"
    return piglatinword


def word_lengths(sentence):
    # TODO (Part 2): return a list with the length of each word in `sentence`
    #   (words are separated by spaces).
    list = []
    splitsentence = sentence.split(" ")

    if sentence == "":
        return []

    for n in range(len(splitsentence)):
        list.append(len(splitsentence[n]))

    return list


def reverse_words(sentence):
    # TODO (Part 3): return `sentence` with the order of its words reversed.
    #   e.g. "hello world" -> "world hello"
    splitsentence = sentence.split(" ")
    finalsentence = ""

    eachword = range(len(splitsentence) - 1, -1, -1)
    for n in eachword:
        finalsentence += splitsentence[n]
        if n != 0:
            finalsentence += " "

    return finalsentence


def letter_counts(text):
    # TODO (Part 4 - STRETCH, optional): return a dictionary mapping each letter
    #   to how many times it appears in `text`. Ignore case, and ignore anything
    #   that isn't a letter.
    dictionary = {}
    
    eachletter = range(0, len(text))
    for n in eachletter:
      letter = text[n].lower()      
      if not letter.isalpha():
        continue
      if dictionary.get(letter) == None:
         dictionary[letter] = 1
      else:
          dictionary[letter] += 1
        
    return dictionary


def main():
    # Optional scratch space - use this to try your functions with sample values.
    # print(pig_latin("banana"))                    # ananabay
    # print(word_lengths("the quick brown fox"))    # [3, 5, 5, 3]
    # print(reverse_words("the quick brown fox"))   # fox brown quick the
    # print(letter_counts("hello"))                 # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    pass


if __name__ == "__main__":
    main()
