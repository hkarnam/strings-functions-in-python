# A python program to reverse a string word by word and then swap the cases of letters

wo = "Python is Awesome"
new_wo = ""

words_split = wo.split(" ") # the whole string is now split into different words when there are spaces

for word in words_split:
    reversed_word = "".join(reversed(word)) # using a reversed function to reverse the word
    swapped_case = reversed_word.swapcase() # swapping lower case to upper and upper to lower
    new_wo += swapped_case + " "

new_wo = new_wo.rstrip()  # just incase if we have any extra spaces
print(new_wo)