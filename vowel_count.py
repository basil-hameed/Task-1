# input - "Welcome to python session , eso
# output - count, individual count

# take user input string and ind char
my_string = "Welcome to python session"
count_characters = "eso"
characters_frequency = {}

# usig for loop to iterate and count the characters
for char in my_string: # w e l c o m e
    if char in count_characters: 
        if char in characters_frequency:
            characters_frequency[char] += 1 # characters_frequency[char] = characters_frequency[char] + 1
        else:
            characters_frequency[char] = 1

# printing the count and individual characters            
print(characters_frequency)
print(sum(characters_frequency.values()))