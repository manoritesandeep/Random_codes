# Q: Write a program to input a row number (n), then print
#Pascal triangle, row 0 to n inclusive, in the format
#                            1
#                        1       1
#                       1    2    1
#                     1   3  3    1
#etc...


#involves three steps
#1. Input (No. of rows)

n = int(input("Enter the row number: "))

#2. list -> Nested -> Numbers : Get the numbers

list1 = []
for i in range(n):
    temp_list = []
    for j in range(i+1):
        if j==0 or j==i:   #assign beginning and ending values
            temp_list.append(1)
        else:
            temp_list.append(list1[i-1][j-1] + list1[i-1][j])
    list1.append(temp_list)

print(list1)

#above we store values into lists

#3. Desired shape of triangle.

for i in range(n):
    for j in range(n-i-1):
        print(format(" ","<2"), end = "")    #format helps us improve the distance and avoid table outlook when digits gets big.
    for j in range(i+1):     #for how many numbers we want in each row, like row 1 will have 1, row 2 will have 2, etc
        print(format(list1[i][j], "<3"), end = " ") #end is space cause there is space between two values.
    print()
 
    
 
    
 
    
 
    
 
    
 
    
 
#the above is the basic structure for pattern programming. 
#Other values like star (*) etc can be used to make good looking patterns.
