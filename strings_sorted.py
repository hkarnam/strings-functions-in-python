# A python code to reverse a string word by word and sorting them in ascending order by each word

s = "Python IS Here"
new_s = ""

word_split = s.split(" ")

for word in word_split:   # for loop to iterate over the iterable word_split
    new_s += "".join(sorted(word.lower())) + " " # using lower() function to lower every element to work upon sorting

new_s = new_s.rstrip()
print(new_s)