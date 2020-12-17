word = input("Put the text in: ")
a = 0
i = 0
trigger = True
firstcommon = None
secondcommon = None
bruh = False
for char in word.lower():
    if char != ' ':
        if word.count(word[i]) > a:
            a = word.count(word[i])
            firstcommon = char
            secondcommon = None
        elif word.count(word[i]) == a and char != firstcommon and char != secondcommon :
            if trigger == True:
                secondcommon = char
                trigger = False
            else:
                print("Too many common characters!")
                break
        i = i+1
    else:
        if word.count(' ') > a:
            bruh = True
print("The most common character appeared ",a,"times. The most common character was:'",firstcommon,"'and '",secondcommon,"'")
if bruh == True:
    print("The most common character was an empty space.")
newword = ''
for char in word.lower():
    if char == firstcommon:
        newword = newword + "$"
    elif char == secondcommon:
        newword = newword + "*"
    else:
        newword = newword + char
print("The original text was: ",word)
print("The compressed text is: ",newword)
        
    
