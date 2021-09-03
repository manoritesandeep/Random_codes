#use dictionary to count the unique words in a file.

#read the file
textFile = open('words.txt','r')
text = textFile.readlines()
#print(text)

#next: change the text into same format such as lowercase or uppercase

full = ""
for i in text:
    full = full + i.replace('\n', ' ')
#print(full)

full = full.strip()    #strip gets rid of extra spaces in the beginning or end.
full = full.lower()
full = full.split()
#print(full)

wordsDict = {}
#print(wordsDict)

#print(type(wordsDict))

for w in full:
    if w in wordsDict:
        wordsDict[w] = wordsDict[w] + 1
    else:
        wordsDict[w] = 1
    
print(wordsDict)

print('the number of unique words is: ', len(wordsDict))