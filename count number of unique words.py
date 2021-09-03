# analyze file

txt_file = open('demo.txt', 'rt')

ss =[]

for line_str in txt_file:
    ss.append(line_str.strip().split(" "))
    
print(ss)

# count number of words in file
txt_file = open("demo.txt", "rt")
data = txt_file.read()
words = data.split()

print('Number of words in text file: ', len(words))


# count number of unique words in file

txt_file = open("demo.txt", "r")
text = txt_file.read()

#here we clean the text i.e change all text into one format, upper or lower.
text = text.lower()
words = text.split()


#now we start counting

unique = []
for word in words:
    if word not in unique:
        unique.append(word)
        
unique.sort()

print(unique)
print("Number of unique words in the given text file are: ", len(unique))

# file will contain words, spaces, newlines only.

# what if 2 words differ by case of letters only? 
#do not consider the same words as unique, if same word but differ in case letter...
