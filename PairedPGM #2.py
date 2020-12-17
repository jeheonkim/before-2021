a = 255 #dummy variable for the loop below
for i in range(5): #gets 5 inputs as strings
    word = input("put word in: ")
    b = ord(word[0]) #checks the first letter of each strings with ord funtion
    if b < a: #this if statement will only keep the word with lowest ord() value
        alpha = word
        a = b #updates the lowest ord(word) value 
print(alpha) 
