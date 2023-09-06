"""Count words in file."""


# put your code here.
output_file = open("test.txt")

words = {}

for row in output_file: # loop over every line in the file
    data = row.rstrip().split()

    for word in data: # loop over every word in that line
        if word in words:
            words[word] += 1 
        else:
            words[word] = 1

for word, num in words.items():
    print(word, num)
