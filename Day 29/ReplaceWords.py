def word_replace(word):
    word_to_replace = input("Enter the word to replace: ")
    word_replacement = input("Enter the word replacement: ")
    print(word.replace(word_to_replace, word_replacement))

word = input("Enter a sentence: ")
word_replace(word)