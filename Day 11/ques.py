text = input()


length_words = 0
total_words = 0
words = text.split( )
    
for x in words:
    length_words += len(x)
    total_words += 1
    
average = length_words / total_words 

print(average)